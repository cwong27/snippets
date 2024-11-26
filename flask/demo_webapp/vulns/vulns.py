import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

bp = Blueprint("vulns", __name__, url_prefix="/vulns")

@bp.route("/xss", methods=("GET", "POST"))
def xss():
    text = request.args.get('text')
    return render_template("vulns/xss.html", text=text)