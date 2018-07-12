##THIS IS THE ONE THAT ACTUALLY WORKS

import re


##eventually fill in all this stuff with the treebank terms
replacement_patterns = [
##  (r'\bNN\b', ''),
##  (r'\bVBZ\b', ''),
##  (r'\bSBARQ\b', ''),
##  (r'\bCC\b', ''),
##  (r'\bSQ\b', ''),
##  (r'\bVP\b', ''),
##  (r'\bVBN\b', ''),
##  (r'\bPP\b', ''),
##  (r'\bIN\b', ''),
##  (r'\bNP\b', ''),
##  (r'\bPRP\b', ''),
##  (r'\bSBAR\b', ''),
##  (r'\bADJP\b', ''),
##  (r'\bDT\b', ''),
##  (r'\bSDS\b', ''),
##  (r'\bROOT\b', ''),
##  (r'\bJJ\b', ''),
##  (r'\bWH\b', ''),
##  (r'\bWDT\b', ''),
##  (r'\bP\b', ''),
##  (r'\bRB\b', ''),
##  (r'\bAD\b', ''),
##  (r'\bFW\b', ''),
##  (r'\bWRB\b', ''),
##  (r'\bTO\b', ''),
##  (r'\bVB\b', ''),
##  (r'\bWP\b', ''),
##  (r'\bPRT\b', ''),
##  (r'\bRP\b', ''),
##  (r'\bFRAG\b', ''),
##  (r'\bW\b', ''),
##  (r'\bVBG\b', ''),
##  (r'\bEX\b', ''),
##  (r'\bS\b', ''),
##  (r'\bFRAG\b', ''),
##  (r'\bW\b', ''),
##  (r'\bVBG\b', ''),
##  (r'\bEX\b', ''),
##  (r'\bS\b', ''),
("[A-Z]{2,6}", ''), ##catchall: pulls out all of the tags 2-6 letters in length
(r'\bS\b', ''), ##the stragglers: 'S' and 'A' tags
("[ ]{2,10}",' '), ##clearing out extra whitespaces (2-10 in a row)
#("[A-Z]{1}", "\n\1")
("(?P<FIRST>[.!?])", "\g<FIRST>"+ "\n")

]


##importing a file and turning it into a useable string
with open ("output.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')




##this takes a string, you have to turn your file into a string first
class RegexpReplacer(object):
  def __init__(self, patterns=replacement_patterns):
    self.patterns = [(re.compile(regex), repl) for (regex, repl) in 
      patterns]

  def replace(self, text):
    s = text
    for (pattern, repl) in self.patterns:
      s = re.sub(pattern, repl, s)
    return s

##now the actual function
from tagCleanup import RegexpReplacer
replacer = RegexpReplacer()

with open("outputClean.txt", "w") as text_file:
    text_file.write(replacer.replace(data))

    




