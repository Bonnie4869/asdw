class PersistentRecord:
    """DTO representing a row in the 'record' database table."""
    def __init__(self, record_id: str, student_id: str, problem: str, summary: str, action: str, date: str):
        self.record_id = record_id
        self.student_id = student_id  # Foreign Key reference
        self.problem = problem
        self.summary = summary
        self.action = action
        self.date = date