import json
import re


# This method will be used by the mock to replace requests.get
def mock_request(*args, **kwargs):
    class MockResponse:
        def __init__(
            self, text, headers={"content-type": "application/json"}, status_code=200
        ) -> None:
            self.text = text
            self.headers = headers
            self.status_code = status_code

        def json(self) -> str:
            return self.text

    base_url = f"https://discord.com/api/v10"
    text = None

    if re.match(rf"{base_url}/channels/\d+/messages", args[0]):
        with open("tests/responses/new_message.json", "r") as file:
            text = json.load(file)
        return MockResponse(text)
    if re.match(rf"{base_url}/channels/\d+", args[0]):
        with open("tests/responses/get_channel.json", "r") as file:
            text = json.load(file)
        return MockResponse(text)

    return MockResponse("", headers={}, status_code=404)
