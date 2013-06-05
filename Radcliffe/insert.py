# Module: insert.py

def row(cur, table, vals):

    qqq = '(' + ','.join(['?']*len(vals)) + ')'
    query = "INSERT INTO " + table + " VALUES " + qqq
    cur.execute(query, vals)

def rows(cur, table, manyvals):
    for vals in manyvals:
        row(cur, table, vals)

