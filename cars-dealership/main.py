import csv
import os
from car import Car
from database import (initialize_database, import_cars, add_car, filter_cars, get_car_by_id, update_car, delete_car, database_sumary, get_all_cars,
                      search_cars, get_all_cars_by_year_asc, get_all_cars_by_year_desc, get_all_cars_by_price_desc, get_all_cars_by_price_asc)

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():    
    print("╔══════════════════════════════════════════╗")
    print("║     🚗 Car Dealership Manager            ║")
    print("╚══════════════════════════════════════════╝")


def show_menu():
    print("\n" + "="*40)
    print("   🚗  CAR DEALERSHIP MANAGER")
    print("="*40)
    print("1. ✏️  Add a new Car")
    print("2. 📜 View all Cars")
    print("3. 📖 Update a specific post")
    print("4. 🗑️  Delete a Car")
    print("5. 🔎 Search Cars")
    print("6. 📜 Statistics")
    print("7. 💾 Export in csv")
    print("8. 🏛️ Exit")      
    choice = input("Selected what you want to do: 1/2/3/4/5/6/7/8:    ")
    return choice


def add_car_flow():
    # Add a new car
    clear_screen()
    print_header()
    print("\n✏️  CREATE A NEW CAR")
    print("-"*30)
    
    check = True
    while check:
        make = input("Manufacturer Name: ").strip()
        if not make:
            print("\n❌ Manufacturer can't be empty !")
            input("\nPress Enter to restart...")
            continue
        
        model = input("Model name: ").strip()      
        if not model:
            print("\n❌ Model can't be empty !")
            input("\nPress Enter to restart...")
            continue

        year = input("Year of build: ")
        if not year:
            print("\n❌ year can not be empty")
            input("\nPress Enter to restart...")
            continue
        elif not year.isdigit():
            print("\n❌ year should be a number bigger than zero like 1980 !")
            input("\nPress Enter to restart...")
            continue
                        

        price = input("Enter the price: ")
        if not price:
            print("\n❌ the price can not be empty !")
            input("\nPress Enter to restart...")
            continue
        elif not price.isdigit():
            print("\n❌ we need as price, a positive number !")
            input("\nPress Enter to restart...")
            continue

        mileage = input("Enter the actual mileage: ")
        if not mileage:
            print("\n❌ Mileage can not be empty, we need a value")
            input("\nPress Enter to restart...")
            continue           
        elif not mileage.isdigit():
            print("\n❌ we need as mileage, a number >= 0 !")
            input("\nPress Enter to restart...")
            continue
                
        new_car = Car(make, model, year, price, mileage) 
        try:
            add_car(new_car)
            print(f"✅  {new_car} successfyly added")
            input("Press Enter to restart... ")
            check = False
        except ValueError:
            print("\n❌ something wrong, car was not add!")



def view_all_cars_flow():
    check_database = database_sumary()
    
    if check_database[0] <= 0:
        print("❌ sorry, the database is empty. You need to create cars first")
    else:
        clear_screen()
        print_header()
        print("\n📜  LIST OFF AVAILABLE CARS")
        print("-"*30)
        print("1- View all cars sorted by price Low -> High")
        print("2- View all cars sorted by price High -> Low")
        print("3- View all cars sorted by year (Acendants)")
        print("4- View all cars sorted by year (Descendants)")
        sort_choice = input("Select how you want to see the list of cars(1/2/3/4):     ")

        #check = True
        # while check:
        # if sort_choice in range(1, 7):
                #     check = False
        if not sort_choice.isdigit():
            print("you should enter a number")
        else: 
            print(f"your choice is {sort_choice}")  

            if int(sort_choice) == 1:     
                clear_screen()
                print_header()
                print("\n✏️  LIST OFF AVAILABLE CARS sorted by price Low -> High")   
                print("-"*70)
                print("\n")
                cars_price = get_all_cars_by_price_asc()            
                for car in cars_price:
                    print(car)
        
                input("Press Enter to continue... ")
                        
            elif int(sort_choice) == 2:     
                clear_screen()
                print_header()
                print("\n✏️  LIST OFF AVAILABLE CARS sorted by price High -> Low")   
                print("-"*70)
                print("\n")
                cars_price = get_all_cars_by_price_desc()            
                for car in cars_price:
                    print(car)
        
                input("\nPress Enter to continue... ")
            
            elif int(sort_choice) == 3:     
                clear_screen()
                print_header()
                print("\n✏️  LIST OFF AVAILABLE CARS sorted by year Ascendant")   
                print("-"*70)
                print("\n")
                cars_year = get_all_cars_by_year_asc()            
                for car in cars_year:
                    print(car)
        
                input("\nPress Enter to continue... ")
            
            elif int(sort_choice) == 4:     
                clear_screen()
                print_header()
                print("\n✏️  LIST OFF AVAILABLE CARS sorted by year Descendant")    
                print("-"*70)
                print("\n")
                cars_year = get_all_cars_by_year_desc()            
                for car in cars_year:
                    print(car)
        
                input("\nPress Enter to continue... ")   
            
            else:
                print("❌ Sorry, you should selecte number between 1-4")
                input("\nPress Enter to continue... ")
        

def update_car_flow():
    clear_screen()
    print_header()
    print("\n✏️  UPDATE SPECIFIC CAR")
    print("-"*30)
    id = int(input("Enter ID of the car you want to update:  "))
    found_car = get_car_by_id(id)
    if found_car == None:
        print("❌ Sorry, this ID car does't exist")
        
    else:
        print(found_car)
        input("Press Enter and give updated value if applicable for each field... ")
        
        if new_make := input(f"Make [{found_car.make}]: "): found_car.make = new_make
        if new_model := input(f"Model [{found_car.model}]: "): found_car.model = new_model
        if new_year := input(f"Year [{found_car.year}]: "): found_car.year = new_year
        if new_price := input(f"Price [{found_car.price}]: "): found_car.price = new_price
        if new_mileage := input(f"Mileage [{found_car.mileage}]: "): found_car.mileage = new_mileage
        
        try:
            update_car(found_car)
            print(f"✅  {found_car} successfyly updated")
            input("Press Enter to continue... ")
            
        except ValueError:
            print("\n❌ something wrong, car was not updated!")


def delete_car_flow():
    clear_screen()
    print_header()
    print("\n✏️  DELETE SPECIFIC CAR")
    print("-"*30)
    id = int(input("Enter ID of the car you want to update:  "))
    found_car = get_car_by_id(id)
    if found_car == None:
        print("❌ Sorry, this ID car does't exist")
        return False 
    else:
        print(found_car)
        choice = input("Are you sure Y/N:   ")

        if choice.lower() == "y":            
            print(f"✅  {found_car} successfyly DELETED")
            delete_car(id)
            return True
            input("Press Enter to continue... ")
        else:
           return False 


def search_cars_flow():
    clear_screen()
    print_header()
    print("\n✏️  SEARCH SPECIFIC(S) CAR")
    print("-"*30)
    print("\n1 - Use standard search by give a term to search")
    print("\n2- Filter cars by price under a given price")
    choice = input("]nEnter your choice (1/2):   ")

    if not choice.isdigit() and not choice in range(1, 2):
        print("You must enter a number 1/2")
        input("\nPress Enter to continue... ")
    else:       
        if int(choice) == 1:
            keyword = input("Which term would you like to use use for SEARCH:    ")
            if not keyword:
                print("❌ The term can not be empty!")
            else:
                result = search_cars(keyword)
                print(f"We found {len(result)} car(s) with this -- : {keyword} : TERM")
                for item in result:
                    print(item)
            
            input("\nPress Enter to continue... ")
        
        elif int(choice) == 2:
            price = input("Enter the maximum price of cars you need:  ")            
            if not price:
                print("Sorry, you should add a float number -- we use $ currency ")
            else:
               
                match_cars = filter_cars(float(price))
                
                for car in match_cars:
                    print(car)
                
                input("\nPress Enter to continue... ")


    


def statistics():
    database_stats = database_sumary()
    
    if database_stats[0] <= 0:
        print("❌ sorry, the database is empty. You need to create cars first")
    else:
        clear_screen()
        print_header()
        print("\n📜  CARS STATISTICS FROM DATABASE  ")
        print("-"*30)
        print(f"\n Total cars in inventory: {database_stats[0]}")
        print(f"\n Average price:   {database_stats[1]:,}")
        print(f"\nMost common make: {database_stats[2][0]}")
        input("\nPress Enter to continue... ")



def export_csv():  
    
    cars = get_all_cars()
    
       
    clear_screen()
    print_header()
    print("\n✏️  SAVE INVENTORY CARS IN CSV FILE ")
    print("-"*30)
    print("\n")
    data_rows = []
    fields = ["id", "make", "model", "year", "price", "mileage"]   

    for car in cars:              
        print (car) 
        data_rows.append([car.id, car.make, car.model, car.year, car.price, car.mileage])     
       
           
    # Open file with newline='' to prevent extra blank rows
    with open('cars_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        writer.writerows(data_rows)  # Writes all rows at once

    print(f"✅ Cars inventory successfyly saved in file: cars_data.csv")
    input("\nPress Enter to continue... ")



def main():
    initialize_database()  # Always call this first!
    import_cars()          # Load sample data if the table is empty
    
    while True:
        clear_screen()
        print_header()
        choice = show_menu()
        
        if choice == "1":
            add_car_flow()
        elif choice == "2":
            # your code here
            view_all_cars_flow()
        # ... continue for all options
        elif choice == "3":
            # your code here
            update_car_flow()
        elif choice == "4":
            # your code here
            delete_car_flow()
        elif choice == "5":
            # your code here
            search_cars_flow()
        elif choice == "6":
            # your code here
            statistics()
        elif choice == "7":
            # your code here
            export_csv()
            
        elif choice == "8":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter 1/2/3/4/5/6:   ")




if __name__ == "__main__":
    main()