from __future__ import annotations
from typing import Dict, Any, Optional, TYPE_CHECKING
from datetime import datetime
if TYPE_CHECKING:
    from .Student import Student
    from .WordFile import WordFile

class Record:
    """
    Entity: Interview record.
    
    Attributes:
        _record_id (str)          : unique identifier
        _student (Student)        : associated student (bidirectional)
        _word_file (WordFile)     : associated word file for export (bidirectional)
        _problem_statement (str)  : problem described
        _interview_summary (str)  : summary of interview
        _follow_up_action (str)   : follow-up plan
        _interview_date (datetime): when interview occurred
    """
    def __init__(self, record_id: str, student: 'Student',
                 problem_statement: str, interview_summary: str,
                 follow_up_action: str, interview_date: datetime = None):
        self._record_id = record_id
        
        # Initialize references as None, then establish relations via setters
        self._student = None
        self._word_file = None
        self.set_student(student)
        
        self._problem_statement = problem_statement
        self._interview_summary = interview_summary
        self._follow_up_action = follow_up_action
        self._interview_date = interview_date or datetime.now()

    # --- Bidirectional setter for Student ---
    def set_student(self, new_student: 'Student') -> None:
        """
        Maintain bidirectional association. 
        """
        if self._student != new_student:
            old_student = self._student
            self._student = new_student
            
            if old_student is not None:
                old_student.remove_record(self)
            if new_student is not None:
                new_student.add_record(self)

    # --- Bidirectional setter for WordFile ---
    def set_word_file(self, new_word_file: Optional['WordFile']) -> None:
        """Maintain bidirectional association with WordFile without infinite loop."""
        if self._word_file != new_word_file:
            old_word_file = self._word_file
            self._word_file = new_word_file
            
            if new_word_file is not None:
                new_word_file.add_record(self)
            if old_word_file is not None:
                old_word_file.remove_record(self)

    # Getters
    def get_record_id(self) -> str:
        return self._record_id

    def get_student(self) -> 'Student':
        return self._student

    def get_student_id(self) -> str:
        return self._student.get_student_id() if self._student else None

    def get_problem_statement(self) -> str:
        return self._problem_statement

    def get_interview_summary(self) -> str:
        return self._interview_summary

    def get_follow_up_action(self) -> str:
        return self._follow_up_action

    def get_interview_date(self) -> datetime:
        return self._interview_date

    # Business method
    def update(self, problem_statement: str, interview_summary: str,
               follow_up_action: str) -> None:
        """Update the record's content (used by Mentor)."""
        self._problem_statement = problem_statement
        self._interview_summary = interview_summary
        self._follow_up_action = follow_up_action

    def get_record_details(self) -> Dict[str, Any]:
        """Return all record data as a dictionary."""
        return {
            "record_id": self._record_id,
            "student_id": self.get_student_id(),
            "student": self._student,
            "problem_statement": self._problem_statement,
            "interview_summary": self._interview_summary,
            "follow_up_action": self._follow_up_action,
            "interview_date": self._interview_date
        }

    def __repr__(self) -> str:
        return f"Record(id={self._record_id}, student={self.get_student_id()})"
