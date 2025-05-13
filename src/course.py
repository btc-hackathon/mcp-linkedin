import json
from pathlib import Path
from typing import List

from pydantic import BaseModel


class LinkedInCourse(BaseModel):
    """
    Model representing a LinkedIn course.
    """

    display_name: str = "Unassigned"
    link: str | None = None


# Function to load JSON and create instances
def load_linkedin_courses() -> List[LinkedInCourse]:
    """
    Load LinkedIn course instances from a JSON file located in the same directory
    as this Python file.
    """
    current_dir = Path(__file__).parent
    json_file = current_dir / "linkedin_courses.json"

    with json_file.open("r", encoding="utf-8") as f:
        data = json.load(f)

    courses = []
    for display_name, link in data.items():
        courses.append(LinkedInCourse(display_name=display_name, link=link))

    return courses
