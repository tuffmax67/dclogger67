import requests
from config import DISCORD_WEBHOOK


def send_notification(message):
    if not DISCORD_WEBHOOK:
        print("Discord webhook not configured.")
        return

    try:
        response = requests.post(
            DISCORD_WEBHOOK,
            json={"content": message},
            timeout=10
        )
        response.raise_for_status()

    except requests.RequestException as error:
        print("Notification failed:", error)
