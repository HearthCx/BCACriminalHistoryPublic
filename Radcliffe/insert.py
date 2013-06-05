# Module: insert.py
#
# This module inserts values into a database table.
#   row  - insert a single row
#   rows - insert a list of rows
#
# Parameters:
#    cur - a database cursor
#    table - the name of an SQL table
#    vals - a tuple of values to insert
#    manyvals - a list of tuples to insert
#
# Called by: process_alias, process_supervision, process_conviction

def row(cur, table, vals):

    qqq = '(' + ','.join(['?']*len(vals)) + ')'
    query = "INSERT INTO " + table + " VALUES " + qqq
    cur.execute(query, vals)

def rows(cur, table, manyvals):
    for vals in manyvals:
        row(cur, table, vals)

