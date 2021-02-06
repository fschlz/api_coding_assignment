# %%
# imports
from flask import Flask
import json
import dataprep
import helper

# %%
# setup flask
app = Flask(__name__)

# %%
# define addresses where to pull data from
with open("./resources/data_sources.json") as f:
    data_list = json.load(f)


# %%
# stream data to localhost
@app.route('/')
def get_data(data_list: list = data_list):
    """instantiate the Data class and pipe results into Flask"""
    data = dataprep.Data()
    return data.get_impression_stats(data_list)


# %%
if __name__ == "__main__":
    # setup logging
    logger = helper.setup_logging(__name__, log_level="DEBUG")
    # run app on port 8000
    app.run(debug=True, port=8000)
