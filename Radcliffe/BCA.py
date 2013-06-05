import xml.etree.cElementTree as et
import process_criminal_record

class BCA():
    def __init__(self, cur, infile):
        self.cur = cur
        self.infile = infile
        cur.execute('SELECT MAX(SubjectID) FROM SubjectName')
        self.subjects = cur.fetchone()[0] or 0
        
        cur.execute('SELECT MAX(ConvictionID) from ConvictionRecord')
        self.convictions = cur.fetchone()[0] or 0
        
        cur.execute('SELECT MAX(SupervisionID) from SupervisionRecord')
        self.supervisions = cur.fetchone()[0] or 0
        
    def run(self):
        begin_tag = "<CriminalRecord>"
        end_tag = "</CriminalRecord>"
        subjects = 0

        buf = ""
        for line in self.infile:
##            if self.subjects >= 50:
##                    xml_file.close()
##                    break
            line = str(line.strip())

            if end_tag in line:
                while end_tag in line:
                    line0, line1 = line.split(end_tag,1)
                    buf += line0 + end_tag
                    if begin_tag in buf:
                        buf = begin_tag + buf.split(begin_tag,1)[1]
                        buf = buf.replace('mnj:','').replace('j:','')
                        record = et.fromstring(buf)
                        process_criminal_record.run(self,record)
                        line = line1
                    buf = ''
                    line = line1
                        
                buf = line
            else:
                buf += line
            
        self.infile.close()

