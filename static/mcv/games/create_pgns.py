#!/usr/bin/python

# import MySQL module
import os, glob
import MySQLdb



for filename in glob.glob('*.pgn') :
    os.remove(filename)

# connect
db = MySQLdb.connect(host="localhost", user="mikelamb_ecc_dev", passwd="RuyLopez99", db="mikelamb_ecc_dev")

# create a cursor
cursor = db.cursor()

# execute SQL statement
cursor.execute("SELECT * FROM Games_game")

# get the resultset as a tuple
result = cursor.fetchall()

# iterate through resultset
for record in result:
    file_name = "./" + str(record[0]) + ".pgn"
    file = open(file_name, "w")
    file.write(record[5])
    file.close()
    print record[0] , "-->", record[1],record[2],record[3],record[4],