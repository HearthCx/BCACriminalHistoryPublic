

a = """
    GivenName
	MiddleName
	SurName
"""

b = """
	SubjectID
	BirthDate
"""

c = """
	ConvictionID
	SubjectID
	ActivityDate
	ConvictionCourtName
	ConvictionCourtORIID
	ControllingAgencyName
	ControllingAgencyORIID
	OriginatingAgencyCaseNumber
	AssignedCustodialAgency
	AssignedProbationAgency
	StatementOfDisagreement
	ChargeClassification
	StatuteCodeID
	StatuteDescription
	CaseTrackingID
	ChargeVerdict
	PronouncedFine
	AssessmentFee
	StayedFine
	Restitution
	PronouncedSentence
	ProbationalSentence
	ConditionalConfinement
	ConvictionLevel
"""

d = """
	SupervisionID
	SubjectID
	ActivityDate
	AgencyName
	AgencyORIID
	ChargeDisposition
	ChargeClassification
	ChargeCodeID
	StatuteDescription
	OriginatingAgencyCaseNumber
	Comments
"""

import re
import sqlite3 as lite
import sys, os

try:

    con = lite.connect('../bca.db')
    cur = con.cursor()

    for table, s in (('subjectname', a), ('subjectbirthdate', b),
                     ('convictionrecord', c), ('supervisionrecord', d)):
        for column in re.findall('(\w+)', s):
            query = "select max(%s) from %s where %s != ''" % (column, table, column)
            cur.execute(query)
            row = cur.fetchall()[0]
            print table, column, row[0]

except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()

