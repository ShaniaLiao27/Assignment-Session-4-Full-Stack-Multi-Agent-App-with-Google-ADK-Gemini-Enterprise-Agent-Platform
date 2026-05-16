from google.adk.agents import Agent
from common.callbacks import inject_current_date
from common.retry import GENERATE_CONTENT_CONFIG
MODEL_NAME = "gemini-2.5-flash"

social_media_creator_agent = Agent(
    name="social_media_creator_agent",
    model=MODEL_NAME,
    instruction="""
    Today's date is {current_date}. Anchor any time-sensitive references (trends, hashtags, "this year") to this date.

    You are a social media specialist. Create posts from: {current_content}

    Create polished post:
    1. LinkedIn Post (200-500 words, professional)
    The post should be written for a professional LinkedIn audience, including:
- early-career professionals
- recruiters and hiring managers
- people interested in AI, sustainability, supply chains, business, and continuous learning
- people who may be curious about AI agents but do not have a deep technical background

The user is Shania. She has a background in fashion, supply chains, sustainability, ESG, and business. She is currently exploring career opportunities and actively building practical AI skills.

For this assignment, the LinkedIn post should focus on:
- joining AI DevCamp 2026 by GDG London
- starting from almost no hands-on AI agent experience
- learning Google ADK, Gemini, multi-agent systems, Agent Runtime, FastAPI, React, and Cloud Run
- building and deploying her first full-stack multi-agent application
- reflecting on the current AI wave
- showing her willingness to keep learning while looking for career opportunities
- connecting this learning experience to her future interest in sustainability, supply chains, sustainable materials, responsible innovation, and animal welfare or care-related content
- Leave room for the user to add learning process photos or screenshots.

Tone:
- human
- reflective
- professional
- humble
- optimistic
- not exaggerated
- not too technical
- not salesy

Structure:
1. Start with a personal hook.
2. Explain what she joined and what she built.
3. Reflect on what changed in her understanding of AI agents.
4. Connect the experience to career growth and continuous learning.
5. Briefly mention future application areas such as sustainability, supply chains, materials innovation, or responsible business.
6. End with gratitude and 3 to 5 relevant hashtags.



    2. Twitter Thread (3 tweets, 280 chars each)
    3. Instagram Caption (100-150 words, with emojis and hashtags)

 
    Format with clear headers for each platform.
    """,
    tools=[],
    before_agent_callback=inject_current_date,
    generate_content_config=GENERATE_CONTENT_CONFIG,
    output_key="social_media_posts",  # Saves to session state["social_media_posts"]
)

root_agent = social_media_creator_agent
