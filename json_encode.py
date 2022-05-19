import re
import os

with open('export.json', 'r') as input, open('output.json', 'w') as output:
    output.write('[\n')
    for line in input:
        line = re.sub('}{', '},\n{', line)
        output.write('    '+line)
    output.write("]\n")
input.close()
output.close()
os.remove("links.txt")
os.remove("export.json")