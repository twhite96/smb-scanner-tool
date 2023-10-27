#!/usr/bin/python

# Would using the queue library to lessen stress in a multithreaded scan be performant?
# would the user notice?
# could I use asyncio?
# find an instance where if the scanner is detected, we kill the process with kill()
# download the files, perhaps compressing them? If there are too many, it might take a long time, thus
# taxing cpu. put on a file limit
# Reference for the jitter methods: https://www.agora.io/en/blog/what-is-jitter-meaning-causes-and-solutions/

import getpass
import ipaddress
import logging
import os
import re
import sys
import time

from impacket.smb import SMB_DIALECT
from slugify import slugify
from logging import handlers #import logging.handlers as handlers

from arg_parser import setup_command_line_args, Options
from scan import scan_single, User

from multiprocessing.pool import Pool
from multiprocessing.pool import ThreadPool
# from multiprocessing import Process, Queue
from multiprocessing import set_start_method
from threading import Thread