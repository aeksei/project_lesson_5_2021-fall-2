import requests


def get_page(url: str, params=None) -> str:
    if params is None:
        params = {}
    resp = requests.get(url, params=params)

    return resp.text


if __name__ == '__main__':
    url_str = "https://www.cbr.ru/scripts/XML_daily.asp?date_req=07/12/2021"
    print(get_page(url_str))

    url_str = "https://www.cbr.ru/scripts/XML_daily.asp"
    url_params = {
        "date_req": "07/12/2021"
    }
    print(get_page(url_str, url_params))
