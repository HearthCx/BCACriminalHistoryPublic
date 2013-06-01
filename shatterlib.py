import sys
def run():
    xml=open("../public.xml")
    i=0
    buf=""
    while True:
        try:
            sys.stdout.write("\rProcessing Record "+str(i))
            data=xml.next()
            if "</CriminalRecord>" in data:
                i+=1
                buf+=data.split("</CriminalRecord>")[0]
                buf+="</CriminalRecord>"
                outfile=open("sub/sub"+str(i)+".xml", 'w')
                outfile.write(buf)
                buf=data.split("</CriminalRecord>")[1]
            else:
                buf+=data
        except StopIteration:
            break
if __name__=="__main__":
    run()