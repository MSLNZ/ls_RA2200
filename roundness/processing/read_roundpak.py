"""read mitutoyo roundpak files
efh
2020-05-18
"""
import numpy as np
import pandas as pd


def read_RA2200(fname, comment_rows=9):
    """read roundness trace generated from right clicking on element in roundpak program

       file may have different number of lines of comment or calculated results at start depending on RoundPak settings

    Arguments:
        fname {string} -- path of file to read

    Keyword Arguments:
        comment_rows {int} -- number of rows to skip at start of file (default: {9})

    Returns:
        numpy array -- n rows, 2 columns, value , position/radians
    """
    d = np.loadtxt(fname, skiprows=comment_rows, comments=list("#{}"))
    return d[:, 2], np.radians(d[:, 1])


def read_result(fname, start_row=14):
    """reads result file from roundpak into pandas dataframe

    These files may differ depending on Roundpak settings, this reads the default/current version 

    Arguments:
        fname {string} -- any valid string path is acceptable

    Keyword Arguments:
        start_row {int} -- first row of file to read (default: {14})

    Returns:
        [pandas DataFrame ] -- contains one row of data with headers from file
    """
    r = lambda x: (float(x.replace("\xb5m", "")))  # µm
    d = lambda x: (float(x.replace("\xb0", "")))  # °
    converters = {
        **dict.fromkeys(
            [
                "Roundness(RONt)",
                "DX",
                "DY",
                "DL",
                "Peak(RONp)",
                "Valley(RONv)",
                "Mean Roundness",
            ],
            r,
        ),
        **dict.fromkeys(["DA"], d),
    }

    df = pd.read_csv(
        fname,
        skiprows=start_row - 1,
        nrows=1,
        encoding="latin-1",
        converters=converters,
    )
    return df


def read_result_list(fnames, ids, start_row=14):
    """read a list of roundpak result files into one dataframe

    Arguments:
        fnames {list of file paths} -- list of rounpak result files
        ids {list of identifiers} -- file identifiers for first column of dataframe

    Keyword Arguments:
        start_row {int} -- first row of file to read (default: {14})

    Returns:
        [pandas DataFrame] -- contains one row of data per file
    """
    df_list = []
    for fname, id_field in zip(fnames, ids):
        df = read_result(fname, start_row=start_row)
        df.iloc[0, 0] = id_field
        df_list.append(df)
    df = pd.concat(df_list)
    return df
