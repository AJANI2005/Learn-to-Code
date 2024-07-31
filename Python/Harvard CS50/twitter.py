import re

url = input("URL: ").strip()
matches = re.search(r"^(?:https?://)?(?:www\.)?twitter.com/(\w+)$",url,re.IGNORECASE)
if(matches):
    print("Username:" + matches.group(1))