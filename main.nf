#!/usr/bin/env nextflow

/*
 *  If localPath specified - local file system will be used
 *  remotePath - path on remote server
 *  remoteUser - user on remote server
 *  serverIP - IP address of remote server
 *  i - path to public key
 */

nextflow.enable.dsl = 2

params.localPath = ''
params.remotePath = ''
params.remoteUser = ''
params.serverIP = ''
params.i = ''  

process fastaFile_fromRemote{
    input:
    val remotePath
    val remoteUser
    val serverIP
    val i
    
    output: 
    path fastaFile

    script:
    """
    #!/bin/bash
    scp -i ${i} ${remoteUser}@${serverIP}:${remotePath} fastaFile
    """
}
process fastaFile_fromLocal{
    input:
    path localPath
    output:
    path fastaFile 
    script:
    """
    #!/bin/bash
    # Function to perform the copy operation
    perform_copy() {
        cp ${1} fastaFile
    }
    
    # Attempt the initial copy
    perform_copy (${localPath})
    
    # Check if the copy was successful
    if test -f "fastaFile"; then
        
    else
        # Retry with a different path
        perform_copy "${baseDir}/${localPath}"
    fi
    """

}

process pyTask{
    debug true
    input: 
    path fastaFile
    output: 
    stdout
    script:
    """
        #!/bin/bash
        python3 ${baseDir}/read_fasta.py ${fastaFile}
    """

}

workflow{
    if (params.localPath != ''){
        if(params.remotePath != ''){
            println("Error: localPath and remotePath cannot be specified at the same time")
            exit 1
        }
        fasta_ch = fastaFile_fromLocal(params.localPath)
    }
    else if(params.remotePath != ''){
        if(params.localPath != ''){
            println("Error: localPath and remotePath cannot be specified at the same time")
            exit 1
        }
        if(params.remoteUser == 'user' || params.i == "path/to/key" || params.serverIP == "127.0.0.1")
        {
            println("Error: remoteUser, serverIP and publicKey must be specified")
            exit 1
        }
        fasta_ch = fastaFile_fromRemote(params.remotePath, params.remoteUser, params.serverIP, params.i)
    }
    else{
        println("Error: localPath or remotePath must be specified")
        exit 1
    }
    pyTask(fasta_ch)
}
