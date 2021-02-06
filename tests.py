import numpy as np
import pandas as pd
import dataprep

# setup test data
url_dict = {
    "https://run.mocky.io/v3/9a01a1b9-26e1-4c8a-84db-d534352e1461": "json",
    "https://run.mocky.io/v3/ba026992-281a-42a6-8447-ae1c8a04106e": "csv"
}

data = dataprep.Data()

data_csv = open("./resources/source_b.csv").read()
data_json = open("./resources/source_a.json").read()

test_df = pd.DataFrame({
    "impressions": np.arange(1, 11)
})


class TestTypes:
    def test_prep_csv_type(self):
        t = type(data.prep_impression_data(data_csv, "csv"))
        assert t == pd.DataFrame, "data prep didn't return dataframe"

    def test_prep_json_type(self):
        t = type(data.prep_impression_data(data_json, "json"))
        assert t == pd.DataFrame, "data prep didn't return dataframe"

    def test_compute_metrics_type(self):
        t = type(data.compute_metrics(test_df, "impressions"))
        assert t == dict, "results are not a dict"

    def test_data_class(self):
        t = type(data.get_impression_stats(url_dict))
        assert t == dict, "results are not a dict"


class TestResults:
    def test_compute_metrics_sum(self):
        s = data.compute_metrics(test_df, "impressions").get("sum")
        assert s == 55, "sum calculation's wrong"

    def test_compute_metrics_mean(self):
        m = data.compute_metrics(test_df, "impressions").get("mean")
        assert m == 5.5, "mean calculation's wrong"
