from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from .Record import Record
    from .LogActivity import LogActivity

class Student:
    """
    Entity: Student information.
    
    Attributes:
        _student_id (str) : unique identifier
        _status (str)     : normal, suspended, probation
        _records (list)   : associated interview records (1-to-many bidirectional)
        _log_activities (list): associated log activities (1-to-many bidirectional)
    """
    def __init__(self, student_id: str, status: str = "normal"):
        self._student_id = student_id
        self._status = status
        
        # Collections to maintain the 1-to-many relationships
        self._records: List['Record'] = []
        self._log_activities: List['LogActivity'] = []

    def get_student_id(self) -> str:
        return self._student_id

    def get_status(self) -> str:
        return self._status

    def set_status(self, status: str) -> None:
        """Update student status (normal/suspended/probation)."""
        self._status = status

    # --- Bidirectional methods for Record ---
    def add_record(self, record: 'Record') -> None:
        """Add a record and trigger reverse synchronization to maintain consistency."""
        if record not in self._records:
            self._records.append(record)
            record.set_student(self)  

    def remove_record(self, record: 'Record') -> None:
        """Remove a record and sever the reverse connection."""
        if record in self._records:
            self._records.remove(record)
            record.set_student(None)  

    # --- Bidirectional methods for LogActivity ---
    def add_log_activity(self, log: 'LogActivity') -> None:
        """Add a log activity and trigger reverse synchronization."""
        if log not in self._log_activities:
            self._log_activities.append(log)
            log.set_student(self)

    def remove_log_activity(self, log: 'LogActivity') -> None:
        """Remove a log activity and sever the reverse connection."""
        if log in self._log_activities:
            self._log_activities.remove(log)
            log.set_student(None)

    def __repr__(self) -> str:
        return f"Student(id={self._student_id}, status={self._status})"
