import os

PROJ_ROOT = os.path.join(__file__, os.pardir, os.pardir)
PROJ_ROOT = os.path.abspath(PROJ_ROOT)
DATA_ROOT = os.path.join(PROJ_ROOT, "data")

DATA_RAW = os.path.join(DATA_ROOT, "raw")
DATA_PROCESSED = os.path.join(DATA_ROOT, "processed")

RESULTS = os.path.join(PROJ_ROOT, "results")
FIGURES = os.path.join(RESULTS, "figures")
