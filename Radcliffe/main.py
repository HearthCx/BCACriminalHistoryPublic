# Module: main.py
#
# This is the main module for the application.
# It creates an instance of the class BCA,
# which is used to update a database from an XML file.
#
# The input file is a data dump of criminal records from
# the Minnesota Bureau of Criminal Apprehensions, and the
# output file is an SQLite3 database.
#
# This module assumes that the database tables have already
# been created. If they do not exist, then they can be created
# using the module BCA_create_tables.py.
#
# The test script BCA_test.py can be used to verify that the
# data was inserted correctly.
#
#
#       Author: David G Radcliffe (dradcliffe@gmail.com)
#       Last modified 5 June 2013
#
#       License: Attribution-ShareAlike (CC-BY-SA)


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
