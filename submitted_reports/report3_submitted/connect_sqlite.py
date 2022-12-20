import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('test.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# CLINIC ---------------------------------------------------------------------------------------
# String variable for passing queries to cursor
query = """
    CREATE TABLE clinic(
    clinicNo INT,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(100) NOT NULL,
    telephoneNo VARCHAR(20) NOT NULL,
    managerNo INT NOT NULL,
    PRIMARY KEY(clinicNo)
    );
    """

# # Execute query, the result is stored in cursor
# cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO clinic
    VALUES (1, "Station Road Clinic", "Station Road, Wellington, 21342", "456-456-4564", 1);
    """
cursor.execute(query)
query = """
    INSERT INTO clinic
    VALUES (2, "Awesome Road Clinic", "Awesome Road, Coral Gables, 54322", "305-654-2423", 2);
    """
cursor.execute(query)
query = """
    INSERT INTO clinic
    VALUES (3, "Evil Road Clinic", "Evil Road, Coral Gables, 54322", "305-456-5555", 3);
    """
cursor.execute(query)
query = """
    INSERT INTO clinic
    VALUES (4, "The Okay Clinic", "Okay Road, Coral Gables, 54322", "305-543-3333", 4);
    """
cursor.execute(query)
query = """
    INSERT INTO clinic
    VALUES (5, "The Thornton Clinic", "Thornton, Highfields, 67854", "543-456-2221", 5);
    """
cursor.execute(query)

# # Select data
query = """
    SELECT * 
    FROM clinic
    WHERE clinicNo = 1;
    """
cursor.execute(query)
clinic_column_names = [row[0] for row in cursor.description]
clinic_table_data = cursor.fetchall()
df = pd.DataFrame(clinic_table_data, columns=clinic_column_names)
print(df)
print(df.columns)
query = """
    SELECT name, telephoneNo 
    FROM clinic
    WHERE clinicNo = 2;
    """
cursor.execute(query)
clinic_column_names = [row[0] for row in cursor.description]
clinic_table_data = cursor.fetchall()
df = pd.DataFrame(clinic_table_data, columns=clinic_column_names)
print(df)
print(df.columns)

query = """
    SELECT name, managerNo 
    FROM clinic
    WHERE managerNo = 3 OR managerNo = 4;
    """
cursor.execute(query)
clinic_column_names = [row[0] for row in cursor.description]
clinic_table_data = cursor.fetchall()
df = pd.DataFrame(clinic_table_data, columns=clinic_column_names)
print(df)
print(df.columns)

query = """
    SELECT name, address 
    FROM clinic
    WHERE address LIKE "%Road%";
    """
cursor.execute(query)
clinic_column_names = [row[0] for row in cursor.description]
clinic_table_data = cursor.fetchall()
df = pd.DataFrame(clinic_table_data, columns=clinic_column_names)
print(df)
print(df.columns)

query = """
    SELECT name, telephoneNo, managerNo 
    FROM clinic
    WHERE telephoneNo LIKE "305%";
    """
cursor.execute(query)
clinic_column_names = [row[0] for row in cursor.description]
clinic_table_data = cursor.fetchall()
df = pd.DataFrame(clinic_table_data, columns=clinic_column_names)
print(df)
print(df.columns)




# STAFF--------------------------------------------------------------------------------------------------------------
# String variable for passing queries to cursor
query = """
    CREATE TABLE staff(
    staffNo INT,
    firstName VARCHAR(100) NOT NULL,
    lastName VARCHAR(100) NOT NULL,
    street VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    zip INT(9) NOT NULL,
    telephoneNo VARCHAR(20) NOT NULL,
    DOB VARCHAR(10) NOT NULL,
    position VARCHAR(20) NOT NULL,
    salary INT(10) NOT NULL,
    clinicNo INT NOT NULL,
    PRIMARY KEY(staffNo)
    );
    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO staff
    VALUES (1, "Bob", "Echeer", "Pearson Street", "Miami", "USA", 12345, "305-456-4444", "06-06-2002", "Helper", 4000, 1);

    """
cursor.execute(query)
query = """
    INSERT INTO staff
    VALUES (2, "Kyle", "Smith", "Mahoney Road", "Orlando", "USA", 23452, "123-765-4356", "29-06-2001", "Helper", 40000, 2);

    """
cursor.execute(query)
query = """
    INSERT INTO staff
        VALUES (3, "James", "Smith", "Random Street", "Miami", "USA", 23456, "305-345-2111", "23-11-2000", "Admin", 6000, 3);
    """
cursor.execute(query)
query = """
    INSERT INTO staff
    VALUES (4, "Bob", "Echeer", "Thornton Street", "Miami", "USA", 12345, "456-242-7654", "01-06-1980", "Surgeon", 3000, 4);
    """
cursor.execute(query)
query = """
    INSERT INTO staff
    VALUES (5, "Bob", "Smith", "Desford Street", "Miami", "USA", 4364, "305-567-5346", "10-06-1992", "Surgeon", 10, 5);
    """
cursor.execute(query)
    
    
#     """

# # Select data
query = """
        SELECT staffNo, firstName, lastName, position, salary
    FROM staff
    WHERE city = "Miami" AND position = "Surgeon";
    """
cursor.execute(query)
staff_column_names = [row[0] for row in cursor.description]
staff_table_data = cursor.fetchall()
df = pd.DataFrame(staff_table_data, columns=staff_column_names)
print(df)
print(df.columns)

query = """
        SELECT staffNo, firstName, lastName, salary
    FROM staff
    WHERE salary > 5000;
    """
cursor.execute(query)
staff_column_names = [row[0] for row in cursor.description]
staff_table_data = cursor.fetchall()
df = pd.DataFrame(staff_table_data, columns=staff_column_names)
print(df)
print(df.columns)

query = """
        SELECT *
    FROM staff
    WHERE city NOT LIKE "Miami";
    """
cursor.execute(query)
staff_column_names = [row[0] for row in cursor.description]
staff_table_data = cursor.fetchall()
df = pd.DataFrame(staff_table_data, columns=staff_column_names)
print(df)
print(df.columns)

query = """
        SELECT *
    FROM staff
    WHERE city NOT LIKE "Miami";
    """
cursor.execute(query)
staff_column_names = [row[0] for row in cursor.description]
staff_table_data = cursor.fetchall()
df = pd.DataFrame(staff_table_data, columns=staff_column_names)
print(df)
print(df.columns)

query = """
        SELECT staffNo, lastName, city, zip, telephoneNo
    FROM staff
    WHERE telephoneNo LIKE "305%";
    """
cursor.execute(query)
staff_column_names = [row[0] for row in cursor.description]
staff_table_data = cursor.fetchall()
df = pd.DataFrame(staff_table_data, columns=staff_column_names)
print(df)
print(df.columns)



















# PET OWNER-------------------------------------------------------------------------------------------------------
# String variable for passing queries to cursor
query = """
    CREATE TABLE petOwner(
    ownerNo INT,
    firstName VARCHAR(100) NOT NULL,
    lastName VARCHAR(100) NOT NULL,
    street VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    zip INT(9) NOT NULL,
    telephoneNo VARCHAR(20) NOT NULL,
    clinicNo INT NOT NULL,
    PRIMARY KEY(ownerNo)
    );
    """

# Execute query, the result is stored in cursor
#cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO petOwner
    VALUES (1, "Amy", "Cutz", "Hay", "Miami", "USA", 34535, "305-567-5346", 1);
    """
cursor.execute(query)
query = """
    INSERT INTO petOwner
    VALUES (2, "Leo", "Amer", "Markfield", "Miami", "USA", 54370, "305-888-6667", 2);
    """
cursor.execute(query)
query = """
    INSERT INTO petOwner
    VALUES (3, "Neo", "Jones", "Desford", "Miami", "USA", 83768, "305-747-7564", 3);
    """
cursor.execute(query)
query = """
    INSERT INTO petOwner
    VALUES (4, "Angel", "Smith", "Bagworth", "Leicester", "USA", 48653, "44-654-1111", 4);
    """
cursor.execute(query)
query = """
    INSERT INTO petOwner
    VALUES (5, "John", "Smith", "Desford", "Miami", "USA", 54363, "305-123-4321", 5);
    """
cursor.execute(query)
    
    
    
# Select data
query = """
    SELECT *
    FROM petOwner
    WHERE city = "Miami"
    """
cursor.execute(query)
petOwner_column_names = [row[0] for row in cursor.description]
petOwner_table_data = cursor.fetchall()
df = pd.DataFrame(petOwner_table_data, columns=petOwner_column_names)
print(df)
print(df.columns)
query = """
    SELECT *
    FROM petOwner
    WHERE telephoneNo LIKE "305%"
    """
cursor.execute(query)
petOwner_column_names = [row[0] for row in cursor.description]
petOwner_table_data = cursor.fetchall()
df = pd.DataFrame(petOwner_table_data, columns=petOwner_column_names)
print(df)
print(df.columns)
query = """
    SELECT *
    FROM petOwner
    WHERE clinicNo = 1;
    """
cursor.execute(query)
petOwner_column_names = [row[0] for row in cursor.description]
petOwner_table_data = cursor.fetchall()
df = pd.DataFrame(petOwner_table_data, columns=petOwner_column_names)
print(df)
print(df.columns)
query = """
    SELECT *
    FROM petOwner
    """
cursor.execute(query)
petOwner_column_names = [row[0] for row in cursor.description]
petOwner_table_data = cursor.fetchall()
df = pd.DataFrame(petOwner_table_data, columns=petOwner_column_names)
print(df)
print(df.columns)
query = """
    SELECT *
    FROM petOwner
    """
cursor.execute(query)
petOwner_column_names = [row[0] for row in cursor.description]
petOwner_table_data = cursor.fetchall()
df = pd.DataFrame(petOwner_table_data, columns=petOwner_column_names)
print(df)
print(df.columns)



# PET -----------------------------------------------------------------------------------------------------
# String variable for passing queries to cursor
query = """
    CREATE TABLE pet(
    petNo INT,
    name VARCHAR(100) NOT NULL,
    DOB VARCHAR(10) NULL,
    species VARCHAR(100) NULL,
    breed VARCHAR(100) NULL,
    color VARCHAR(100) NOT NULL,
    ownerNo INT NOT NULL,
    PRIMARY KEY(petNo)
    );
    """
cursor.execute(query)


# Insert row into table
query = """
    INSERT INTO pet
    VALUES (1, "Ruby", "04-06-2004", "Cat", "Ninja Cat", "Black", 1);
    """
cursor.execute(query)
query = """
    INSERT INTO pet
    VALUES (2, "Jedi", "21-09-2009", "Cat", "Fat Cat", "Black and White", 1);
    """
cursor.execute(query)
query = """
    INSERT INTO pet
    VALUES (3, "Maggie", "04-03-2002", "Dog", "King Charles Cavalier Spaniel", "Brown", 2);
    """
cursor.execute(query)
query = """
    INSERT INTO pet
    VALUES (4, "Elvis", "24-01-2017", "Cat", "Fat Cat", "Black", 3);
    """
cursor.execute(query)
query = """
    INSERT INTO pet
    VALUES (5, "Albert", "04-06-2016", "Snake", "Python", "Pink", 4);
    """
cursor.execute(query)
query = """
    INSERT INTO pet
    VALUES (6, "Roger", "10-11-2021", "Turtle", "Fat Turtle", "Green", 5);
    """
cursor.execute(query)

    
# # Select data
query = """
    SELECT *
    FROM pet
    WHERE species = "Cat";
"""
cursor.execute(query)
pet_column_names = [row[0] for row in cursor.description]
pet_table_data = cursor.fetchall()
df = pd.DataFrame(pet_table_data, columns=pet_column_names)
print(df)
print(df.columns)
query = """
    SELECT * 
    FROM pet
    WHERE ownerNo = 1;
"""
cursor.execute(query)
pet_column_names = [row[0] for row in cursor.description]
pet_table_data = cursor.fetchall()
df = pd.DataFrame(pet_table_data, columns=pet_column_names)
print(df)
print(df.columns)
query = """
    SELECT * 
    FROM pet
    WHERE species LIKE "Fat%";
"""
cursor.execute(query)
pet_column_names = [row[0] for row in cursor.description]
pet_table_data = cursor.fetchall()
df = pd.DataFrame(pet_table_data, columns=pet_column_names)
print(df)
print(df.columns)
query = """
    SELECT petNo, name, ownerNo 
    FROM pet
    WHERE name LIKE "R%";
"""
cursor.execute(query)
pet_column_names = [row[0] for row in cursor.description]
pet_table_data = cursor.fetchall()
df = pd.DataFrame(pet_table_data, columns=pet_column_names)
print(df)
print(df.columns)
query = """
    SELECT petNo, name, ownerNo 
    FROM pet
    WHERE name LIKE "R%";
"""
cursor.execute(query)
pet_column_names = [row[0] for row in cursor.description]
pet_table_data = cursor.fetchall()
df = pd.DataFrame(pet_table_data, columns=pet_column_names)
print(df)
print(df.columns)




# EXAMINATION -----------------------------------------------------------------------------------------------------
# String variable for passing queries to cursor
query = """
    CREATE TABLE exam(
    examNo INT,
    procedureNo INT NOT NULL,
    dateSeen VARCHAR(10) NOT NULL,
    petNo INT NOT NULL,
    staffNo INT NOT NULL,
    PRIMARY KEY(examNo)
    );
    """
cursor.execute(query)


# Insert row into table
query = """
    INSERT INTO exam
    VALUES (1, 1, "10-02-2021", 1, 4);
"""
cursor.execute(query)
query = """
    INSERT INTO exam
    VALUES (2, 2, "10-03-2022", 1, 4);
"""
cursor.execute(query)
query = """
    INSERT INTO exam
    VALUES (3, 1, "17-04-2022", 2, 4);
"""
cursor.execute(query)
query = """
    INSERT INTO exam
    VALUES (4, 1, "07-08-2022", 3, 5);
"""
cursor.execute(query)
query = """
    INSERT INTO exam
    VALUES (5, 3, "01-09-2022", 4, 5);
"""
cursor.execute(query)
query = """
    INSERT INTO exam
    VALUES (6, 4, "19-10-2022", 4, 4);
"""
cursor.execute(query)
query = """
    INSERT INTO exam
    VALUES (7, 1, "29-10-2022", 5, 5);
"""
cursor.execute(query)

    

# Select data
query = """
    SELECT *
    FROM exam
    WHERE staffNo = 4;
"""
cursor.execute(query)
exam_column_names = [row[0] for row in cursor.description]
exam_table_data = cursor.fetchall()
df = pd.DataFrame(exam_table_data, columns=exam_column_names)
print(df)
print(df.columns)
query = """
        SELECT *
    FROM exam
    WHERE petNo = 1;
"""
cursor.execute(query)
exam_column_names = [row[0] for row in cursor.description]
exam_table_data = cursor.fetchall()
df = pd.DataFrame(exam_table_data, columns=exam_column_names)
print(df)
print(df.columns)
query = """
        SELECT *
    FROM exam
    WHERE procedureNo = 1;
"""
cursor.execute(query)
exam_column_names = [row[0] for row in cursor.description]
exam_table_data = cursor.fetchall()
df = pd.DataFrame(exam_table_data, columns=exam_column_names)
print(df)
print(df.columns)
query = """
        SELECT *
    FROM exam
    WHERE dateSeen LIKE "%2022";
"""
cursor.execute(query)
exam_column_names = [row[0] for row in cursor.description]
exam_table_data = cursor.fetchall()
df = pd.DataFrame(exam_table_data, columns=exam_column_names)
print(df)
print(df.columns)
query = """
        SELECT *
    FROM exam
    WHERE dateSeen LIKE "%2021";
"""
cursor.execute(query)
exam_column_names = [row[0] for row in cursor.description]
exam_table_data = cursor.fetchall()
df = pd.DataFrame(exam_table_data, columns=exam_column_names)
print(df)
print(df.columns)


# PROCEDURE ------------------------------------------------------------------------------------------------------------------------------
# String variable for passing queries to cursor
query = """
    CREATE TABLE procedure(
    procedureNo INT,
    chiefComplaint VARCHAR(100) NOT NULL,
    description VARCHAR(100) NOT NULL,
    actionsTaken VARCHAR(100) NOT NULL,
    PRIMARY KEY(procedureNo)
    );
    """
cursor.execute(query)


# Insert row into table
query = """
    INSERT INTO procedure
    VALUES (1, "Pain during pregnancy", "Test for pain on abdomen", "C-Section");
"""
cursor.execute(query)
query = """
    INSERT INTO procedure
    VALUES (2, "Bladder Infection", "Physical test for inflammation.", "Fluid through an IV + catheter.");
"""
cursor.execute(query)
query = """
    INSERT INTO procedure
    VALUES (3, "Bee sting", "Inflammed, swollen, limping", "Anti itch cream");
"""
cursor.execute(query)
query = """
    INSERT INTO procedure
    VALUES (4, "Neutering", "n/a", "Chop off bits and bobs.");
"""
cursor.execute(query)


# # Select data
query = """
    SELECT *
    FROM procedure
    """
cursor.execute(query)
procedure_column_names = [row[0] for row in cursor.description]
procedure_table_data = cursor.fetchall()
df = pd.DataFrame(procedure_table_data, columns=procedure_column_names)
print(df)
print(df.columns)



# FOREIGN KEYS---------------------------------------
# String variable for passing queries to cursor
# query = """
#     UPDATE clinic(

#     FOREIGN KEY(managerNo)
#         REFERENCES staff(staffNo)
#             ON UPDATE CASCADE
#             ON DELETE SET NULL;
#     );
# """
# cursor.execute(query)
# query = """
#     UPDATE TABLE staff(

#     FOREIGN KEY(clinicNo)
#         REFERENCES clinic(clinicNo)
#             ON UPDATE CASCADE
#             ON DELETE NO ACTION;
#     );
# """
# cursor.execute(query)
# query = """
#     UPDATE TABLE exam(

#     FOREIGN KEY(procedureNo)
#         REFERENCES procedure(procedureNo)
#             ON UPDATE CASCADE
#             ON DELETE NO ACTION;
#     );
# """
# cursor.execute(query)
# query = """
#     UPDATE TABLE exam(

#     FOREIGN KEY(petNo)
#         REFERENCES pet(petNo)
#             ON UPDATE NO ACTION
#             ON DELETE CASCADE;
#     );
# """
# cursor.execute(query)
# query = """
#     UPDATE TABLE exam(

#     FOREIGN KEY(staffNo)
#         REFERENCES staff(staffNo)
#             ON UPDATE NO ACTION
#             ON DELETE NO ACTION;
#     );
# """
# cursor.execute(query)
# query = """
#     UPDATE TABLE pet(

#     FOREIGN KEY(ownerNo)
#         REFERENCES petOwner(ownerNo)
#             ON UPDATE CASCADE
#             ON DELETE NO ACTION;
#     );
# """
# cursor.execute(query)
# query = """
#     UPDATE TABLE petOwner(

#     FOREIGN KEY(clinicNo)
#         REFERENCES clinic(clinicNo)
#             ON UPDATE CASCADE
#             ON DELETE NO ACTION;
#     );
#     """
# cursor.execute(query)


# Example to extract a specific column
# print(df['name'])


# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()
