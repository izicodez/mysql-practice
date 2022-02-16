from ast import Try
from asyncore import read
from re import I
import mysql.connector
from tabulate import tabulate

# Connecting
# Enter your username and password.
conn  = mysql.connector.connect(
    user='root', password='mysql@P@ssw0rd', host='127.0.0.1', database='mysql'
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()




def main(command):
    """
    Take the command run the execution and then append 
    it to a text file called "results.txt"
    param command: Takes mysql command as a parameter
    """
    # while True:
    try:
        # Take input from the user
        # command = input("Enter any mysql Command that you would like to store: ")
        if command == 'exit' or command == '0':
            pass

        cursor.execute(command)
        result = cursor.fetchall()
        results = tabulate(result, headers=[cursor.column_names[0]], tablefmt='psql')


        with open('results', 'a+') as file:
            file.write("\nThe commmand: " + command + "\n")
            file.write(results)
        
    except Exception:
        print(f"\nPlease check your command : \n{command}\n and enter again ")

def readfile():
    """
    Reading the file that has mysql commands, then executing it 
    Send the commands to main function.
    Once all commands have been executed end the connection
    """
    with open("mysqlCommands", "r") as file:
        readline=file.read().splitlines()
        for i in readline:
            if i == "":
                pass
            else:
                main(i)
    conn.close()
readfile()