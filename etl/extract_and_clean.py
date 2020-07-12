import pandas as pd
import requests
from tqdm import tqdm  # progress bars

from abc import ABC, abstractmethod


class RawDataset(ABC):
    PATH_RAW = "data/raw/"
    PATH_CLEANED = "data/cleaned/"

    def __init__(self, URL):
        super().__init__()
        self.URL = URL

    def download_from_url(self, path):
        """
        Sends a request to a URI, opens a stream for downloading to a path
        Parameters
        ----------
        path: str
            path, incl filename to store the data
        """
        response = requests.get(self.URL, stream=True)

        with open(path, "wb") as out_file:
            for chunk in tqdm(response.iter_content(chunk_size=1024)):
                out_file.write(chunk)
        print("Done.")
        return

    @abstractmethod
    def get_raw(self):
        pass


class CovidDatahub(RawDataset):
    FILENAME = 'covid_datahub.csv'

    def __init__(self):
        super().__init__("https://storage.covid19datahub.io/data-1.csv")
        self.cleaned = False
        self.df = None

    def get_raw(self):
        self.download_from_url(self.PATH_RAW + self.FILENAME)
        return

    def get_cleaned(self, from_disk=False):
        self.cleaned = True

        if from_disk:  # ETL already performed
            self.df = pd.read_csv(self.PATH_CLEANED + self.FILENAME)
            return self.df

        else:  # perform data cleansing

            # read raw data from disk
            df_raw = pd.read_csv(self.PATH_RAW + self.FILENAME)

            # custom cleansing code : None
            self.df = (df_raw
                       .drop(columns=['key', 'key_apple_mobility', 'key_google_mobility',
                                      'administrative_area_level_2', 'administrative_area_level_3',
                                      'stringency_index', 'iso_alpha_3', 'iso_alpha_2', 'iso_numeric',
                                      'currency']
                             )
                       )

            # write to disk
            self.df.to_csv(self.PATH_CLEANED + self.FILENAME)

        return self.df

    def get_countries(self):
        if self.cleaned is True:
            df_countries = pd.DataFrame(self.df[['id', 'administrative_area_level_1', 'latitude', 'longitude']])
            countries = df_countries.drop_duplicates()
            countries.columns = ["code", "full_name", 'latitude', 'longitude']
            return countries
        else:
            return None

    def get_measures(self):
        if self.cleaned is True:
            return list(self.df.columns[12:23])
        else:
            return None

    def get_cleaned_df(self):
        return self.df


class MortalityOrg(RawDataset):
    URL = "https://www.mortality.org/Public/STMF/Outputs/stmf.csv"
    FILENAME = 'mortality_org.csv'

    def __init__(self):
        super().__init__(self.URL)
