import os
import sys

hostname = os.uname()[1]
if hostname == 'darya':
    home = '/home/deepak/'
elif 'cheyenne' in hostname or 'casper' in hostname:
    home = '/glade/u/home/dcherian/'
elif 'caguas' in hostname:
    home = '/Users/dcherian/'

# sys.path.append(home + 'python/')

import warnings

import matplotlib as mpl
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore", message="numpy.dtype size changed")
import numpy as np
import scipy as sp
import pandas as pd

import xarray as xr
xr.set_options(keep_attrs=True)

# for company python completer
warnings.simplefilter("ignore",
                      category=PendingDeprecationWarning,
                      lineno=1943)

warnings.simplefilter(action='ignore', category=FutureWarning)

# projects
if hostname in ['darya', 'cgdm-caguas']:
    sys.path.append(home + 'work/eddydiff/')
    sys.path.append(home + 'work/bay/scripts')
    # import eddydiff as ed

    # import bay
    # import moor
    # import chipy
