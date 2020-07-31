import sys

argv = sys.argv[1:]

with open(argv[0], 'r') as fr:
    with open(argv[1], 'w') as fw:
        
        for line in fr:
            fw.write(line)