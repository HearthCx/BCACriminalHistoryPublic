import sys
npf=100
npfc=1
i=1
buf=""
fnb="cct/cct"
fne=".xml"
inb="sub/sub"
ine=".xml"

while True:
	try:
		sys.stdout.write("\rWriting Concatenated File "+str(i)+" (Record "+str(npfc)+")")
		inf=open(inb+str(npfc)+ine, 'r')
		for ix in inf.readlines(): buf+=ix
		inf.close()
		npfc+=1
		if npfc>npf:
			ouf=open(fnb+str(i)+fne, 'w')
			ouf.write(buf)
			ouf.close()
			i+=1
			npfc=1
	except Exception as e: print str(e)