from update_bot_name import botNameUpdate
import sqlite3
from sqlite3 import Error
import dateparser



def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def updateNextTourney(_nextTourney):

  connection = create_connection('tournamentDb')
  cursor = connection.cursor()

  nextTourney = dateparser.parse(f'{_nextTourney}, cst',)

  createTableCommand = """CREATE TABLE IF NOT EXISTS
  tournamentDb(tournamentID INTEGER PRIMARY KEY, TdateTime DATETIME)"""

  cursor.execute(createTableCommand)


  #add rows
  cursor.execute("INSERT INTO tournamentDb VALUES(?,?)", (1, nextTourney))

  cursor.execute("SELECT * FROM tournamentDb")
  results = cursor.fetchall()
  print(results)


  #Send results
  botNameUpdate(f'Next Tournament: {nextTourney}', "Tourney_Bot_Token", "test")