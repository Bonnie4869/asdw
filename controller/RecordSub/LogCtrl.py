# =========================================================
# app/controller/log_ctrl.py
# =========================================================

from flask import Blueprint
from flask import render_template
from flask import request

from app.persistency.PersistentLog import PersistentLog

log_bp = Blueprint("log", __name__)


class LogCtrl:

    # =====================================================
    # View All Logs
    # =====================================================

    @staticmethod
    @log_bp.route("/view_logs", methods=["GET"])
    def view_logs():

        persistent_log = PersistentLog()

        logs = persistent_log.find_all()

        return render_template("record/view_logs.html", logs=logs)

    # =====================================================
    # Search Logs By Student ID
    # =====================================================

    @staticmethod
    @log_bp.route("/search_logs", methods=["GET"])
    def search_logs():

        student_id = request.args.get("student_id")

        persistent_log = PersistentLog()

        logs = persistent_log.find_by_student_id(student_id)

        return render_template("record/view_logs.html", logs=logs)

    # =====================================================
    # Filter Logs By Function
    # =====================================================

    @staticmethod
    @log_bp.route("/filter_logs", methods=["GET"])
    def filter_logs():

        used_function = request.args.get("used_function")

        persistent_log = PersistentLog()

        logs = persistent_log.find_by_function(used_function)

        return render_template("record/view_logs.html", logs=logs)
