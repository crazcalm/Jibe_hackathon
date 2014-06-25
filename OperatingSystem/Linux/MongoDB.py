from installer import install, command_formater
from subprocess import call
from time import sleep
import os

"""
  For more information about the commands, see Databases/MongoDB/Notes.txt
"""

COMMAND_LIST = ["sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10", "echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list", "sudo apt-get update", "sudo apt-get install mongodb"]

"""
Note:
-----
  Some online documatation says install mongodb-org, some say mongodb-10gen,
but plain mangodb worked for me.
"""

def setup():
    """
    Install MongoDB
    """
    for command in COMMAND_LIST:
        call(command_formater(command))
        sleep(1)

if __name__ == "__main__":
    setup()
