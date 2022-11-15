import mysql.connector


# DML - data manipulation language
insert_query = "INSERT INTO cats VALUES(8, 'test_cat', 'test_breed', 66)"
update_query = "UPDATE cats SET name='update_cat', breed='update_breed' WHERE cat_id=8"
delete_query = "DELETE FROM cats WHERE cat_id=8"

# DRL - data retrieval language
select_all = "SELECT * FROM cats"

try:
  connection = mysql.connector.connect(host="localhost", 
                                       port=3306, 
                                       user="root", 
                                       passwd="1234", 
                                       database="cat_app")


  cursor = connection.cursor()

  # cursor.execute(insert_query) # INSERT operation
  # connection.commit()

  # cursor.execute(update_query) # UPDATE operation
  # connection.commit()

  # cursor.execute(delete_query) # DELETE operation
  # connection.commit()

  cursor.execute(select_all)
  for row in cursor:
    print(row[0], row[1], row[2], row[3])

  connection.close()
except:
  print("Connection unsuccessful")