#!/usr/bin/python3

__author__ = "Mateusz Kowalski"
__email__ = "mateusz.kowalski@cern.ch"
__status__ = "Development"

import tools

tools.do_heavy_computation(time=1)
tools.do_nothing(time=1)
tools.read_from_file('/etc/hosts')
tools.do_heavy_computation(time=3)
tools.do_nothing(time=3)
tools.run_application("echo", "test 123")
