import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Copernicus Credentials
CDSE_USERNAME = os.getenv("CDSE_USERNAME")
CDSE_PASSWORD = os.getenv("CDSE_PASSWORD")

# Data Paths
DATA_RAW = Path(os.getenv("DATA_RAW", BASE_DIR / "data/raw"))
DATA_PROCESSED = Path(os.getenv("DATA_PROCESSED", BASE_DIR / "data/processed"))
MODEL_DIR = Path(os.getenv("MODEL_DIR", BASE_DIR / "data/models"))

# Malaysia AOI (Klang Valley)
AOI_WKT = "POLYGON((101.4 2.9, 101.9 2.9, 101.9 3.4, 101.4 3.4, 101.4 2.9))"

# Model Parameters
RF_PARAMS = {"n_estimators": 200, "max_depth": 15, "class_weight": "balanced"}
CNN_PARAMS = {"time_steps": 5, "height": 64, "width": 64, "channels": 4}