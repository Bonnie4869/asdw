from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

from app.models.RecordSub.Record import Record

from app.persistency.PersistentRecord import PersistentRecord

record_bp = Blueprint("record", __name__)


class RecordCtrl:

    # =====================================================
    # Search Student Record
    # =====================================================

    @staticmethod
    @record_bp.route("/search_student", methods=["GET"])
    def search_student():

        student_id = request.args.get("student_id")

        persistent_record = PersistentRecord()

        record = persistent_record.find_by_student_id(student_id)

        return render_template("record/search_record.html", record=record)

    # =====================================================
    # Add Record
    # =====================================================

    @staticmethod
    @record_bp.route("/add_record", methods=["POST"])
    def add_record():

        form = request.form

        record = Record(
            None,
            form["student_id"],
            form["mentor_id"],
            form["datetime"],
            form["problem_statement"],
            form["interview_summary"],
            form["follow_up_actions"],
        )

        persistent_record = PersistentRecord()

        persistent_record.save(record)

        return redirect(url_for("record.search_student", student_id=form["student_id"]))

    # =====================================================
    # Update Record
    # =====================================================

    @staticmethod
    @record_bp.route("/update_record/<int:record_id>", methods=["POST"])
    def update_record(record_id):

        form = request.form

        updated_record = Record(
            record_id,
            form["student_id"],
            form["mentor_id"],
            form["datetime"],
            form["problem_statement"],
            form["interview_summary"],
            form["follow_up_actions"],
        )

        persistent_record = PersistentRecord()

        persistent_record.update(updated_record)

        return {"message": "Record updated successfully"}

    # =====================================================
    # Delete Record
    # =====================================================

    @staticmethod
    @record_bp.route("/delete_record/<int:record_id>", methods=["POST"])
    def delete_record(record_id):

        persistent_record = PersistentRecord()

        persistent_record.delete(record_id)

        return {"message": "Record deleted successfully"}

    # =====================================================
    # View All Records
    # =====================================================

    @staticmethod
    @record_bp.route("/view_records", methods=["GET"])
    def view_records():

        persistent_record = PersistentRecord()

        records = persistent_record.find_all()

        return render_template("record/view_records.html", records=records)
