#!/usr/bin/env python3

__author__ = 'yuwei'

import sys
import os
import platform
from glob import glob

from zhihurss.main import run


if platform.system() == 'Darwin':
    sip_site = glob("/usr/local/Cellar/sip/*/lib/python3.[0-9]/site-packages/")[0]
    pyqt5_site = glob("/usr/local/Cellar/pyqt5/[0-9].[0-9]/lib/python3.[0-9]/site-packages/")[0]
    sys.path.insert(0, pyqt5_site)
    sys.path.insert(0, sip_site)


if __name__ == '__main__':

    if hasattr(sys, 'frozen') is False:
        path = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, os.path.join(path, "zhihurss"))
    run()

