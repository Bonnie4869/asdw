class PersistentLog:
    """DTO representing a row in the 'log_activity' database table."""
    def __init__(self, log_id: int, time: str, data: str, func: str, student_id: str):
        self.log_id = log_id
        self.time = time
        self.data = data
        self.function_access = func
        self.student_id = student_id