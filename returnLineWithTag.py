##reads file into string

infile = open('parsedClean.txt', 'r')
outfile = open('output.txt', 'w')

with open('parsedClean.txt','r') as f:
    for line in f:
        for word in line.split():
            if (word == "SBARQ") or (word == "SBARQ") or (word == "SQ"):
                outfile.write(line)
            


infile.close()
outfile.close()

## I think the following serves as a 'question set' but I'm not 100%
## if (word == "SBARQ") or (word == "SBARQ") or (word == "SQ"):



