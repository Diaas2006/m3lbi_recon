import re

def validUrl(url: str) -> bool:
    try: 
        regex = re.compile('^https?://(?:[A-Za-z0-9-]+.)+[A-Za-z]{2,}(?:.*)?$')
        return regex.fullmatch(url)
    except ValueError:
        return False