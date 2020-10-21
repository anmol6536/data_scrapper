# elsapy connector
# libraries Import

import pandas as pd
import os
from . import requests
from . import error

data_folder = os.path.abspath("./data")


@error.error
def final_result(search_string):
    """
    docstring for final_result
    Description:
    ------------
    Fromats the query terms into appropriate URL and queries Scopus

    Parameters:
    -----------
    search_string: Query Terms to search scopus with

    Return:
    -------
    out:dataframe with all returned information
    """
    req = requests.request_handler()
    apikey = req.apikey
    summary = req.get_summary(search_string)
    total_results = summary["total_results"]
    if total_results > 0:
        urls = req.get_urls(
            search_string=summary["search_terms"], total_results=total_results
        )
        final_result = []
        for url in urls:
            res = req.get_res(url)
            final_result.append(res)
        out = pd.concat(final_result)
        return out
    else:
        raise ValueError(f"No papers founds for the search string {search_string}")


def database_table():
    table = pd.read_csv(f"{data_folder}/table.ob", sep="\t")
    table = table.to_records()
    return table
