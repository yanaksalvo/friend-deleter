import discord
import requests

token = input("Token: ")

user_token = token

headers = {
    "Authorization": user_token
}

response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)

for friend in response.json():
    friend_name = friend['user']['username']
    response = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friend['id']}", headers=headers)
    print(f"Deleted Friend : {friend_name}")

response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)
print(f"Friends : {len(response.json())}")