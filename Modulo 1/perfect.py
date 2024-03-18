# -*- coding: utf-8 -*-

import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']

API_SERVICE_NAME = 'youtubeAnalytics'
API_VERSION = 'v2'
CLIENT_SECRETS_FILE = 'C:\\Users\\siete\\OneDrive\\Escritorio\\client_secret_1096159937422-rvafv3i6nmlvh5584stdof11kh7s3eh6.apps.googleusercontent.com.json'
def get_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def execute_api_request(client_library_function, **kwargs):
  response = client_library_function(
    **kwargs
  ).execute()

  print(response)

if __name__ == '__main__':
  # Disable OAuthlib's HTTPs verification when running locally.
  # *DO NOT* leave this option enabled when running in production.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

  youtubeAnalytics = get_service()
  execute_api_request(
      youtubeAnalytics.reports().query,
      ids='channel==MINE',
      startDate='2017-01-01',
      endDate='2017-12-31',
      metrics='estimatedMinutesWatched,views,likes,subscribersGained',
      dimensions='day',
      sort='day'
  )

  data = {
    'kind': 'youtubeAnalytics#resultTable',
    'columnHeaders': [
        {'name': 'day', 'columnType': 'DIMENSION', 'dataType': 'STRING'},
        {'name': 'estimatedMinutesWatched', 'columnType': 'METRIC', 'dataType': 'INTEGER'},
        {'name': 'views', 'columnType': 'METRIC', 'dataType': 'INTEGER'},
        {'name': 'likes', 'columnType': 'METRIC', 'dataType': 'INTEGER'},
        {'name': 'subscribersGained', 'columnType': 'METRIC', 'dataType': 'INTEGER'}
    ],
    'rows': [
        ['2017-01-01', 0, 0, 0, 0],
        ['2017-01-02', 0, 0, 0, 0],
        ['2017-01-03', 0, 0, 0, 0],
        ['2017-01-04', 0, 0, 0, 0],
        # Many more rows...
        ['2017-12-30', 0, 0, 0, 0],
        ['2017-12-31', 0, 0, 0, 0]
    ]
}

# Para acceder a los datos:
for row in data['rows']:
    day = row[0]
    estimated_minutes_watched = row[1]
    views = row[2]
    likes = row[3]
    subscribers_gained = row[4]
    print(f"Day: {day}, Estimated Minutes Watched: {estimated_minutes_watched}, Views: {views}, Likes: {likes}, Subscribers Gained: {subscribers_gained}")

  #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 Secreto de cliente
  #1096159937422-rvafv3i6nmlvh5584stdof11kh7s3eh6.apps.googleusercontent.com id