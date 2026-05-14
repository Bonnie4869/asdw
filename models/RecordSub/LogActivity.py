from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .Student import Student


class LogActivity:
    """
    Entity: System log entry.

    Attributes:
        _log_id (int)            : unique identifier
        _time (datetime)         : timestamp
        _data (str)              : contextual data (e.g., user ID)
        _function_access (str)   : function accessed
        _student (Student)       : associated student
    """

    def __init__(self, log_id: int, time: datetime, data: str, function_access: str):
        self._log_id = log_id
        self._time = time
        self._data = data
        self._function_access = function_access

        # Reference to the Student entity
        self._student = None

    # --- Bidirectional setter for Student ---
    def set_student(self, new_student: Optional[Student]) -> None:
        """Maintain bidirectional association, preventing infinite loops."""
        if self._student != new_student:
            old_student = self._student
            self._student = new_student

            if new_student is not None:
                new_student.add_log_activity(self)
            if old_student is not None:
                old_student.remove_log_activity(self)

    def get_log_id(self) -> int:
        return self._log_id

    def get_time(self) -> datetime:
        return self._time

    def get_data(self) -> str:
        return self._data

    def get_function_access(self) -> str:
        return self._function_access

    def set_time(self, time: datetime) -> None:
        self._time = time

    def set_data(self, data: str) -> None:
        self._data = data

    def set_function_access(self, function_access: str) -> None:
        self._function_access = function_access

    def add_function(self, function_name: str) -> None:
        """Append another function name to the access list."""
        if self._function_access:
            self._function_access += f", {function_name}"
        else:
            self._function_access = function_name

    @staticmethod
    def create_log(data: str, func: str) -> "LogActivity":
        """Factory: create log with current timestamp and auto-generated ID."""
        log_id = abs(hash(datetime.now())) % 10**6
        return LogActivity(log_id, datetime.now(), data, func)

    def view_log_info(self) -> List[str]:
        """Return formatted log lines for display."""
        return [
            f"Log ID: {self._log_id}",
            f"Time: {self._time}",
            f"Data: {self._data}",
            f"Functions Accessed: {self._function_access}",
        ]

    def __repr__(self) -> str:
        return f"LogActivity(id={self._log_id}, time={self._time})"
