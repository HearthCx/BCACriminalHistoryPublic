# Module: process_criminal_record.py
#
# Extract the element PersonAlias and send it to process_alias.py
# Extract the element ConvictionRecord and send it to process_conviction.py
# Extract the element SupervisionRecord and send it to process_supervision.py
#
# These three elements contain all of the data in a criminal record.
#
# Called by: BCA.py
#
# Requires: process_alias, process_supervision, process_conviction, get

import process_alias, process_conviction, process_supervision, get

def run(b, Criminal_Record):

    Alias = get.node(Criminal_Record, 'Subject/PersonAlias')

    if Alias:

        process_alias.run(b, Alias)

        for x in Criminal_Record.findall('ConvictionRecord'):
            process_conviction.run(b, x)

        for x in Criminal_Record.findall('SupervisionRecord'):
            process_supervision.run(b, x)
