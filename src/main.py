import urllib.request, json
import requests
import requests.auth

class AppURLopener(urllib.request.FancyURLopener):
    version = "App/1.7"

urllib.request._urlopener = AppURLopener()
def authenticate():
    pass


client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
post_data = {"grant_type": "password", "username": username, "password": password}
headers = {"User-Agent": "discord_reddit/0.1 by " + username}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
print(response.json())

h = {"Authorization": "bearer " + response.json()['access_token'], "User-Agent": "discord_reddit/0.1 by " + username}

def main():
    url = "https://oauth.reddit.com/r/funny/comments/8tzuqk/i_told_my_son_if_he_let_me_shoot_his_tooth_out_id/.json"
    response = requests.get(url, headers = h)
    video_url = response.json()[0]['data']['children'][0]['data']['media']['reddit_video']['fallback_url']
    print(video_url)

if __name__ == '__main__':
    main()