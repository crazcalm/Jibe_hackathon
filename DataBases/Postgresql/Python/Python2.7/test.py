from subprocess import call
import os, sys, psycopg2


ERRORS = ["Could not create database", "Issue with basic Pysconpg commands",
            "Could not Delete database"]

def main():
    """
    Controls the flow of the program
    """

    # Coupling the error msgs with the functions
    function_list = [(createdb,ERRORS[0]), (basic_functionality, ERRORS[1]),
                        (deletedb, ERRORS[2])]

    for func, error in function_list:
        test_function(func, error)

    print "Past all tests!"

def command_formater(command):
    """
    Formats the commands for the subprocess.call function
    """
    return command.split(" ")

def createdb():
    """
    Creates a test database
    """
    command = "createdb crazcalm"
    call(command_formater(command))

def deletedb():
    """
    Deletes the test database
    """
    command = "dropdb crazcalm"
    call(command_formater(command))

def test_function(func, error):
    """
    Takes and function and an error msg and runs them in a try/except statment
    """
    try:
        func()
    except Exception:
        sys.exit(error)

def basic_functionality():
    """
    Runs the the basic psycopg2 commands
    """
    username = os.getlogin()

    # Connecting to an existing databases
    conn = psycopg2.connect("dbname=crazcalm user=%s" % username)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: This creates a new table
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, "
                +"data varchar);")

    # Pass data to fill a query placeholders and let Psyconpg perform
    # the correct conversion (no more SQL injections!)
    cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
            (100, "abc'def"))

    # Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM test")
    cur.fetchone()

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()


def hello(name="Marcus"):
    print "Hello %s" % name

if __name__ == "__main__":
    main()


