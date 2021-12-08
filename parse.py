import json
import datetime
from typing import Optional

import xmltodict

from client import get_page
from conf import URL_CBR, FORMAT_DATETIME


def xml_to_dict(xml_str: str) -> dict:
    """ Test """
    return xmltodict.parse(xml_str)


def get_exchange(date: Optional[str] = None):  # todo добавить регулярку
    """
    Курс обмена ...

    :param date: теук
    :return:
    """
    if date is None:
        date = datetime.datetime.now().strftime(FORMAT_DATETIME)

    url_params = {
        "date_req": date
    }

    dict_ = xml_to_dict(get_page(URL_CBR, url_params))
    print(json.dumps(dict_, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    get_exchange()
