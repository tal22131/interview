import sys

filename = list(sys.argv)[2]


with open(filename, 'w') as f:
    f.write(".".join(filename.split(".")[:-1]))

