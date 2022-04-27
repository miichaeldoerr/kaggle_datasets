import pandas as pd

class Extract(object):
    FILENAME = None

    def __init__(self):
        pass

    @classmethod
    def from_json(cls, filename):
        pass

    @classmethod
    def from_csv(cls, filename):
        cls.FILENAME = filename
        return pd.read_csv(cls.FILENAME)

    @classmethod
    def return_file(cls):
        if cls.FILENAME is None:
            raise Exception("No filename provided.")

        return cls.FILENAME


