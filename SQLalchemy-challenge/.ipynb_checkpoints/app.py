import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



# Base = automap_base()
# Base.prepare(engine, reflect=True)

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes"""
    return f"Available Routes:<br/>" f"/api/v1.0/precipitation" f"/api/v1.0/stations"f"/api/v1.0/tobs" f"/api/v1.0/<start>" f"/api/v1.0/<start>/<end>"

#@app.route("/api/v1.0/precipitation")
