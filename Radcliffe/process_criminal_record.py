import process_alias, process_conviction, process_supervision, get

def run(b, Criminal_Record):

    Alias = get.node(Criminal_Record, 'Subject/PersonAlias')

    if Alias:

        process_alias.run(b, Alias)

        for x in Criminal_Record.findall('ConvictionRecord'):
            process_conviction.run(b, x)

        for x in Criminal_Record.findall('SupervisionRecord'):
            process_supervision.run(b, x)
