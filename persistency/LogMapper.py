from .db import get_connection
from .PersistentLog import PersistentLog

class LogMapper:
    """Handles SQL operations for LogActivity entities."""
    def save(self, log_entity) -> None:
        student_id = log_entity._student.get_student_id() if log_entity._student else None
        p_log = PersistentLog(
            log_id=log_entity.get_log_id(),
            time=str(log_entity.get_time()),
            data=log_entity.get_data(),
            func=log_entity.get_function_access(),
            student_id=student_id
        )
        
        conn = get_connection()
        try:
            conn.execute('''
                INSERT INTO log_activity (log_id, time, data, function_access, student_id)
                VALUES (?, ?, ?, ?, ?)
            ''', (p_log.log_id, p_log.time, p_log.data, p_log.function_access, p_log.student_id))
            conn.commit()
        finally:
            conn.close()