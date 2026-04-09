"""
Shared configuration for the Content Creation Studio agents.
Centralizes model name and quality thresholds.
"""

import os

MODEL_NAME = "gemini-2.5-flash"

QUALITY_SCORE_THRESHOLD = int(os.getenv("QUALITY_SCORE_THRESHOLD", "70"))
MAX_IMPROVEMENT_ITERATIONS = int(os.getenv("MAX_IMPROVEMENT_ITERATIONS", "2"))
