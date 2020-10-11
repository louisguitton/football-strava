import logging

from football_strava.config import generate_settings


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("football_strava")

SETTINGS = generate_settings()
