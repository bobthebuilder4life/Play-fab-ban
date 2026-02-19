import requests

PLAYFAB_TITLE_ID = "title_id"
PLAYFAB_SECRET_KEY = "secret_key"

def ban_player(playfab_id="user_id", reason="reason", duration_hours=amount):
    url = f"https://title_id.playfabapi.com/Admin/BanUsers"

    headers = {
        "X-SecretKey": PLAYFAB_SECRET_KEY,
        "Content-Type": "application/json"
    }

    ban_entry = {
        "PlayFabId": playfab_id,
        "Reason": reason #do not change this
    }
    #replace "title_id", "secret_key", "user_id" and "reason" with their things
    #if you want to perm ban then remove ', duration_hours=178'
    #change 'amount' in duration_hours= with your desired amount
