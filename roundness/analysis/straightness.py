"""functions to determine spindle parallelism to z-axis by measuring straightness"""

import numpy as np
import pandas as pd


def straighness_reversal(out, opp):
    """separate machine and part straighness by reversal"""
    # interpolate outer and inner dfs onto same index and combine dfs
    start = max(opp.loc[0, "ZPos (mm)"], out.loc[0, "ZPos (mm)"])
    stop = min(opp.loc[opp.index[-1], "ZPos (mm)"], out.loc[out.index[-1], "ZPos (mm)"])
    interval = 0.004
    zpos = np.arange(start, stop, interval)
    df1 = opp.set_index("ZPos (mm)")
    df1 = (
        df1.reindex(df1.index | zpos)
        .interpolate(method="index", limit_direction="both")
        .loc[zpos]
    )
    df2 = out.set_index("ZPos (mm)")
    df2 = (
        df2.reindex(df2.index | zpos)
        .interpolate(method="index", limit_direction="both")
        .loc[zpos]
    )
    S1 = pd.concat([df1, df2], axis=1)
    S1.columns = [c + "_opp" for c in df1.columns] + [c + "_out" for c in df2.columns]

    # separate machine and part profiles
    # the signs chosen to match directions given by wire taped to surface
    S1["machine"] = (
        S1["Extracted line (µm)_out"] + S1["Extracted line (µm)_opp"]
    ) / 2.0
    S1["part"] = (S1["Extracted line (µm)_out"] - S1["Extracted line (µm)_opp"]) / 2.0
    S1["machine filtered"] = (S1["Profile (µm)_out"] + S1["Profile (µm)_opp"]) / 2.0
    S1["part filtered"] = (S1["Profile (µm)_out"] - S1["Profile (µm)_opp"]) / 2.0

    return S1


def df_interpolate(df1, df2, column=None):
    """combine two dataframes onto a common index by interpolation
       both dataframes should contain "column"
       if column is None the index is used.
    """
    pass
