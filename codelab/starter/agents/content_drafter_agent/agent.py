from google.adk.agents import Agent
MODEL_NAME = "gemini-2.5-flash"

content_drafter_agent = Agent(
    name="content_drafter_agent",
    model=MODEL_NAME,
    instruction="""
    You are a content writer. Write a blog post: {{blog_topic}}

    Create a draft (400-600 words) with:
    - Engaging introduction
    - At least 2 H2 headings
    - A conclusion section

    Output only the blog post in markdown format.
    """,
    tools=[],
    output_key="current_content",  # Saves to session state["current_content"]
)

root_agent = content_drafter_agent
