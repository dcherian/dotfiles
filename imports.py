import sys
sys.path.append('/home/deepak/python/')

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
import bottleneck as bn

# for company python completer
warnings.simplefilter("ignore",
                      category=PendingDeprecationWarning,
                      lineno=1943)

warnings.simplefilter(action='ignore', category=FutureWarning)
import h5py

import xrscipy as xrsp
import sciviscolor as svc
import moor
import chipy
import moorarr
import xfilter

import dcpy.xr_accessor

# projects
import sys
sys.path.append('/home/deepak/work/eddydiff/')
import eddydiff as ed

sys.path.append('/home/deepak/work/bay/scripts')
import bay

import dcpy.util
import dcpy.ts
import dcpy.oceans
import dcpy.plots
import dcpy.explode

warnings.resetwarnings()

warnings.filterwarnings("ignore", message="BlockingKernelClient._ip_changed")
warnings.filterwarnings("ignore", message="ResourceWarning")
warnings.filterwarnings("ignore", message="Completer")


def export_bokeh(plot, outPNG, outJS, outHTML, bkjs='local'):
    from bokeh.io import export_png
    from bokeh.embed import autoload_static, file_html
    import bokeh.resources

    if bkjs is 'local':
        # use local installed bokeh scripts
        wherebokeh = bokeh.resources.Resources(mode='absolute')

    if bkjs is 'remote' or bkjs is 'CDN':
        # use CDN bokeh scripts
        wherebokeh = bokeh.resources.CDN

    if bkjs is 'relative':
        # bkjs is a relative path?
        wherebokeh = bokeh.resources.Resources(mode='relative', root_dir='./bokeh/')

    if bkjs is 'inline':
        wherebokeh = bokeh.resources.INLINE

    # save the png file
    export_png(plot, filename=outPNG)

    # save the html file
    with open(outHTML, "w") as writer:
        writer.write(file_html(plot, wherebokeh, None))

    js, script = autoload_static(plot, wherebokeh, outJS)

    # save the .js file
    with open(outJS, "w") as writer:
        writer.write(js)

    # embed in the org-exported HTML file
    print('''#+BEGIN_EXPORT html\n{script}\n#+END_EXPORT'''.format(script=script.lstrip()))
