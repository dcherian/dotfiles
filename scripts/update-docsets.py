#!/usr/bin/env python3
import subprocess
import tqdm

for name in tqdm.tqdm(
    [
        "hvplot",
        "dask",
        "distributed",
        "dask-jobqueue",
        "numba",
        "cartopy",
        "xarray",
        "cf-xarray",
        "xgcm",
        "xrft",
        "sparse",
        "toolz",
    ]
):
    url = f"https://raw.githubusercontent.com/andersy005/dash-docsets/docsets/docsets/{name}.tar.gz"
    file = f"/tmp/{name}.xz"
    subprocess.run(["wget", url, "-O", file])
    subprocess.run(["tar", "-xvf", file, "--directory", f"{HOME}/docsets/"])
