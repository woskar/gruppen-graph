#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi, os.path

DEFAULT_NAME = "OhneName"
DEFAULT_ADDR = "OhneName"


def main():
    form = cgi.FieldStorage()
    print('Hey cool, das hat geklappt :D<br/>Vielen Dank fürs Eintragen.<br/><br/>')
    name = form.getfirst("name", DEFAULT_NAME)
    addr = form.getlist("addr")
    print('Dein Name:', str(name), '<br/>')
    print('Freunde:', str(addr))
    text = '"' + str(name)+'": ' + str(addr) + '\n'
    with open('graphData.txt','a') as fileOutput:
        	fileOutput.write(text)


    
def processInput(name, addr):  
    '''Process input parameters and return the final page as a string.'''
    fileName= "namelist.txt"
    if name != DEFAULT_NAME or addr != DEFAULT_ADDR:
        #line = "Name: {name}  Address:  {addr}\n".format(**locals())
        #line = "{name}, {addr}\n".format(**locals())
        line = "{name}, {addr}\n".format(**locals())
        #liste = request.POST.getlist('addr')
        #line = (**locals()[0])
        
        #for i in liste:
        #    line += ', ' + str(liste[i])
        append(fileName, line)
    lines = fileLinesToHTMLLines(fileName)
    return 

def append(fileName, s):
    """Append string s to file with name fileName.
    This fails if there are multiple people trying simultaneously.
    """
    fout = open(fileName,'a') # 'a' means append to the end of the file
    fout.write(s)
    fout.close()

def safePlainText(s):
    '''Return string s with reserved html markup characters replaced
    and newlines replaced by <br>.'''
    result = s.replace('&', '&amp;').replace('<', '&lt;').replace('\n', '<br>')
    print('Test safe Plain Text')
    return result

def fileLinesToHTMLLines(fileName):
    """Allow lines of the file with name fileName to be embedded in html.
    This fails if there are multiple people trying.
    Alters code with possible tags.
    Returns the empty string if fileName does not exist
    """
    
    safeLines = list()
    if os.path.exists(fileName): # test if the file exists yet
        lines = fileToStr(fileName).splitlines()
        for line in lines:
            safeLines.append(safePlainText(line))
    return "<br>\n".join(safeLines)
    
# standard functions and code from here on
def fileToStr(fileName): 
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close()
    return contents

try:
    print("Content-type: text/html\n\n")   # say generating html
    print('<head><meta charset="utf-8"/></head>')
    main()
except:
    cgi.print_exception()                 # catch and print errors

