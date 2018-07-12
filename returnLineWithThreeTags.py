##reads file, returns lines that match two different grammar tags
##it's working well, but the text needs to have redundant lines and tags 
##removed with tagCleanup.py and deleteMultipleLines.py

infile = open('parsedClean.txt', 'r')
outfile = open('output.txt', 'w')

match1 = 0
match2 = 0
match3 = 0

with open('parsedClean.txt','r') as f:
    for line in f:
        for word in line.split():
            if (word == "NN"):
                match3 = 1
            if (word == "VBZ"):
                match1 = 1      
            if (word == "VBG"):
                match2 = 1
            if (match1 == 1 and match2 == 1 and match3 == 1):
                outfile.write(line)
        match1 = 0
        match2 = 0
        match3 = 0

                
            
##        if (match1 == 1 and match2 == 1): not working for some reason
##            
##            outfile.write(line)

infile.close()
outfile.close()





