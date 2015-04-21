def tables(db):
  cur = db.cursor()
  cur.execute("select table_name from information_schema.tables where table_schema='sam'")
  tables = [i[0] for i in cur.fetchall()]
  return tables

def columns(db, table):
  cur = db.cursor()
  cur.execute("select COLUMN_NAME from information_schema.columns where TABLE_NAME=%s", (table,))
  tables = [i[0] for i in cur.fetchall()]
  return tables
