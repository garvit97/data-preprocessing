import nltk
from nltk.tokenize import word_tokenize
import sys
reload(sys)
sys.setdefaultencoding('utf8')

filename=sys.argv[1]
outFileName=sys.argv[2]

f = open(str(filename), 'r')
f1=open("temp",'w')

flag=1
while True:  #To remove xml tags
    ch=f.read(1)
    if not ch: break
    if ch=='<':
    	flag=0
    
    if flag==1:
    	f1.write(ch)
    
    if ch=='>':
    	flag=1
    	f1.write(' ')	

f.close()
f1.close()

f2=open("temp",'r')
f3=open(str(outFileName),'w')
for line in f2:  #To write words in proper format(eah word separated by 1 space)
	t=word_tokenize(str(line))
	for i in range(len(t)):
		f3.write(str(t[i]))
		f3.write(" ")

f2.close()
f3.close()		

puncList=[[",","?","!",".","..","...","....",":",";","-","--","\"","\'","(",")","#"],[",COMMA","?QUESTIONMARK","!EXCLAMATIONMARK",".PERIOD","..DOUBLEDOTS","...TRIPLEDOTS","....FOURDOTS",":COLON",";SEMICOLON","-DASH","--DOUBLEDASH","\"DOUBLEQUOTES","\'SINGLEQUOTE","(BRACKETOPEN",")BRACKETCLOSE","#HASHTAG"],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

f4=open(str(outFileName)+"1",'w') #file that contains punctuations in format .PERIOD,!EXCLAMATIONMARK
f3=open(str(outFileName),'r')  #file that contains punctuations in format .,! 
for line in f3:
	for word in line.split():
		for i in range(len(puncList[0])):
			if puncList[0][i]==word:
				word=puncList[1][i]
				puncList[2][i]+=1
		f4.write(str(word))
		f4.write(" ")

f5=open(str(outFileName)+"stats",'w') #File that prints stats of punctuations
for i in range(len(puncList[0])):
	f5.write(str(puncList[1][i])+"\t"+str(puncList[2][i])+"\n")

f3.close()
f4.close()
f3.close()




