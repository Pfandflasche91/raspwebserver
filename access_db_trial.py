import mariadb

db_connection = mariadb.connect(
    user="myuser",
    password="mypassword",
    host="192.168.2.208",
    database="mydb"
)

cursor = db_connection.cursor()

create_table = """
    CREATE TABLE IF NOT EXISTS DHT11(
        id INT AUTO_INCREMENT PRIMARY KEY,
        TEMPERATURE int,
        HUMIDITY int,
        SENSORNR int,
        SENSORLOCATION VARCHAR(100),
        DATETIME DATETIME
    )
"""

insert_data = """
    INSERT INTO DHT11(TEMPERATURE,HUMIDITY,SENSORNR,SENSORLOCATION,DATETIME)
    VALUES
        (25,18,1,'Keller',NOW()),
        (24,19,1,'Keller',NOW())
"""
cursor.execute(create_table)
cursor.execute(insert_data)
db_connection.commit()
cursor.close()