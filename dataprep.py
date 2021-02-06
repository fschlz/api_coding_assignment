import requests
import pandas as pd
import io
import helper

logger = helper.setup_logging(__name__)


class Data():
    """class to pull and prepare data, as well as return stats

    Methods
    -------
        __init__(self)

        get_impression_stats(self, data_list: list)

        prep_impression_data(data: str, datatype: str) -> pd.DataFrame

        compute_metrics(dataframe: pd.DataFrame, column_name: str) -> dict
    """

    __name__ = "Data"

    def __init__(self):
        logger.debug(f"{self.__name__} instantiated")
        pass

    def get_impression_stats(self, data_list: list) -> dict:
        """ping urls to get data, process received data, return stats in a dictionary

        Parameters
        ----------
            data_list : list
                list containing dicts with urls of APIs and their respective data types

        Returns
        -------
            dict
                dictionary containing sum and mean
        """

        logger.info("evaluating data")

        dataframe = pd.DataFrame(columns=["date", "impressions"])

        for data_dict in data_list:

            url = data_dict.get('url')
            datatype = data_dict.get('datatype')

            logger.debug(f"calling API: {url}")
            result = requests.get(data_dict.get('url'))
            assert result.status_code == 200, logger.error(f"API response incorrect - status code: {result.status_code}")

            logger.debug(f"prep data as {datatype}")
            temp_df = self.prep_impression_data(data=result.text, datatype=datatype)

            dataframe = dataframe.append(temp_df, ignore_index=True).reset_index(drop=True)

        self.dataframe = dataframe

        logger.debug("calculating metrics")
        self.metrics_dict = self.compute_metrics(dataframe=self.dataframe, column_name="impressions")

        return self.metrics_dict

    @staticmethod
    def prep_impression_data(data: str, datatype: str) -> pd.DataFrame:
        """prepare received data according to its data type
        return a dataframe with the data

        Parameters
        ----------
            data: str
                data received from API call, i.e. response.get(url).text

            datatype : str
                either json or csv

        Returns
        -------
            pd.DataFrame
        """

        if datatype == "csv":
            dataframe = pd.read_csv(io.StringIO(data))
            dataframe.rename(columns={"impression": "impressions"}, inplace=True)
            return dataframe

        elif datatype == "json":
            dataframe = pd.read_json(data)
            return dataframe

        else:
            logger.error("datatype not found")

    @staticmethod
    def compute_metrics(dataframe: pd.DataFrame, column_name: str) -> dict:
        """calculate basic stats for a given column in a dataframe
        then return as a dictionary

        Parameters
        ----------
            dataframe : pd.DataFrame

            column_name : str

        Returns
        -------
            dict
                dictionary containing sum and mean
        """

        metrics_dict = {
            "mean": round(dataframe[column_name].mean(), 2),
            "sum": dataframe[column_name].sum(),
        }

        return metrics_dict
