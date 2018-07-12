##reads file into string

infile = open('parsedClean.txt', 'r')
outfile = open('output.txt', 'w')

with open('parsedClean.txt','r') as f:
    for line in f:
        for word in line.split():
            if (word == "SBAR"):
                outfile.write(line)
            


infile.close()
outfile.close()





