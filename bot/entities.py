from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    login: str
    issue_year: str
    current_location: Optional[str]
    company: Optional[str]
    position: Optional[str]
    ref_possibilities: Optional[str]
    hobbies: Optional[str]

    def __str__(self):
        return f"{self.login} {self.issue_year} {self.current_location}"
