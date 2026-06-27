import requests

URL = "https://www.legifrance.gouv.fr/codes/id/LEGITEXT000006071191/"

def get_code_html():
    r = requests.get(URL)
    r.raise_for_status()
    return r.text
