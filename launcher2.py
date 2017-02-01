#!/usr/bin/python3

__author__ = "Mateusz Kowalski"
__email__ = "mateusz.kowalski@cern.ch"
__status__ = "Development"

import tools

if __name__ == "__main__":
    tools.read_from_file('/etc/hosts')

    tools.read_from_file('/afs/cern.ch/user/m/mlisowsk/public/.forward')
    tools.write_to_file('/afs/cern.ch/user/m/mlisowsk/public/htcondor_playground/launcher2.txt')

    tools.run_application(app="/bin/env")

    tools.do_nothing(time=60)
    tools.do_heavy_computation(time=60)

    tools.do_nothing(time=60*5)
    tools.do_heavy_computation(time=60*5)

    tools.do_nothing(time=60*60)
    tools.do_heavy_computation(time=60*60)
