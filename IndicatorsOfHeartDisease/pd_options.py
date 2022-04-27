import pandas as pd


def set_pandas_display_options(max_columns=None, max_rows=None, max_colwidth=None, width=None, max_=False):
    if max_:
        option = pd.options.display
        option.max_columns = None  # or 1000
        option.max_rows = None  # or 1000
        option.max_colwidth = None  # or 199
        option.width = None  # or 1000
        # pd.set_option('display.precision', 2)
    else:
        option = pd.options.display
        option.max_columns = max_columns  # or 1000
        option.max_rows = max_rows  # or 1000
        option.max_colwidth = max_colwidth  # or 199
        option.width = width  # or 1000