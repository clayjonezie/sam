def alldata(db, table):
  cur = db.cursor()
  cur.execute("SELECT * FROM %s" % (db.escape_string(table),))
  return cur.fetchall()
  
