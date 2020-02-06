import random
import sqlite3
import string
import sys
import numpy as np


punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# special for register and login app (ID GENERATOR)
def ID():
    uniqueNUM = random.choice(np.linspace(10000, 100000, 10000).round(0))
    letter = []
    for i in range(random.randint(10, 15)):
        lower = random.choice(string.ascii_lowercase)
        upper = random.choice(string.ascii_uppercase)
        letter.append(upper)
        letter.sort()
    uniqueID = ''
    uniqueID += ( letter[random.randint(0, 4)] + letter[
        random.randint(5, 7)] + letter[-1] + str(int(uniqueNUM))
                 + lower + random.choice(string.ascii_lowercase))
    return uniqueID


''' DB COMMAND ONLY SUPPORT UNTIL 6 COLUMN !!!, WAITING FOR UPDATE'''
def db_command2(command, database_name, table_name, column1, column2, INSERT1='', INSERT2='', WHERE='', SET='',SETWHERE='', WHEREPLACE='', WHERESELECT = ''):
    '''THIS FUNCTION ONLY SUPPORT 2 COLUMN,
     COMMAND=(INSERT, DELETE, UPDATE, SELECT ALL, SELECT ALL CHOICE AND SELECT CHOICE)
     WHERE=(COLUMN NAME)
     SETWHERE=(LOCATE COLUMN NAME TO SET THE DATA)
     WHEREPLACE=(THE DATA AFTER /WHERE/ COMMAND)
     WHERESELECT=(TO SELECTED THE COLUMN A.K.A COLUMN NAME)
     SET=(VALUE TO SET)

    INSERT:("INSERT INTO {table_name} VALUES (?,?)", (INSERT1, INSERT2))
     DELETE: ("DELETE FROM {table_name} WHERE {WHERE}")
     UPDATE: ("UPDATE {table_name} SET {SETWHERE}=? WHERE {WHERE}=? ", (SET, WHEREPLACE))
     SELECT ALL: ("SELECT * FROM {table_name}")
     SELECT ALL CHOICE: ("SELECT {WHERE} FROM {table_name} ")
     SELECT CHOICE: ("SELECT {WHERESELECT} FROM {table_name} WHERE {WHERE}={WHEREPLACE} ")
     '''

    print("COMMAND STARTED")
    conn = sqlite3.connect(database_name)
    console = conn.cursor()
    com = str(command).upper()
    print(conn, com)
    if com.upper() == "INSERT":
        console.execute(f"INSERT INTO {table_name} VALUES (?,?)", (INSERT1, INSERT2))
        conn.commit()
        conn.close()
        print(f"""{INSERT1} INSERT {column1}
{INSERT2} INSERT {column2}
DATA SUCCESSFULLY INSERTED""")

    elif com.upper() == "DELETE":
        console.execute(f"DELETE FROM {table_name} WHERE {WHERE}")
        conn.commit()
        conn.close()
        print(f""" Data from {table_name} at {WHERE}
SUCCESSFULLY DELETED""")

    elif com.upper() == "UPDATE":
        console.execute(f"UPDATE {table_name} SET {SETWHERE}=? WHERE {WHERE}=? ", (SET, WHEREPLACE))
        conn.commit()
        conn.close()
        print(f"""Data from {table_name} at {WHERE}={WHEREPLACE}
Set {SETWHERE} to {SET}
SUCCESSFULLY UPDATED""")

    elif com.upper() == "SELECT ALL":
        console.execute(f"SELECT * FROM {table_name}")
        conn.commit()
        row = console.fetchall()
        for rows in row:
            print(rows)
        print("")
        print("ALL DATA SELECTED")
        conn.close()
        list = []
        for rows in row:
            list.append(rows[0])
            list.append(rows[1])
        #     data_one = rows[0]
        #     data_two = rows[1]
        #     data_three = rows[2]
        #     data_four = rows[3]
        # return data_one,data_two,data_three,data_four
        return list

    elif com.upper() == "SELECT ALL CHOICE":
        console.execute(f"SELECT {WHERE} FROM {table_name} ")
        conn.commit()
        row = console.fetchall()
        list = []
        for rows in row:
            print(rows)
            list.append(rows)
        print("")
        print(f"DATA {WHERE} SELECTED")
        conn.close()
        return list

    elif com.upper() == "SELECT CHOICE":
        console.execute(f"SELECT {WHERESELECT} FROM {table_name} WHERE {WHERE}={WHEREPLACE} ")
        conn.commit()
        raw = str(console.fetchone())
        data = ''
        for i in raw:
            if i not in punctuations:
                data = data + i
        print('')
        print("DATA SELECTED")
        conn.close()
        return data

    else:
        print("ONLY EXCEPT COMMAND (INSERT, UPDATE, DELETE, SELECT ALL, SELECT ALL CHOICE, SELECT CHOICE)", file=sys.stderr)


def db_command3(command, database_name, table_name, column1, column2, column3, INSERT1='', INSERT2='',INSERT3 = '' , WHERE='', SET='',SETWHERE='', WHEREPLACE='', WHERESELECT = ''):
    '''THIS FUNCTION ONLY SUPPORT 3COLUMN,
         COMMAND=(INSERT, DELETE, UPDATE, SELECT ALL, SELECT ALL CHOICE AND SELECT CHOICE)
         WHERE=(COLUMN NAME)
         SETWHERE=(LOCATE COLUMN NAME TO SET THE DATA)
         WHEREPLACE=(THE DATA AFTER /WHERE/ COMMAND)
         WHERESELECT=(TO SELECTED THE COLUMN A.K.A COLUMN NAME)
         SET=(VALUE TO SET)

        INSERT:("INSERT INTO {table_name} VALUES (?,?)", (INSERT1, INSERT2))
         DELETE: ("DELETE FROM {table_name} WHERE {WHERE}")
         UPDATE: ("UPDATE {table_name} SET {SETWHERE}=? WHERE {WHERE}=? ", (SET, WHEREPLACE))
         SELECT ALL: ("SELECT * FROM {table_name}")
         SELECT ALL CHOICE: ("SELECT {WHERE} FROM {table_name} ")
         SELECT CHOICE: ("SELECT {WHERESELECT} FROM {table_name} WHERE {WHERE}={WHEREPLACE} ") '''

    print("COMMAND STARTED")
    conn = sqlite3.connect(database_name)
    console = conn.cursor()
    com = str(command).upper()
    print(conn, com)
    if com.upper() == "INSERT":
        console.execute(f"INSERT INTO {table_name} VALUES (?,?,? )", (INSERT1, INSERT2, INSERT3))
        conn.commit()
        conn.close()
        print(f"""{INSERT1} INSERT {column1}
{INSERT2} INSERT {column2}
{INSERT3} INSERT {column3}
DATA SUCCESSFULLY INSERTED""")

    elif com.upper() == "DELETE":
        console.execute(f"DELETE FROM {table_name} WHERE {WHERE}")
        conn.commit()
        conn.close()
        print(f""" Data from {table_name} at {WHERE}
SUCCESSFULLY DELETED""")

    elif com.upper() == "UPDATE":
        console.execute(f"UPDATE {table_name} SET {SETWHERE}=? WHERE {WHERE}=? ", (SET, WHEREPLACE))
        conn.commit()
        conn.close()
        print(f"""Data from {table_name} at {WHERE}={WHEREPLACE}
Set {SETWHERE} to {SET}
SUCCESSFULLY UPDATED""")

    elif com.upper() == "SELECT ALL":
        console.execute(f"SELECT * FROM {table_name}")
        conn.commit()
        row = console.fetchall()
        for rows in row:
            print(rows)
        print("")
        print("ALL DATA SELECTED")
        conn.close()
        list = []
        for rows in row:
            list.append(rows[0])
            list.append(rows[1])
            list.append(rows[2])
        #     data_one = rows[0]
        #     data_two = rows[1]
        #     data_three = rows[2]
        #     data_four = rows[3]
        # return data_one,data_two,data_three,data_four
        return list

    elif com.upper() == "SELECT ALL CHOICE":
        console.execute(f"SELECT {WHERE} FROM {table_name} ")
        conn.commit()
        row = console.fetchall()
        list = []
        for rows in row:
            print(rows)
            list.append(rows)
        print("")
        print(f"DATA {WHERE} SELECTED")
        conn.close()
        return list

    elif com.upper() == "SELECT CHOICE":
        console.execute(f"SELECT {WHERESELECT} FROM {table_name} WHERE {WHERE}={WHEREPLACE} ")
        conn.commit()
        raw = str(console.fetchone())
        data = ''
        for i in raw:
            if i not in punctuations:
                data = data + i
        print('')
        print("DATA SELECTED")
        conn.close()
        return data

    else:
        print("ONLY EXCEPT COMMAND (INSERT, UPDATE, DELETE, SELECT ALL, SELECT ALL CHOICE, SELECT CHOICE)", file=sys.stderr)


def db_command4(command, database_name, table_name, column1, column2, column3, column4, INSERT1='', INSERT2='',INSERT3 = '', INSERT4 ='' , WHERE='', SET='',SETWHERE='', WHEREPLACE='', WHERESELECT = ''):
    '''THIS FUNCTION ONLY SUPPORT 3COLUMN,
             COMMAND=(INSERT, DELETE, UPDATE, SELECT ALL, SELECT ALL CHOICE AND SELECT CHOICE)
             WHERE=(COLUMN NAME)
             SETWHERE=(LOCATE COLUMN NAME TO SET THE DATA)
             WHEREPLACE=(THE DATA AFTER /WHERE/ COMMAND)
             WHERESELECT=(TO SELECTED THE COLUMN A.K.A COLUMN NAME)
             SET=(VALUE TO SET)

            INSERT:("INSERT INTO {table_name} VALUES (?,?)", (INSERT1, INSERT2))
             DELETE: ("DELETE FROM {table_name} WHERE {WHERE}")
             UPDATE: ("UPDATE {table_name} SET {SETWHERE}=? WHERE {WHERE}=? ", (SET, WHEREPLACE))
             SELECT ALL: ("SELECT * FROM {table_name}")
             SELECT ALL CHOICE: ("SELECT {WHERE} FROM {table_name} ")
             SELECT CHOICE: ("SELECT {WHERESELECT} FROM {table_name} WHERE {WHERE}={WHEREPLACE} ") '''


    print("COMMAND STARTED")
    conn = sqlite3.connect(database_name)
    console = conn.cursor()
    com = str(command).upper()
    print(conn, com)
    if com.upper() == "INSERT":
        console.execute(f"INSERT INTO {table_name} VALUES (?,?,?,? )", (INSERT1, INSERT2,INSERT3,INSERT4))
        conn.commit()
        conn.close()
        print(f"""{INSERT1} INSERT {column1}
{INSERT2} INSERT {column2}
{INSERT3} INSERT {column3}
{INSERT4} INSERT {column4}
DATA SUCCESSFULLY INSERTED""")

    elif com.upper() == "DELETE":
        console.execute(f"DELETE FROM {table_name} WHERE {WHERE}")
        conn.commit()
        conn.close()
        print(f""" Data from {table_name} at {WHERE}
SUCCESSFULLY DELETED""")

    elif com.upper() == "UPDATE":
        console.execute(f"UPDATE {table_name} SET {SETWHERE}=? WHERE {WHERE}=? ", (SET, WHEREPLACE))
        conn.commit()
        conn.close()
        print(f"""Data from {table_name} at {WHERE}={WHEREPLACE}
Set {SETWHERE} to {SET}
SUCCESSFULLY UPDATED""")

    elif com.upper() == "SELECT ALL":
        console.execute(f"SELECT * FROM {table_name}")
        conn.commit()
        row = console.fetchall()
        print("")
        print("ALL DATA SELECTED")
        conn.close()
        list = []
        for rows in row:
            list.append(rows[0])
            list.append(rows[1])
            list.append(rows[2])
            list.append(rows[3])
        return list



    elif com.upper() == "SELECT ALL CHOICE":
        console.execute(f"SELECT {WHERE} FROM {table_name} ")
        conn.commit()
        row = console.fetchall()
        list = []
        for rows in row:
            print(rows)
            list.append(rows)
        print("")
        print(f"DATA {WHERE} SELECTED")
        conn.close()
        return list

    elif com.upper() == "SELECT CHOICE":
        console.execute(f"SELECT {WHERESELECT} FROM {table_name} WHERE {WHERE}={WHEREPLACE} ")
        conn.commit()
        raw = str(console.fetchall())
        data = ''
        for i in raw:
            if i not in punctuations:
                data = data + i
        print('')
        print("DATA SELECTED")
        conn.close()
        return data

    else:
        print("ONLY EXCEPT COMMAND (INSERT, UPDATE, DELETE, SELECT ALL, SELECT ALL CHOICE, SELECT CHOICE)", file=sys.stderr)


def db_command5(command, database_name, table_name, column1, column2, column3, column4, column5, INSERT1='', INSERT2='', INSERT3 = '', INSERT4 = '', INSERT5= '', WHERE='', SET='',SETWHERE='', WHEREPLACE='', WHERESELECT = ''):
    '''THIS FUNCTION ONLY SUPPORT 3COLUMN,
             COMMAND=(INSERT, DELETE, UPDATE, SELECT ALL, SELECT ALL CHOICE AND SELECT CHOICE)
             WHERE=(COLUMN NAME)
             SETWHERE=(LOCATE COLUMN NAME TO SET THE DATA)
             WHEREPLACE=(THE DATA AFTER /WHERE/ COMMAND)
             WHERESELECT=(TO SELECTED THE COLUMN A.K.A COLUMN NAME)
             SET=(VALUE TO SET)

            INSERT:("INSERT INTO {table_name} VALUES (?,?)", (INSERT1, INSERT2))
             DELETE: ("DELETE FROM {table_name} WHERE {WHERE}")
             UPDATE: ("UPDATE {table_name} SET {SETWHERE}=? WHERE {WHERE}=? ", (SET, WHEREPLACE))
             SELECT ALL: ("SELECT * FROM {table_name}")
             SELECT ALL CHOICE: ("SELECT {WHERE} FROM {table_name} ")
             SELECT CHOICE: ("SELECT {WHERESELECT} FROM {table_name} WHERE {WHERE}={WHEREPLACE} ") '''


    print("COMMAND STARTED")
    conn = sqlite3.connect(database_name)
    console = conn.cursor()
    com = str(command).upper()
    print(conn, com)
    if com.upper() == "INSERT":
        console.execute(f"INSERT INTO {table_name} VALUES (?,?,?,?,? )", (INSERT1, INSERT2,INSERT3,INSERT4,INSERT5))
        conn.commit()
        conn.close()
        print(f"""{INSERT1} INSERT {column1}
{INSERT2} INSERT {column2}
{INSERT3} INSERT {column3}
{INSERT4} INSERT {column4}
{INSERT5} INSERT {column5}
DATA SUCCESSFULLY INSERTED""")

    elif com.upper() == "DELETE":
        console.execute(f"DELETE FROM {table_name} WHERE {WHERE}")
        conn.commit()
        conn.close()
        print(f""" Data from {table_name} at {WHERE}
SUCCESSFULLY DELETED""")

    elif com.upper() == "UPDATE":
        console.execute(f"UPDATE {table_name} SET {SETWHERE}=? WHERE {WHERE}=? ", (SET, WHEREPLACE))
        conn.commit()
        conn.close()
        print(f"""Data from {table_name} at {WHERE}={WHEREPLACE}
Set {SETWHERE} to {SET}
SUCCESSFULLY UPDATED""")

    elif com.upper() == "SELECT ALL":
        console.execute(f"SELECT * FROM {table_name}")
        conn.commit()
        row = console.fetchall()
        for rows in row:
            print(rows)
        print("")
        print("ALL DATA SELECTED")
        conn.close()
        list = []
        for rows in row:
            list.append(rows[0])
            list.append(rows[1])
            list.append(rows[2])
            list.append(rows[3])
            list.append(rows[4])
        #     data_one = rows[0]
        #     data_two = rows[1]
        #     data_three = rows[2]
        #     data_four = rows[3]
        # return data_one,data_two,data_three,data_four
        return list

    elif com.upper() == "SELECT ALL CHOICE":
        console.execute(f"SELECT {WHERE} FROM {table_name} ")
        conn.commit()
        row = console.fetchall()
        list = []
        for rows in row:
            print(rows)
            list.append(rows)
        print("")
        print(f"DATA {WHERE} SELECTED")
        conn.close()
        return list

    elif com.upper() == "SELECT CHOICE":
        console.execute(f"SELECT {WHERESELECT} FROM {table_name} WHERE {WHERE}={WHEREPLACE} ")
        conn.commit()
        raw = str(console.fetchone())
        data = ''
        for i in raw:
            if i not in punctuations:
                data = data + i
        print('')
        print("DATA SELECTED")
        conn.close()
        return data

    else:
        print("ONLY EXCEPT COMMAND (INSERT, UPDATE, DELETE, SELECT ALL, SELECT ALL CHOICE, SELECT CHOICE)", file=sys.stderr)


def db_command6(command, database_name, table_name, column1, column2, column3, column4, column5, column6, INSERT1='', INSERT2='', INSERT3 = '', INSERT4 = '', INSERT5= '', INSERT6 = '', WHERE='', SET='',SETWHERE='', WHEREPLACE='', WHERESELECT = ''):
    '''THIS FUNCTION ONLY SUPPORT 3COLUMN,
             COMMAND=(INSERT, DELETE, UPDATE, SELECT ALL, SELECT ALL CHOICE AND SELECT CHOICE)
             WHERE=(COLUMN NAME)
             SETWHERE=(LOCATE COLUMN NAME TO SET THE DATA)
             WHEREPLACE=(THE DATA AFTER /WHERE/ COMMAND)
             WHERESELECT=(TO SELECTED THE COLUMN A.K.A COLUMN NAME)
             SET=(VALUE TO SET)

            INSERT:("INSERT INTO {table_name} VALUES (?,?)", (INSERT1, INSERT2))
             DELETE: ("DELETE FROM {table_name} WHERE {WHERE}")
             UPDATE: ("UPDATE {table_name} SET {SETWHERE}=? WHERE {WHERE}=? ", (SET, WHEREPLACE))
             SELECT ALL: ("SELECT * FROM {table_name}")
             SELECT ALL CHOICE: ("SELECT {WHERE} FROM {table_name} ")
             SELECT CHOICE: ("SELECT {WHERESELECT} FROM {table_name} WHERE {WHERE}={WHEREPLACE} ") '''


    print("COMMAND STARTED")
    conn = sqlite3.connect(database_name)
    console = conn.cursor()
    com = str(command).upper()
    print(conn, com)
    if com.upper() == "INSERT":
        console.execute(f"INSERT INTO {table_name} VALUES (?,?,?,?,?,? )", (INSERT1, INSERT2,INSERT3,INSERT4,INSERT5,INSERT6))
        conn.commit()
        conn.close()
        print(f"""{INSERT1} INSERT {column1}
{INSERT2} INSERT {column2}
{INSERT3} INSERT {column3}
{INSERT4} INSERT {column4}
{INSERT5} INSERT {column5}
{INSERT6} INSERT {column6}
DATA SUCCESSFULLY INSERTED""")

    elif com.upper() == "DELETE":
        console.execute(f"DELETE FROM {table_name} WHERE {WHERE}")
        conn.commit()
        conn.close()
        print(f""" Data from {table_name} at {WHERE}
SUCCESSFULLY DELETED""")

    elif com.upper() == "UPDATE":
        console.execute(f"UPDATE {table_name} SET {SETWHERE}=? WHERE {WHERE}=? ", (SET, WHEREPLACE))
        conn.commit()
        conn.close()
        print(f"""Data from {table_name} at {WHERE}={WHEREPLACE}
Set {SETWHERE} to {SET}
SUCCESSFULLY UPDATED""")

    elif com.upper() == "SELECT ALL":
        console.execute(f"SELECT * FROM {table_name}")
        conn.commit()
        row = console.fetchall()
        for rows in row:
            print(rows)
        print("")
        print("ALL DATA SELECTED")
        conn.close()
        list = []
        for rows in row:
            list.append(rows[0])
            list.append(rows[1])
            list.append(rows[2])
            list.append(rows[3])
            list.append(rows[4])
            list.append(rows[5])
        #     data_one = rows[0]
        #     data_two = rows[1]
        #     data_three = rows[2]
        #     data_four = rows[3]
        # return data_one,data_two,data_three,data_four
        return list

    elif com.upper() == "SELECT ALL CHOICE":
        console.execute(f"SELECT {WHERE} FROM {table_name} ")
        conn.commit()
        row = console.fetchall()
        list = []
        for rows in row:
            print(rows)
            list.append(rows)
        print("")
        print(f"DATA {WHERE} SELECTED")
        conn.close()
        return list

    elif com.upper() == "SELECT CHOICE":
        console.execute(f"SELECT {WHERESELECT} FROM {table_name} WHERE {WHERE}={WHEREPLACE} ")
        conn.commit()
        raw = str(console.fetchone())
        data = ''
        for i in raw:
            if i not in punctuations:
                data = data + i
        print('')
        print("DATA SELECTED")
        conn.close()
        return data

    else:
        print("ONLY EXCEPT COMMAND (INSERT, UPDATE, DELETE, SELECT ALL, SELECT ALL CHOICE, SELECT CHOICE)", file=sys.stderr)



# TODO: nanti tambah db_command untuk support 20 column (max)