import os, sys

merge_file = sys.argv[1]
out1 = sys.argv[2]
out2 = sys.argv[3]

with open(merge_file, 'r') as fin, open(out1,'w') as fout1, open(out2,'w') as fout2:
    for line in fin:
        array = line.strip().split(' ||| ')
        if len(array) != 2:
            continue
        fout1.write(array[0]+'\n')
        fout2.write(array[1]+'\n')
