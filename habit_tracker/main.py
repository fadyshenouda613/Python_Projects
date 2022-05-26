import requests
from datetime import datetime


pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "fady.shenouda.fady.shenouda"
USERNAME = "fadyshenouda01"
GRAPH_ID = "graphfady1"
# parameters = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# # graph_config = {
# #     "id": "graphfady1",
# #     "name": "Coding Graph",
# #     "unit": "Days",
# #     "type": "int",
# #     "color": "ajisai"
# # }
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}
response = requests.post(url=pixel_creation_endpoint, headers=headers, json=pixel_data)
print(response.text)
