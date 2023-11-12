import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import requests

url = "https://slack.com/api/conversations.list"
headers = {
    "Authorization": "Bearer xoxb-6052895306385-6180531818643-3oiecwRxrFioYdjEQ8lnfdxa",
}

response = requests.get(url, headers=headers)

# Check the status code of the response
if response.status_code == 200:
    # The request was successful
    data = response.json()
    # Do something with the data
    print(data)
else:
    # There was an error with the request
    print(f"Error: {response.status_code} - {response.text}")



# # WebClient instantiates a client that can call API methods
# # When using Bolt, you can use either `app.client` or the `client` passed to listeners.
# client = WebClient(token=os.environ.get("SLACK_USR_TOKEN"))
# logger = logging.getLogger(__name__)

# channel_name = "general"
# conversation_id = 1
# print("hello")

# x = requests.get('https://slack.com/api/conversations.list')

# print(x.text)

# try:
#     # Call the conversations.list method using the WebClient
#     for result in client.conversations_list():
#         if conversation_id is not None:
#             break
#         for channel in result["channels"]:
#             if channel["name"] == channel_name:
#                 conversation_id = channel["id"]
#                 #Print result
#                 print(f"Found conversation ID: {conversation_id}")
#                 break

# except SlackApiError as e:
#     print(f"Error: {e}")



