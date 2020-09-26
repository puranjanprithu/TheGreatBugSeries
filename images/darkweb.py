

#Download the main page of the c0c0n website :

import requests

#create session
session=requests.session()

#Define the url
CurrentURL="https://india.c0c0n.org/2020/"

#"https://www.propub3r6espa33w.onion/"
#Make the request
try:
    page=session.get(CurrentURL)
    print("[i] Webpage downloaded")
except session.exceptions.HTTPError as err:
    raise SystemExit(err)

#display the page
print(page.text)