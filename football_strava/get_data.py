from stravaio import Athlete, StravaIO, Streams, strava_oauth2

from football_strava import SETTINGS


resp = strava_oauth2(
    client_id=SETTINGS.strava_client_id, client_secret=SETTINGS.strava_client_secret
)
STRAVA_ACCESS_TOKEN = resp["access_token"]


client = StravaIO(access_token=STRAVA_ACCESS_TOKEN)

athlete: Athlete = client.get_logged_in_athlete()
streams: Streams = client.get_activity_streams(4093691464, athlete_id=athlete.id)

# Store streams locally (~/.stravadata/streams_<athlete_id>/streams_<id>.parquet)
# as a .parquet file, that can be loaded later using gpd.read_parquet()
streams.store_locally()
