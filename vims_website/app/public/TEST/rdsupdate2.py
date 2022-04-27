#rdsupdater.py
#!/usr/bin/env python3
import pymysql.cursors

# Open file and grab last item sold
f = open('itemsold.txt', 'r')
item_sold = f.read()
f.close()

# Open file and grab vending sim total
f2 = open('machinetotal.txt', 'r')
simTotal = f2.read()
f2.close()

item_sold2 = str(item_sold)
item_sold3 = item_sold2.strip()

# If Selection is Pepsi
if item_sold3 == "Pepsi" :

        # Open database connection
        cnx = pymysql.connect(user='admin', password='password',
                              host='machines-database.cvczlcshulp9.us-east-2.rds.amazonaws.com',
                              database='machines_database',
                              cursorclass=pymysql.cursors.Cursor,
                              autocommit=True)

        #db = mysql.connector.connect(user='admin', password='password', host=hostname, database='machines_database')

        # prepare a cursor object using cursor() method

        #cursor = db.cursor()
        cursor = cnx.cursor()

        # Prepare SQL queries to UPDATE required records

        db_qty = cursor.execute("SELECT pe_qty FROM machines_database.inventory WHERE machine_id = 100001")
        curr_qty = cursor.fetchone()
        new_qty = (curr_qty[0] - 1)

        qty_update = "UPDATE inventory SET pe_qty = %s WHERE machine_id =100001"
        cursor.execute(qty_update, new_qty)

        money_update = "UPDATE money SET machine_total = %s WHERE machine_id =100001"

        # Execute the SQL command
        cursor.execute(money_update, simTotal)

# If Selection is Diet Pepsi
if item_sold3 == "Diet Pepsi" :

        # Open database connection
        cnx = pymysql.connect(user='admin', password='password',
                              host='machines-database.cvczlcshulp9.us-east-2.rds.amazonaws.com',
                              database='machines_database',
                              cursorclass=pymysql.cursors.Cursor,
                              autocommit=True)

        #db = mysql.connector.connect(user='admin', password='password', host=hostname, database='machines_database')

        # prepare a cursor object using cursor() method

        #cursor = db.cursor()
        cursor = cnx.cursor()

        # Prepare SQL queries to UPDATE required records

        db_qty = cursor.execute("SELECT dp_qty FROM machines_database.inventory WHERE machine_id = 100001")
        curr_qty = cursor.fetchone()
        new_qty = (curr_qty[0] - 1)

        qty_update = "UPDATE inventory SET dp_qty = %s WHERE machine_id =100001"
        cursor.execute(qty_update, new_qty)

        money_update = "UPDATE money SET machine_total = %s WHERE machine_id =100001"

        # Execute the SQL command
        cursor.execute(money_update, simTotal)

# If Selection is Dr Pepper
if item_sold3 == "Dr Pepper" :

        # Open database connection
        cnx = pymysql.connect(user='admin', password='password',
                              host='machines-database.cvczlcshulp9.us-east-2.rds.amazonaws.com',
                              database='machines_database',
                              cursorclass=pymysql.cursors.Cursor,
                              autocommit=True)

        #db = mysql.connector.connect(user='admin', password='password', host=hostname, database='machines_database')

        # prepare a cursor object using cursor() method

        #cursor = db.cursor()
        cursor = cnx.cursor()

        # Prepare SQL queries to UPDATE required records

        db_qty = cursor.execute("SELECT dr_qty FROM machines_database.inventory WHERE machine_id = 100001")
        curr_qty = cursor.fetchone()
        new_qty = (curr_qty[0] - 1)

        qty_update = "UPDATE inventory SET dr_qty = %s WHERE machine_id =100001"
        cursor.execute(qty_update, new_qty)

        money_update = "UPDATE money SET machine_total = %s WHERE machine_id =100001"

        # Execute the SQL command
        cursor.execute(money_update, simTotal)

# If Selection is Mt Dew
if item_sold3 == "Mt Dew" :

        # Open database connection
        cnx = pymysql.connect(user='admin', password='password',
                              host='machines-database.cvczlcshulp9.us-east-2.rds.amazonaws.com',
                              database='machines_database',
                              cursorclass=pymysql.cursors.Cursor,
                              autocommit=True)

        #db = mysql.connector.connect(user='admin', password='password', host=hostname, database='machines_database')

        # prepare a cursor object using cursor() method

        #cursor = db.cursor()
        cursor = cnx.cursor()

        # Prepare SQL queries to UPDATE required records

        db_qty = cursor.execute("SELECT md_qty FROM machines_database.inventory WHERE machine_id = 100001")
        curr_qty = cursor.fetchone()
        new_qty = (curr_qty[0] - 1)

        qty_update = "UPDATE inventory SET md_qty = %s WHERE machine_id =100001"
        cursor.execute(qty_update, new_qty)

        money_update = "UPDATE money SET machine_total = %s WHERE machine_id =100001"

        # Execute the SQL command
        cursor.execute(money_update, simTotal)

# If Selection is Sierra Mist
if item_sold3 == "Sierra Mist" :

        # Open database connection
        cnx = pymysql.connect(user='admin', password='password',
                              host='machines-database.cvczlcshulp9.us-east-2.rds.amazonaws.com',
                              database='machines_database',
                              cursorclass=pymysql.cursors.Cursor,
                              autocommit=True)

        #db = mysql.connector.connect(user='admin', password='password', host=hostname, database='machines_database')

        # prepare a cursor object using cursor() method

        #cursor = db.cursor()
        cursor = cnx.cursor()

        # Prepare SQL queries to UPDATE required records

        db_qty = cursor.execute("SELECT sm_qty FROM machines_database.inventory WHERE machine_id = 100001")
        curr_qty = cursor.fetchone()
        new_qty = (curr_qty[0] - 1)

        qty_update = "UPDATE inventory SET sm_qty = %s WHERE machine_id =100001"
        cursor.execute(qty_update, new_qty)

        money_update = "UPDATE money SET machine_total = %s WHERE machine_id =100001"

        # Execute the SQL command
        cursor.execute(money_update, simTotal)

        # disconnect from server
        cnx.close()
