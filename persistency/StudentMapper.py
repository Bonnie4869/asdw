from .db import get_connection
from .PersistentStudent import PersistentStudent

class StudentMapper:
    """Handles SQL operations for Student entities."""
    def save(self, student_entity) -> None:
        p_student = PersistentStudent(
            student_id=student_entity.get_student_id(),
            status=student_entity.get_status()
        )
        
        conn = get_connection()
        try:
            conn.execute('''
                INSERT INTO student (student_id, status)
                VALUES (?, ?)
                ON CONFLICT(student_id) DO UPDATE SET 
                status=excluded.status, 
                updated_at=datetime('now', 'localtime')
            ''', (p_student.student_id, p_student.status))
            conn.commit()
        finally:
            conn.close()