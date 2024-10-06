"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

"""

import requests


def extract(
    url="https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/candy-power-ranking/candy-data.csv",  # put the link to raw data here, one with only a couple off
    file_path="data/candy-data.csv",
    directory="data",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path


if __name__ == "__main__":
    extract()
