from installer import install, command_formater
from subprocess import call
import os

def set_db_username():
    """
    Uses your login in name from your computer to create a Postgres account
    """
    username = os.getlogin()
    command = "sudo -u postgres createuser --superuser %s" % username
    call(command_formater(command))

def setup():
    """
    installs postgresql and postgressql-contrib
    """
    packages = 'postgresql postgresql-contrib'
    install(packages)
    set_db_username()


if __name__ == "__main__":
    setup()
