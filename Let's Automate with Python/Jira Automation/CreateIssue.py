import requests
import json

url = "https://aaditlearnjira.atlassian.net/rest/api/2/issue"
headers = {
    "Accept": "application/json",
    "Content-type": "application/json"
}
payload = json.dumps(
    {
        "fields":
            {
                "project":
                    {
                        "key": "PA"
                    },
                "summary": "Hey This Test",
                "description": "This is sample desc",
                "issuetype": {
                    "name": "Bug"
                }
            }
    }
)
response = requests.post(url, headers, data=payload, auth=("aadit.jain@tcs.com",
                                                           "ATATT3xFfGF0jeXKzyZvGxvaHcV7ZtVqRYIXU7gvr5RKcIn0DUMX8jjzNXe6TKcclXBFg17Ru9FRFjK9rGnir-ObXX-cJ9GlBb6dcVkllrB-4JuKrHpJEoj2OOwl56wMjL-UEyOltZSj1FRefh3XU4YxD1Xl8AQwZV_FKs5HgBCEGisQr4OxM7M=545DF2DF"))
print(response.json())
