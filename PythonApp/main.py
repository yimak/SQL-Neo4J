import countriesDB

def get_menu():
    horizontal_line = "========================================================"
    menu_title = "MENU".center(50)

    while True:
        print(horizontal_line)
        print(menu_title)
        print(horizontal_line)
        print("""
        1 - View Cities by Country 
        2 - Update City Population 
        3 - Add New Person 
        4 - Delete Person 
        5 - View Countries by population
        6 - Show Twinned Cities 
        7 - Twin with Dublin 
        x - Exit application 
        """)

        choice = input("Choice: ")

        if choice == '1':
            while True:
                country = input("Enter Country : ")

                countries = countriesDB.get_countries(country)
                for i in range(0, len(countries), 2):
                    for country_info in countries[i:i+2]:
                        print(country_info["country.name"], "|", country_info["city.name"], "|", country_info["city.district"], "|", country_info["country.population"])
                    
                    user_input = input("-- Quit (q)--")
                    if user_input.lower() == 'q':
                        break
                #use twice to return to choice 
                if user_input.lower() == 'q':
                    break
        
        elif choice == '2':
          
          while True:
           city_id = int(input("Enter city ID : "))
           cities = countriesDB.get_city_details(city_id)
           
           if cities:
            for city_data in cities:
                print(city_data["id"], "|", city_data["name"], "|", city_data["countrycode"], "|", city_data["population"], "|", city_data["latitude"], "|", city_data["longitude"])
                
                while True:
                    option = input("[I]ncrease/[D]crease Population: ")
                    if option.upper() == 'I':
                        increase_amount = int(input("Enter Population Increase: ")) 
                        print("\n")
                        new_population = city_data["population"] + increase_amount
                        countriesDB.update_population(city_id,new_population)
                        break
                        
                    elif option.upper() == 'D':
                        decrease_amount = int(input("Enter Population Decrease: ")) 
                        print("\n")
                        new_population = city_data["population"] - decrease_amount
                        countriesDB.update_population(city_id, new_population)
                        break
           else:
            print("No city found with ID = ", city_id, "\n")

           
        elif choice == '3':
            space =         "-----------------"
            person_id = print("Add New Person")   
            print(space)
            add_personid = int(input("ID : "))
            add_personname = input("Name : ")
            add_age = int(input("Age: "))
            add_salary = float(input("Salary : "))
            add_city = int(input("City : "))
            new_person = {'personID' : add_personid, 'personname': add_personname, 'age': add_age, 'salary': add_salary, 'city': add_city}
            countriesDB.add_new_person(new_person)
        
#in this part I had to change the code again: in point 4.4.4 we are asked to delete a row regardless if "city" is NULL, however, in 4.4.4.1 personID should NOT be deleted if city is not NULL          
        elif choice == '4':
            while True:
                delete_person_id = int(input("Enter ID of Person to Delete : "))                
                delete = countriesDB.delete_person(delete_person_id)
                #if city is not null
                if delete:
                    print(f"Error: Can't delete Person ID: {delete_person_id}. He/she has visited cities.")
                #if city is null
                else:
                    print(f"Person ID: {delete_person_id} deleted.")                 
                break
                       
                   
        elif choice == '5':
            print("Countries by Population")
            print("-----------------------")
            while True: #als block benutzen
                operator = input("Enter < > or = : ")
                if operator in ['<', '>', '=']:
                    break
                    
            population_number = int(input("Enter population : "))
            if operator == '<':
                countries = countriesDB.countries_population(population_number,operator) 
                if countries:
                    for country in countries:
                        print(country["code"], "|", country["name"], "|", country["continent"], "|" , country["population"])
                else:
                    return
            
            elif operator == '=':
                countries = countriesDB.countries_population(population_number,operator)
                if countries:
                    for country in countries:
                        print(country["code"], "|", country["name"], "|", country["continent"], "|" , country["population"])
                else:
                    return
            
            elif operator == '>':
                countries = countriesDB.countries_population(population_number,operator)
                if countries:
                    for country in countries:
                        print(country["code"], "|", country["name"], "|", country["continent"], "|" , country["population"])
                else:
                    return
            
            else:
                break
                               
        elif choice == '6':
            show_twinned_cities()
        elif choice == '7':
            twin_with_dublin()
        elif choice.lower() == 'x':
            print("Exiting application.")
            break
    
def main():
    get_menu()
    
if __name__ ==  '__main__':
    main()
    
#6 & 7 missing