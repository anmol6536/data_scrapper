#elsapy connector
#libraries Import

import pandas as pd
from . import requests

def final_result(search_string, total_results = None):
    req = requests.request_handler()
    apikey = req.apikey
    summary = req.get_summary(search_string)
    if not total_results:
        total_results = summary['total_results']
    urls = req.get_urls(search_string = summary['search_terms'], total_results = total_results)
    final_result = []
    for url in urls:
        res = req.get_res(url)
        final_result.append(res)
    out = pd.concat(final_result)
    return out
