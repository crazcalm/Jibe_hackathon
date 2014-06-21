from subprocess import call
import os

def install():
    """
    installs postgresql and postgressql-contrib
    """
    command = 'sudo apt-get install postgresql postgresql-contrib'
    command_list = command.split(" ")
    call(command.split(" "))

def set_db_username():
    """
    Uses your login in name from your computer to create a Postgres account
    """
    username = os.getlogin()
    command = "sudo -u postgres createuser --superuser %s" % username
    command_list = command.split(" ")
    call(command_list)

if __name__ == "__main__":
    install()
    set_db_username()
