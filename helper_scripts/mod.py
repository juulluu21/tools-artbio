#!/usr/bin/env python

import sys

input = open(sys.argv[1])
output = open(sys.argv[2], 'w')

for i,line in enumerate(input):
    if i==0:
        output.write(line)
    else:
        newline = []
        fields=line.strip().split('\t')
        for i, field in enumerate(fields):
            if not i==0:
                if len(field)>3:
                    field=field[:-3]+'.*?'
                else:
                    field='.*?'
            newline.append(field)
        output.write("\t".join(newline)+"\n")
input.close()
output.close()