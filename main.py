import requests
from bs4 import BeautifulSoup

username = input() 
url = f"https://github.com/{username}"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
img_tag = soup.select_one('img.avatar-user')
img_url = img_tag['src']
print(f"프로필 이미지 URL: {img_url}")
img_data = requests.get(img_url).content
name_tag = soup.select_one('span.p-name')
name = name_tag.text.strip()
followers_tag = soup.select_one('a[href$="?tab=followers"] > span')
followers = followers_tag.text.strip()
repo_tag = soup.select_one('a[href$="?tab=repositories"] > span')
repos = repo_tag.text.strip()

print(f"사용자: {name}")
print(f"팔로워 수: {followers}")
print(f"저장소 수: {repos}")
with open(f"{username}_github_profile.jpg", "wb") as f:
    f.write(img_data)
print(f"{username}_github_profile.jpg")
