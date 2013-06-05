import get, insert

def run(b, Alias):
    b.subjects += 1
    for Name in Alias.findall('PersonName'):
        insert.row(b.cur, 'SubjectName', (
            b.subjects,
            get.text(Name, 'PersonGivenName'),
            get.text(Name, 'PersonMiddleName'),
            get.text(Name, 'PersonSurName')))

    for BDate in Alias.findall('PersonBirthDate'):
        insert.row(b.cur, 'SubjectBirthDate', (
            b.subjects,
            get.text(BDate)))
