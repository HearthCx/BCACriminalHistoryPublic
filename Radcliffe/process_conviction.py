# Module: process_conviction.py
#
#   Extract the data from a ConvictionRecord element, then insert
#   into the SQL table ConvictionRecord.
#
# Called from: process_criminal_record.py
#
# Requires:    get.py, insert.py

import BCA, get, insert

def run(b, c):
    b.convictions += 1
    insert.row(b.cur, 'ConvictionRecord', (
        b.convictions,
        b.subjects,
        get.text(c, 'ActivityDate'),
        get.text(c, 'ConvictionCourt/OrganizationName'),
        get.text(c, 'ConvictionCourt/OrganizationORIID/ID'),
        get.text(c, 'ControllingAgency/OrganizationName'),
        get.text(c, 'ControllingAgency/OrganizationORIID/ID'),
        get.text(c, 'ControllingAgency/OriginatingAgencyCaseNumber/ID'),
        get.text(c, 'AssignedCustodialAgency/OrganizationName'),
        get.text(c, 'AssignedProbationAgency/OrganizationName'),
        get.text(c, 'StatementOfDisagreement'),
        get.text(c, 'ConvictionCharge/ChargeClassification/ChargeApplicabilityText'),
        get.text(c, 'ConvictionCharge/ChargeStatute/StatuteCodeID/ID'),
        get.text(c, 'ConvictionCharge/ChargeStatute/StatuteDescriptionText'),
        get.text(c, 'ConvictionCharge/ConvictionCourtCase/CaseTrackingID/ID'),
        get.text(c, 'ConvictionCharge/ChargeDisposition/ChargeDispositionVerdict/VerdictDescriptionText'),
        get.text(c, 'ConvictionCharge/ChargeDisposition/PronouncedFine/ObligationAmount'),
        get.text(c, 'ConvictionCharge/ChargeDisposition/AssessmentFee/ObligationAmount'),
        get.text(c, 'ConvictionCharge/ChargeDisposition/StayedFine/ObligationAmount'),
        get.text(c, 'ConvictionCharge/ChargeDisposition/Restitution/ObligationAmount'),
        get.text(c, 'ConvictionCharge/ChargeDisposition/PronouncedSentence/TermDuration'),
        get.text(c, 'ConvictionCharge/ChargeDisposition/ProbationalSentence/TermDuration'),
        get.text(c, 'ConvictionCharge/ChargeDisposition/ConditionalConfinement/TermDuration'),
        get.text(c, 'ConvictionCharge/ConvictionLevel')))
 
    
    

    
