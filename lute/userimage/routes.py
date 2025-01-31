"""
User images routes.

User images are stored in the database as /userimages/langid/term, but
with no jpeg extension.  Reason: the old symfony code couldn't manage
urls with periods.
"""

import os
from flask import Blueprint, send_from_directory, current_app

bp = Blueprint("userimages", __name__, url_prefix="/userimages")


@bp.route("/<int:lgid>/<path:f>", methods=["GET"])
def get_image(lgid, f):
    "Serve the image from the data/userimages directory."
    datapath = current_app.config["DATAPATH"]
    directory = os.path.join(datapath, "userimages", str(lgid))
    return send_from_directory(directory, f)
