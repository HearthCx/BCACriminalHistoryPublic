# Module: main.py
from BCA import BCA
import sys
from time import time, localtime, strftime
import xml.etree.cElementTree as et
import sqlite3 as lite

def run():

    start = time()
    print 'Start time:',
    print strftime("%a, %d %b %Y %H:%M", localtime())

    db = 'bca.db'
    filename = '../public.xml'

    try:
        con = lite.connect(db)
        cur = con.cursor()
        infile = open(filename, 'r')
        
        b = BCA(cur,infile)
        b.run()

        con.commit()

    except lite.Error, e:

        if con:
            con.rollback()

        print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:

        infile.close()
        if con:
            con.close()

        elapsed = int(time() - start + 0.5)
        ss = elapsed % 60
        mm = (elapsed//60) % 60
        hh = elapsed//3600
        print "Running time: %d hr %d min %d sec" % (hh, mm, ss)

if __name__=="__main__":
    run()
