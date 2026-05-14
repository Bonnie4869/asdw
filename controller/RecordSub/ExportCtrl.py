# =========================================================
# app/controller/export_ctrl.py
# =========================================================

from flask import Blueprint
from flask import request
from flask import send_file

from app.models.RecordSub.WordFile import WordFile

from app.persistency.PersistentRecord import PersistentRecord

export_bp = Blueprint("export", __name__)


class ExportCtrl:

    # =====================================================
    # Export Student Records
    # =====================================================

    @staticmethod
    @export_bp.route("/export_student_records", methods=["GET"])
    def export_student_records():

        student_id = request.args.get("student_id")

        persistent_record = PersistentRecord()

        records = persistent_record.find_all_by_student_id(student_id)

        word_file = WordFile("student_records.docx", "exports/")

        for record in records:

            word_file.add_record(record)

        word_file.export()

        return {"message": "Export successful"}

    # =====================================================
    # Export By Academic Year
    # =====================================================

    @staticmethod
    @export_bp.route("/export_by_year", methods=["GET"])
    def export_by_year():

        academic_year = request.args.get("academic_year")

        persistent_record = PersistentRecord()

        records = persistent_record.find_by_academic_year(academic_year)

        word_file = WordFile(f"{academic_year}_records.docx", "exports/")

        for record in records:

            word_file.add_record(record)

        word_file.export()

        return {"message": "Year export successful"}

    # =====================================================
    # Export By Mentor
    # =====================================================

    @staticmethod
    @export_bp.route("/export_by_mentor", methods=["GET"])
    def export_by_mentor():

        mentor_name = request.args.get("mentor_name")

        persistent_record = PersistentRecord()

        records = persistent_record.find_by_mentor_name(mentor_name)

        word_file = WordFile(f"{mentor_name}_records.docx", "exports/")

        for record in records:

            word_file.add_record(record)

        word_file.export()

        return {"message": "Mentor export successful"}
