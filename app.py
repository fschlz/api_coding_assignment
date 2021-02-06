from flask import Flask
import json
import dataprep
import helper

app = Flask(__name__)

with open("./resources/data_sources.json") as f:
    data_list = json.load(f)


@app.route('/')
def get_data(data_list: list = data_list):
    """instantiate the Data class to pipe results into Flask"""
    data = dataprep.Data()
    return data.get_impression_stats(data_list)


if __name__ == "__main__":
    logger = helper.setup_logging(__name__, log_level="INFO")
    app.run(debug=True, port=8000)
