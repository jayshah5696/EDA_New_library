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

# Instead of creatinf direct client, you can form your own cluster and than build client on top of thatself.

from dask.distributed import Client, LocalCluster
cluster = LocalCluster()
client = Client(cluster)

# This will allow you to control your clusters properties.


#The next step will be to instantiate dask joblib in the
# backend. You need to import parallel_backend from sklearn # joblib like I have shown below.


import dask_ml.joblib
from sklearn.externals.joblib import parallel_backend
with parallel_backend('dask'):
    # Your normal scikit-learn code here
     from sklearn.ensemble import RandomForestClassifier
     model = RandomForestClassifier()


# I want to parallize the custom workflows
# This can be used with the sciki learn pipeline.

# Let's say I have a function that do some process on the data.
# And I want to parallize the process using dask_ml

def process(data):

    return something

# Normal process
results = [processs(x) for x in inputs]


# Instead of this now wrap this function in dask.delayed and let the appropriate dask scheduler parallelize and load balance the work.

from dask import compute, delayed
values = [delayed(process)(x) for x in inputs]
# This task is same for local and clusters machine computation

# 1 Now for multiple threads
import dask.threaded
results = compute(*values, scheduler='threads')

# 2 for cluster
from dask.distributed import Client
client = Client("cluster-address:8786")
results = compute(*values, scheduler='distributed'


# Now every function can be wrapped under delayed computation
