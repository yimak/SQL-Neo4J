#connect to sql

import pymysql

conn = None

def connect():
    global conn
    conn = pymysql.connect(host="localhost", user="root", password="root", db="appdbproj", cursorclass=pymysql.cursors.DictCursor)

def get_countries(country):
    if not conn:
        connect()
    query = "SELECT country.name AS 'country.name', country.population AS 'country.population', city.name AS 'city.name', city.district AS 'city.district' FROM country JOIN city ON country.code = city.countrycode WHERE country.name = %s" 
    cursor = conn.cursor()
    cursor.execute(query, (country,))
    x = cursor.fetchall()
    return x

def get_city_details(city_id):
    if not conn:
        connect()
    query = "SELECT city.id, city.name, city.countrycode, city.population, city.latitude, city.longitude FROM city WHERE city.id = %s"
    cursor = conn.cursor()
    cursor.execute(query, (city_id,))
    city = cursor.fetchall()
    return city

def update_population(city_id, new_population):
    if not conn:
        connect()
    try:
        with conn.cursor() as cursor:
            update_query = "UPDATE city SET population = %s WHERE id = %s"
            cursor.execute(update_query, (new_population, city_id))
            conn.commit()
    except Exception as e:
        print("Error occurred while updating population:", e)
    finally:
        pass



def add_new_person(new_person):
    if not conn:
        connect()
    try:
        with conn.cursor() as cursor:
            #check if personID already exists
            unique_personid = "SELECT 1 FROM person WHERE personID = %s"
            cursor.execute(unique_personid, (new_person['personID'],))
            existing_personid = cursor.fetchone()
            if existing_personid:
                print(f"Error: PersonID: {new_person['personID']} already exists")           
            
            elif not existing_personid:
            #check if city exists
                unique_city = "SELECT 1 FROM person WHERE city = %s"
                cursor.execute(unique_city, (new_person['city'],))
                existing_city = cursor.fetchone()
                if not existing_city:
                    print(f"Error: City ID: {new_person['city']} does not exist")
            
            query = "SELECT person.city FROM person JOIN hasvisitedcity ON person.city = hasvisitedcity.cityID WHERE person.city = %s"
            cursor.execute(query, (new_person,))
            existing_city = cursor.fetchone()
            if not existing_city:
            #\n not working
                print(f"\nError: City ID: {new_person['city']} does not exist\n") 
                return
            
            else:
                insert_query = "INSERT INTO person (personID, personname, age, salary, city) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(insert_query, (new_person['personID'], new_person['personname'], new_person['age'], new_person['salary'], new_person['city']))
                conn.commit()
    except pymysql.Error as e:
       pass


def delete_person(delete_person_id):
    try:
        if not conn:
            connect()
        #check if the person exists
        query_check = "SELECT 1 FROM person WHERE personid = %s"
        cursor = conn.cursor()
        cursor.execute(query_check, (delete_person_id,))
        existing_person = cursor.fetchone()
        
        if not existing_person:
            return False
        
        #if person exists, proceed with deletion
        query_delete = "DELETE FROM person WHERE personid = %s AND city IS NULL"
        cursor.execute(query_delete, (delete_person_id,))
        conn.commit()
        return True
    #catch errors related to interaction with SQL table
    except pymysql.Error as e:
        print(e)
        return False
        


def countries_population(population, operator):
    try: 
        if not conn:
            connect()
        query = "SELECT code, name, continent, population FROM country WHERE"
        if operator == '<':
            query += " population < %s"
        elif operator == '=':
            query += " population = %s"
        elif operator == '>':
            query += " population > %s"
        else:
            return None
        cursor = conn.cursor()
        cursor.execute(query, (population,))
        countries = cursor.fetchall()
        return countries 
    except pymysql.Error as e:
        print(e)
        return None

        
        

