# I have Done some EDA on learning new librariesself.4
# This script is specifically for Dask


import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import os
import glob
import feather




# The first step is to import client from dask.distributed.
#This command will create a local scheduler and worker on your
#machine.
# Dask distributed is used for single machine
from dask.distributed import Client
client = Client() # start a local Dask client

# You can navigate to http://localhost:8787/status to see the diagnostic dashboard if you have Bokeh installed.


#The next step will be to instantiate dask joblib in the
# backend. You need to import parallel_backend from sklearn # joblib like I have shown below.


import dask_ml.joblib
from sklearn.externals.joblib import parallel_backend
with parallel_backend('dask'):
    # Your normal scikit-learn code here
     from sklearn.ensemble import RandomForestClassifier
     model = RandomForestClassifier()
