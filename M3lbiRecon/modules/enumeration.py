from urllib.parse import urlparse
import urllib.request as request;
import urllib.error as error

opener = request.build_opener()

def __dir(urlBase):
    urlPs = urlparse(urlBase)
    scheme = urlPs.scheme
    hostname = urlPs.hostname
    path = urlPs.path
    newPath = path + '/' if path[-1] != "/" else path

    with open("./wordlists/directory.txt", "r") as wordlist:
        if not wordlist:
            return
        for word in wordlist.readlines():
            url = f"{scheme}://{hostname}{newPath}{word.rstrip("\n")}"
            try:
                response = opener.open(url, timeout=10)
                status = response.getcode()
                print(url, "->", status)
            except error.HTTPError as e:
                print(url, "->", e.code)
            except error.URLError as e:
                print(url, "-> URLError:", e.reason)

def __sub(urlBase):
    urlPs = urlparse(urlBase)
    scheme = urlPs.scheme
    hostname = urlPs.hostname

    parts = hostname.split(".")
    if len(parts) == 2:
        objUrl = {
            "subdomain": "",
            "domain": parts[-2],
            "tld": parts[-1]
        }        
    else:
        objUrl = {
            "subdomain": ".".join(parts[:-2]),
            "domain": parts[-2],
            "tld": parts[-1]
        }

    with open("./wordlists/subdomain.txt", "r") as wordlist:
        if not wordlist:
            return
        for word in wordlist.readlines():
            url = f"{scheme}://{word.rstrip('\n')}.{objUrl['domain']}.{objUrl["tld"]}"
            try:
                response = opener.open(url, timeout=10)
                status = response.getcode()
                print(url, "->", status)
            except error.HTTPError as e:
                print(url, "->", e.code)
            except error.URLError as e:
                print(url, "-> URLError:", e.reason)

def __all(urlBase):
    __dir(urlBase)
    __sub(urlBase)