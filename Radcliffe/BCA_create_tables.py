#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('bca.db')

try:
    con = lite.connect('bca.db')
    cur = con.cursor()
    cur.executescript("""
        DROP TABLE IF EXISTS SubjectName;
        CREATE TABLE SubjectName(
            SubjectID INT not null,
            GivenName TEXT,
            MiddleName TEXT,
            SurName TEXT);
        DROP TABLE IF EXISTS SubjectBirthDate;
        CREATE TABLE SubjectBirthDate(
            SubjectID INT not null,
            BirthDate TEXT not null);
        DROP TABLE IF EXISTS ConvictionRecord;
        CREATE TABLE ConvictionRecord(
            ConvictionID INT primary key,
            SubjectID INT not null,
            ActivityDate TEXT,
            ConvictionCourtName TEXT,
            ConvictionCourtORIID TEXT,
            ControllingAgencyName TEXT,
            ControllingAgencyORIID TEXT,
            OriginatingAgencyCaseNumber TEXT,
            AssignedCustodialAgency TEXT,
            AssignedProbationAgency TEXT,
            StatementOfDisagreement TEXT,
            ChargeClassification TEXT,
            StatuteCodeID TEXT,
            StatuteDescription TEXT,
            CaseTrackingID TEXT,
            ChargeVerdict TEXT,
            PronouncedFine NUMERIC,
            AssessmentFee NUMERIC,
            StayedFine NUMERIC,
            Restitution NUMERIC,
            PronouncedSentence TEXT,
            ProbationalSentence TEXT,
            ConditionalConfinement TEXT,
            ConvictionLevel TEXT);
        DROP TABLE IF EXISTS SupervisionRecord;
        CREATE TABLE SupervisionRecord(
            SupervisionID INT primary key,
            SubjectID INT not null,
            ActivityDate TEXT,
            AgencyName TEXT,
            AgencyORIID TEXT,
            ChargeDisposition TEXT,
            ChargeClassification TEXT,
            ChargeCodeID TEXT,
            StatuteDescription TEXT,
            OriginatingAgencyCaseNumber TEXT,
            Comments TEXT);
    """)
    con.commit()
    print 'commit successful!'

except lite.Error, e:
    if con:
        con.rollback()
    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:
    if con:
        con.close()
        
