from flask import Flask, render_template, redirect
from samlib import metadata, data, jsonhelpers, graph

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

@app.route('/graph/<t>/<x>/<y>')
def route_graph(t, x, y):
  return redirect(graph.graph(data.col(db,t,y),data.col(db,t,x)))

# returns data from that table as json
@app.route('/data/<t>')
def route_data(t):
  return json.dumps(data.alldata(db, t),
		    default=jsonhelpers.dated_default)

