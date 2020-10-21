import requests
from . import error
import json


class dataset_retriever:

    #     def __init__(self):
    #         db_names = pd.read_csv("/Users/anmol_gorakshakar/python/github/alpine_ridge/allergan/assets/db_names.ob", sep = '\t')
    #         self.db_names = db_names
    #     return

    def url_handler(
        self,
        search_type="esearch",
        query_term="",
        db="pubmed",
        retmax=500,
        retmode="json",
        webenv="",
        query_key="",
    ):
        base = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/{search_type}.fcgi"
        query_term = query_term.replace(" ", "%20")
        term = f"&term={query_term}"
        ret_number = f"&retmax={retmax}"
        ret_data_type = f"&retmode={retmode}"
        db = f"?db={db}"
        if search_type == "esearch":
            url = base + db + term + ret_number + ret_data_type + "&usehistory=y"
        if search_type == "esummary":
            webenv = f"&webenv={webenv}"
            query_key = f"&query_key={query_key}"
            url = (
                base
                + db
                + query_key
                + webenv
                + ret_data_type
                + ret_number
                + "&usehistory=y"
            )
        self.url = url
        return url

    def database_overview(self, url=None, db="gds"):
        if not url:
            url = self.url
        content = requests.get(url).content
        json_df = json.loads(content)
        query_key = json_df["esearchresult"]["querykey"]
        webenv = json_df["esearchresult"]["webenv"]
        print(query_key, webenv)
        url = self.url_handler(
            search_type="esummary", db=db, query_key=query_key, webenv=webenv
        )
        print(url)
        res = requests.get(url)
        res = json.loads(res.text)
        return res


def database_search_run(query, db="gds"):
    handler = dataset_retriever()
    url = handler.url_handler(query_term=query, db=db)
    df = handler.database_overview(url, db=db)
    # df["result"].pop("uids")
    return df
