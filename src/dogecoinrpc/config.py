# Copyright (c) 2010 Witchspace <witchspace81@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
Utilities for reading dogecoin configuration files.
"""

import os
import platform
from pathlib import Path


def read_config_file(filename):
    """
    Read a simple ``'='``-delimited config file.
    Raises :const:`IOError` if unable to open file, or :const:`ValueError`
    if an parse error occurs.
    """
    with open(filename) as f:
        cfg = {}
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                try:
                    (key, value) = line.split("=", 1)
                    cfg[key] = value
                except ValueError:
                    pass  # Happens when line has no '=', ignore
    return cfg


def read_default_config(filename=None):
    """
    Read dogecoin default configuration from the current user's home directory.

    Arguments:

    - `filename`: Path to a configuration file in a non-standard location (optional)
    """
    if filename is None:
        home = str(Path.home())
        if platform.system() == "Darwin":
            location = "Library/Application Support/Dogecoin/dogecoin.conf"
        elif platform.system() in ("Windows", "Microsoft"):
            location = "AppData\\Roaming\\DogeCoin\\dogecoin.conf"
        else:
            location = ".dogecoin/dogecoin.conf"
        filename = os.path.join(home, location)

    elif filename.startswith("~"):
        filename = os.path.expanduser(filename)

    try:
        return read_config_file(filename)
    except (IOError, ValueError):
        pass  # Cannot read config file, ignore
