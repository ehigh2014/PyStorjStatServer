# -*- coding: utf-8 -*-
"""
Created on Wed Dec 06 13:41:49 2017

@author: ehigh
@email : ehigh2014@163.com
"""

import daemon
from main import server_run

with daemon.DaemonContext():
    server_run()