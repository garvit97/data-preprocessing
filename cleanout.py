
f1=open("lower2out.dev.txt",'w')	#all lowercase
f2=open("2out.dev.txt",'r')		#with .
punc=[",COMMA","?QUESTIONMARK","!EXCLAMATIONMARK",".PERIOD",":COLON",";SEMICOLON","-DASH"]
for line in f2:
	for word in line.split():
		flag=0
		for i in range(len(punc)):
			if punc[i]==word:
				f1.write(word)
				flag=1
				break
		if flag==0:
			f1.write(str(word).lower())
		f1.write(" ")

f1.close()
f2.close()