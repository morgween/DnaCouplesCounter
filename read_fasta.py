#!/usr/bin/env python
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


class Sequencer:
    def __init__(self):
        self.file_path = sys.argv[1]
        if not self.file_path:
            print("File wasn't found, try again")
            sys.exit(1)

    def read_sequences(self, file_path: str) -> dict[str, int]:
        self.results: dict[str, int] = {}
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('>'):  # no need to do anything
                    continue
                else:
                    for i in range(len(line)-2):
                        couple = line[i:i+2]
                        if (len(couple) < 2):
                            continue
                        if couple in self.results:
                            self.results[couple] += 1
                        else:
                            self.results[couple] = 1

    def create_histogram(self) -> None:
        fig, ax = plt.subplots(num=None, figsize=(
            16, 12), dpi=80, facecolor='w', edgecolor='k')

        # Get the maximum and minimum values from the results dictionary
        max_value = max(self.results.values())
        min_value = min(self.results.values())

        # Create a colormap with three colors: yellow, green, and red
        colors = [
            '#ABC270',  # green min
            '#77B7D7',  # blue others
            '#FEC868'  # yellow max
        ]

        # Plot the bars and set the colors based on the values
        for couple, value in self.results.items():
            color_index = 0
            if value == max_value:
                color_index = 2  # Green for max value
            elif value == min_value:
                color_index = 0  # Yellow for min value
            else:
                color_index = 1

            ax.bar(couple, value, color=colors[color_index])

        mean_value = np.mean(list(self.results.values()))
        ax.axhline(y=mean_value, color='r', linestyle='--', label='Mean')

        green_patch = mpatches.Patch(
            color=colors[0], label='Minimum of apperances')
        yellow_patch = mpatches.Patch(
            color=colors[2], label='Maximum of apperances')
        mean_line = mpatches.Patch(color='red', linestyle='--', label='Mean')
        ax.legend(handles=[green_patch, yellow_patch, mean_line])

        script_dir = os.path.dirname(os.path.realpath(__file__))
        new_file_path = os.path.join(script_dir, 'results')
        if not os.path.exists(new_file_path):
            os.makedirs(new_file_path)
        os.chdir(new_file_path)
        plt.savefig('histogram.png')


if __name__ == "__main__":
    solution = Sequencer()
    solution.read_sequences(solution.file_path)
    solution.create_histogram()
