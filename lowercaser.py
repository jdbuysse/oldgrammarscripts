infile = open('tenderButtons.txt', 'r')
outfile = open('output.txt', 'w')

for line in infile:
  outfile.write(line.lower())



infile.close()
outfile.close()
