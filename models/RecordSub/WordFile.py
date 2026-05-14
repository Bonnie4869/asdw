from __future__ import annotations
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from .Record import Record

class WordFile:
    """
    Helper Entity: Word document to be exported.
    
    Attributes:
        _file_name (str)        : output file name
        _file_path (str)        : output directory
        _records (List[Record]) : records to export
    """
    def __init__(self, file_name: str = "", file_path: str = ""):
        self._file_name = file_name
        self._file_path = file_path
        self._records: List[Record] = []

    # --- Bidirectional methods for Record ---
    def add_record(self, record: Record) -> None:
        """Add a record and notify the record to point to this WordFile."""
        if record not in self._records:
            self._records.append(record)
            record.set_word_file(self)

    def remove_record(self, record: Record) -> None:
        """Remove a record and sever its connection to this WordFile."""
        if record in self._records:
            self._records.remove(record)
            record.set_word_file(None)

    def get_file_name(self) -> str:
        return self._file_name

    def set_file_name(self, name: str) -> None:
        self._file_name = name

    def get_file_path(self) -> str:
        return self._file_path

    def set_file_path(self, path: str) -> None:
        self._file_path = path

    def get_records(self) -> List[Record]:
        return self._records.copy()

    def append_record(self, record: Record) -> None:
        """Legacy support: Redirects to the bidirectional method."""
        self.add_record(record)

    def clear_records(self) -> None:
        """Disconnect all records properly to prevent memory leaks."""
        for record in list(self._records):
            self.remove_record(record)

    def export(self) -> None:
        """Mock generation of the Word file."""
        print(f"[WordFile] Exporting {len(self._records)} records to "
              f"{self._file_path}/{self._file_name}")

    def export_to(self, path: str) -> None:
        """Export to a specific full path."""
        print(f"[WordFile] Exporting {len(self._records)} records to {path}")

    def __repr__(self) -> str:
        return f"WordFile(name={self._file_name}, records={len(self._records)})"