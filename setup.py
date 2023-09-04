from googlesearch import search
import pandas as pd

search_history = {}  # Dictionary to store search history


def perform_search(query):
    try:
        return list(search(query, tld="co.in", num=100, stop=100, pause=2))
    except ImportError:
        print("No module named 'google' found")
        return []


def process_results(results):
    ranking_list = []
    site_name_list = []
    results_list = []

    for i, j in enumerate(results):
        j = j.replace('www.', '')
        ranking_list.append(i + 1)
        site_name_list.append(j.split('/')[2])
        results_list.append(j)

    return ranking_list, site_name_list, results_list


def create_dataframe(ranking, site_name, results):
    data = {'Ranking': ranking, 'Site Name': site_name, 'Results': results}
    return pd.DataFrame(data)
