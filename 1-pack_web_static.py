#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    d_time = datetime.now()
    path = "versions/web_static_{}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz".format(
        d_time.year,
        d_time.month,
        d_time.day,
        d_time.hour,
        d_time.minute,
        d_time.second
    )
    try:
        print("Packing web_static to {}".format(path))
        local("tar -cvzf {} web_static".format(path))
        size = os.stat(path).st_size
        print("web_static packed: {} -> {}Bytes".format(path, size))
    except Exception:
        path = None
    return path
