from flask import Flask, render_template
from samlib import metadata, data, jsonhelpers

import MySQLdb, json
import pw

db = MySQLdb.connect(host=pw.db_host,
                     user=pw.db_user,
                   passwd=pw.db_pass,
                       db=pw.db_name)


app = Flask(__name__)
app.debug = True

# thanks stack overflow
from werkzeug.debug import DebuggedApplication
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

# index page that lists the avaliable tables
@app.route('/')
def route_index():
  tables = metadata.tables(db)
  return render_template("tables.html", tables=tables)

# graphing page for this table
@app.route('/graph/<t>')
def route_table(t):
  cols = metadata.columns(db, t)
  return render_template("graph.html", table=t, cols=cols)

# returns data from that table as json
@app.route('/data/<t>')
def route_data(t):
  return json.dumps(data.alldata(db, t),
		    default=jsonhelpers.dated_default)

app.run()
