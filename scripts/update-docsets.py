#!/usr/bin/env python3
import subprocess
import tqdm

for name in tqdm.tqdm(["dask", "xarray", "distributed", "numba",
                       # "xgcm"
                       ]):
    url = f"https://raw.githubusercontent.com/andersy005/dash-docsets/docsets/docsets/{name}.tgz"
    file = f"/tmp/{name}.tgz"
    subprocess.run(["wget", url, "-O", file])
    subprocess.run(["tar", "-xvf", file, "--directory", "/home/deepak/docs/docsets/"])
