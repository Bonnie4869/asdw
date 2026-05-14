class PersistentStudent:
    """DTO representing a row in the 'student' database table."""
    def __init__(self, student_id: str, status: str):
        self.student_id = student_id
        self.status = status