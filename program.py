"""
Program de extras comentarii dintr-un cod sursa C

"""
from sys import argv

with open(argv[1]) as fisier:
    data=fisier.read()

index_lit = 0
comment=""
stareText = 0

def parcurgeText():
    global index_lit, comment, stareText
    if data[index_lit] == '"':
        stareText = 3
        index_lit += 1
        return
    
    if data[index_lit] == '/' and data[index_lit + 1] == '/':
        print "Comentariu cu '//':",
        comment = data[index_lit] + data[index_lit + 1]
        index_lit += 2
        stareText = 1
        return
    
    elif data[index_lit] == '/' and data[index_lit + 1] == '*':
		for x in range(index_lit,(len(data)-1)):
			if data[index_lit] == '*' and data[index_lit + 1] == '/': 
				print "Comentariu cu '/*' si '*/':",
				comment = data[index_lit] + data[index_lit + 1]
				index_lit += 2
				stareText = 2
    index_lit += 1
    
def parcurgeComment1():
    global index_lit, comment, stareText
    
    if data[index_lit] == '\n':
        stareText = 0
        index_lit += 1
        print comment
        print '__________________________________________________________'
        return
    else:
        comment = comment + data[index_lit]
        index_lit += 1
  
def parcurgeComment2():
    global index_lit, comment, stareText
    
    if data[index_lit] == '*' and data[index_lit + 1] == '/':
        stareText = 0
        index_lit += 2
        comment = comment + '*/'
        print comment
        print '__________________________________________________________'
        return
    else:
        comment = comment + data[index_lit]
        index_lit += 1

def parcurgeString():
    global index_lit, comment, stareText
    
    if data[index_lit] == '"' or data[index_lit] == '\n':
        stareText = 0
        index_lit += 1
        return
    else:
        index_lit += 1
        
        
while (index_lit < (len(data)-1)):
    if (stareText == 0):
        parcurgeText()
    elif stareText == 1:
        parcurgeComment1()
    elif stareText == 2:
        parcurgeComment2()
    elif stareText == 3:
        parcurgeString()

