def alldata(db, table):
  cur = db.cursor()
  cur.execute("SELECT * FROM %s" % (db.escape_string(table),))
  return cur.fetchall()

def col(db, table, col):  
  cur = db.cursor()
  cur.execute("SELECT %s FROM %s" % (db.escape_string(col), db.escape_string(table)))
  return [x[0] for x in cur.fetchall()]
