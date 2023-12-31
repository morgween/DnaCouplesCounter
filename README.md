# About The project
The DNA Couples Counter is a program that takes a file containing DNA sequences, counts DNA pairs, and plots the contribution graph (histogram) of the data read from the file. The resulting histogram is saved to the results directory in the current working directory.

The project is compatible with Linux and any Darwin (macOS) machines.



  The project is compatible with Linux and any darwyn machines
## Build with:
* Nextflow - Workflow management
* Python 3.11.4 - Used for data analysis and plot creation
* Bash - Secondary scripts
## Requirements
### Nextflow Requirements
* Bash
* Java 11 (or later, up to 18)
* Git
* Docker
 ### Python Requirements
 * Python 3.0 or later to run the Python scripts in the project

## Getting started
  If you *don't* have the [nextflow](https://github.com/nextflow-io/nextflow) on your local machine:\
      - Option 1:  
        ``` curl -s https://get.nextflow.io | bash ```\
      - Option 2:  
        ``` wget -qO- https://get.nextflow.io | bash ``` \
      * After downloading Nextflow, make it executable with the following command:\
        ```chmod +x nextflow```\
      * Finally, add it to the PATH environment variable.

## Clone Repository
  If you already have Nextflow installed, you can clone the project repository with the following command:\
      ```git clone https://github.com/morgween/DnaCouplesCounter.git```
      

## Usage
  The workflow could be used in 3 different ways, if you already have Nextflow installed:\
    1. ``` nextflow main.nf --localPath full/path/to/sequencefile ```\
    2. * ``` nextflow main.nf --remotePath remote/path/to/sequencefile```\ 
    * ``` --remoteUser yourRemoteUsername ```\ 
    * ``` --serverIP serverThatContains.faFile ```\ 
    * ``` --i path/to/publicKey ```\
    3. Third option is to enter nextflow.config file and to change\
        * ```params.remoteUser = 'user'```\
        * ```params.i = "path/to/key"```\
        * ```params.serverIP = "127.0.0.1"```\
        If all entries are changed, you can use:\
      ```nextflow main.nf --remotePath remote/path/to/sequenceFile```

## License
Distributed under the MIT License. See LICENSE.txt for more information.



