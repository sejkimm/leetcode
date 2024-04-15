import numpy as np
import pandas as pd


def parse_data_to_dataframe(data: str, delimiter: str = "|") -> pd.DataFrame:
    """
    Parses a multiline string containing tabular data into a pandas DataFrame.

    :param data: A multiline string where each line is a record and values are separated by a delimiter.
    :param delimiter: The character that separates values in the data. Default is '|'.
    :return: A pandas DataFrame constructed from the parsed data.
    """
    # Split the data into lines
    lines = data.strip().split("\n")

    # Extract the header (first line) and use it to form the column names
    headers = lines[0].split(delimiter)
    headers = [header.strip() for header in headers]  # Remove any surrounding whitespace

    # Initialize a list to hold each data row as a dictionary
    records = []

    # Iterate over each line after the header, skipping the second line (dashes)
    for line in lines[2:]:
        if not line.strip().startswith("----"):  # Skip lines that start with '----'
            values = line.split(delimiter)
            values = [value.strip() for value in values]  # Clean up any surrounding whitespace
            values = [np.nan if value == "null" else value for value in values]
            record = dict(zip(headers, values))
            records.append(record)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(records)

    return df
