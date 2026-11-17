
import requests


#cw1
def pobierz_plik(url: str, filename: str = "latest.txt")->None:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    with open(filename, "wb") as file:
        file.write(response.content)

#test
        pobierz_plik("https://oleksandr-fedoruk.com/sggw/podyplomowe/file","lokalny.txt")


#cw2


class DownloadError(Exception):
    pass

class NotFoundError(DownloadError):
 pass

class AccessDeniedError(DownloadError):
    pass


def pobierz_plik(url: str, filename: str = "latest.txt")->None:

    response = requests.get(url, timeout=10)
    response.raise_for_status() 

    if response.status_code == 404:
        raise NotFoundError(f"Nie znaleziono pliku pod adresem: {url}")
    elif response.status_code == 403:
        raise AccessDeniedError(f"Brak dostępu do pliku pod adresem: {url}")

    with open(filename, "wb") as file:
        file.write(response.content)

#test
        pobierz_plik("https://oleksandr-fedoruk.com/sggw/podyplomowe/file","lokalny.txt")

#cw3 ???



