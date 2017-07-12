import nltk
from nltk.tokenize import word_tokenize
import sys
reload(sys)
sys.setdefaultencoding('utf8')

filename=sys.argv[1]#raw_input("Enter filename: ")
outFileName=sys.argv[2]

# f = open(str(filename), 'r')
# f1=open("temp",'w')

# flag=1
# while True:
#     ch=f.read(1)
#     if not ch: break
#     if ch=='<':
#     	flag=0
    
#     if flag==1:
#     	f1.write(ch)
    
#     if ch=='>':
#     	flag=1
#     	f1.write(' ')	

# f.close()
# f1.close()

# f2=open("temp",'r')
# f3=open(str(outFileName),'w')
# for line in f2:
# 	t=word_tokenize(str(line))
# 	for i in range(len(t)):
# 		f3.write(str(t[i]))
# 		f3.write(" ")

# f2.close()
# f3.close()		

wordList=[]
puncList=[[",","?","!",".",":",";","-","..","...","....."],[",COMMA","?QUESTIONMARK","!EXCLAMATIONMARK",".PERIOD",":COLON",";SEMICOLON","-DASH",".PERIOD",".PERIOD",".PERIOD"],[0,0,0,0,0,0,0,0,0,0]]

f4=open("1"+str(outFileName),'w')	#without .
f3=open(str(outFileName),'r')		#with .
f6=open("2"+str(outFileName),'w') #with .PERIOD
for line in f3:
	for word in line.split():
		flag=0
		word1=word
		for i in range(len(puncList[0])):
			if puncList[0][i]==word:
				word1=puncList[1][i]
				puncList[2][i]+=1
				flag=1
				break
		f6.write(str(word1))
		f6.write(" ")
		if flag==0:
			f4.write(str(word.lower()))
			f4.write(" ")
		#wordList.append(word)
f5=open(str(outFileName)+"stats",'w')
for i in range(len(puncList[0])):
	f5.write(str(puncList[1][i])+"\t"+str(puncList[2][i])+"\n")

f5.close()
f4.close()
f3.close()
f6.close()




