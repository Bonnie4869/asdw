from .db import get_connection
from .PersistentRecord import PersistentRecord

class RecordMapper:
    """Handles SQL operations for Record entities."""
    def save(self, record_entity) -> None:
        p_record = PersistentRecord(
            record_id=record_entity.get_record_id(),
            student_id=record_entity.get_student_id(),
            problem=record_entity.get_problem_statement(),
            summary=record_entity.get_interview_summary(),
            action=record_entity.get_follow_up_action(),
            date=str(record_entity.get_interview_date())
        )
        
        conn = get_connection()
        try:
            conn.execute('''
                INSERT INTO record (record_id, student_id, problem_statement, interview_summary, follow_up_action, interview_date)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(record_id) DO UPDATE SET 
                student_id=excluded.student_id,
                problem_statement=excluded.problem_statement,
                interview_summary=excluded.interview_summary,
                follow_up_action=excluded.follow_up_action,
                updated_at=datetime('now', 'localtime')
            ''', (p_record.record_id, p_record.student_id, p_record.problem, 
                  p_record.summary, p_record.action, p_record.date))
            conn.commit()
        finally:
            conn.close()

    def delete(self, record_id: str) -> None:
        conn = get_connection()
        try:
            conn.execute('DELETE FROM record WHERE record_id = ?', (record_id,))
            conn.commit()
        finally:
            conn.close()