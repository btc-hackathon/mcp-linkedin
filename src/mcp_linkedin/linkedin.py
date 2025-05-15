import json
from fastmcp import FastMCP
from .course import load_linkedin_courses

mcp = FastMCP(name="LinkedIn MCP Service",
              description="Provides tools for interacting with LinkedIn.",
              )


@mcp.tool()
async def get_all_linkedin_courses() -> str:
    """
    Retrieve all LinkedIn courses.

    Returns:
        JSON string representing the LinkedIn courses, or an error object if not found.
    """
    linkedin_courses = load_linkedin_courses()
    courses_list = [
        {"display_name": course.display_name, "link": course.link}
        for course in linkedin_courses
    ]
    response_data = {"success": True, "linkedin_courses": courses_list}

    return json.dumps(response_data, indent=2, ensure_ascii=False)
