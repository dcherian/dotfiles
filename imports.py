import os
import sys

hostname = os.uname()[1]
if hostname == 'darya':
    home = '/home/deepak/'
elif 'cheyenne' in hostname:
    home = '/glade/u/home/dcherian/'
elif 'caguas' in hostname:
    home = '/Users/dcherian/'

sys.path.append(home + 'python/')

import warnings

import importlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import cmocean

warnings.filterwarnings("ignore", message="numpy.dtype size changed")
import numpy as np

import scipy as sp
import pandas as pd
import seaborn as sns

import xarray as xr
xr.set_options(keep_attrs=True)

import netCDF4 as nc
import seawater as sw
# import gsw

# for company python completer
warnings.simplefilter("ignore",
                      category=PendingDeprecationWarning,
                      lineno=1943)

warnings.simplefilter(action='ignore', category=FutureWarning)

import xrscipy as xrsp
import sciviscolor as svc
import xfilter

import dcpy.xr_accessor

# projects
if hostname in ['darya', 'cgdm-caguas']:
    sys.path.append(home + 'work/eddydiff/')
    sys.path.append(home + 'work/bay/scripts')
    import eddydiff as ed

    import bay
    import moor
    import chipy

import dcpy.util
import dcpy.ts
import dcpy.oceans
import dcpy.plots
