lines_seen = set() # holds lines already seen


outfile = open('testing.txt', "w")

for line in open('outputClean.txt', "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
