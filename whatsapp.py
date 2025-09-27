
# whatsapp.py
from agents import function_tool
import requests
import os

@function_tool
def send_whatsapp_message(number: str, message: str) -> str:
    instance_id = os.getenv("ULTRA_INSTANCE_ID")
    token = os.getenv("ULTRA_TOKEN")

    if not instance_id or not token:
        return "UltraMSG credentials not configured."

    url = f"https://api.ultramsg.com/{instance_id}/messages/chat"
    payload = {"token": token, "to": number, "body": message}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return f"Message sent to {number}"
        else:
            return f"Failed to send message: {response.text}"
    except Exception as e:
        return f"Error sending message: {e}"
