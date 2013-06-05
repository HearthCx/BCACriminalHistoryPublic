# Module: process_supervision.py
#
#   Extract the data from a SupervisionRecord element, then insert
#   into the SQL TABLE SupervisionRecord.
#
# Called from: process_criminal_record.py
#
# Requires:    get.py, insert.py

import get, insert

def run(b, s):
    b.supervisions += 1
    insert.row(b.cur, 'SupervisionRecord',
               (b.supervisions,
                b.subjects,
                get.text(s, 'ActivityDate'),
                get.text(s, 'SupervisionAgency/OrganizationName'),
                get.text(s, 'SupervisionAgency/OrganizationORIID/ID'),
                get.text(s, 'SupervisionChargeDisposition/StatusDescriptionText'),
                get.text(s, 'SupervisionConvictionCharge/ChargeClassification'),
                get.text(s, 'SupervisionConvictionCharge/ChargeStatute/StatuteCodeID/ID'),
                get.text(s, 'SupervisionConvictionCharge/ChargeStatute/StatuteDescriptionText'),
                get.text(s, 'SupervisionConvictionCharge/OriginatingAgencyCaseNumber/ID'),
                '/n'.join(get.Alltext(s, 'SupervisionConvictionCharge/Comment'))))
