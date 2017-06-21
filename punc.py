import nltk
from nltk.tokenize import word_tokenize
import sys
reload(sys)
sys.setdefaultencoding('utf8')

filename=sys.argv[1]#raw_input("Enter filename: ")
outFileName=sys.argv[2]
f = open(str(filename), 'r')
f1=open("temp",'w')

flag=1
while True:
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
for line in f2:
	t=word_tokenize(str(line))
	for i in range(len(t)):
		f3.write(str(t[i]))
		f3.write(" ")

f2.close()
f3.close()



