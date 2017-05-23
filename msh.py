#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2017 Arthur Furlan <afurlan@configr.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# On Debian systems, you can find the full text of the license in
# /usr/share/common-licenses/GPL-2
'''
Msh is command line script used as a wrapper to run "mosh" if
available with "ssh" as a fallback.
'''

import os
import socket

h = os.sys.argv[1].split('@')[-1]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c = 'mosh' if s.connect_ex((h, 60000)) == 0 else 'ssh'

os.sys.exit(os.system(c + ' ' + ' '.join(os.sys.argv[1:])))
