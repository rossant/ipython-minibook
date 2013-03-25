import sys
import os
# we retrieve the folder as the first positional argument
# to the command-line call
if len(sys.argv) > 1:
    folder = sys.argv[1]
# we list all files in the specified folder
files = os.listdir(folder)
# ids contains the sorted list of all unique idenfitiers
ids = sorted(set(map(lambda file: int(file.split('.')[0]), files)))
