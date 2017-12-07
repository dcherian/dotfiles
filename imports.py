import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr
import importlib

import netCDF4 as nc
import h5py
import seawater as sw
import matplotlib.dates as dt
import bottleneck as bn

import sys
sys.path.append('/home/deepak/python/')

import moor
import chipy
import moorarr

import dcpy.util
import dcpy.ts
import dcpy.oceans
import dcpy.plots

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
