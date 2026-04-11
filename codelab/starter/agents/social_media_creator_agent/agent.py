from google.adk.agents import Agent
MODEL_NAME = "gemini-2.5-flash"

social_media_creator_agent = Agent(
    name="social_media_creator_agent",
    model=MODEL_NAME,
    instruction="""
    You are a social media specialist. Create posts from: {{current_content}}

    Create:
    1. LinkedIn Post (150-200 words, professional)
    2. Twitter Thread (3 tweets, 280 chars each)
    3. Instagram Caption (100-150 words, with emojis and hashtags)

    Format with clear headers for each platform.
    """,
    tools=[],
    output_key="social_media_posts",  # Saves to session state["social_media_posts"]
)

root_agent = social_media_creator_agent
