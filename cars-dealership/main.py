from datetime import datetime
import os
from car import Car
from database import (initialize_database, import_cars, add_car, get_all_cars, get_car_by_id, update_car, delete_car, search_cars)

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
    print("6. 🚪 Exit")      
    choice = input("Selected what you want to do: 1/2/3/4/5/6:    ")
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
    cars = get_all_cars()
    if not cars:
        print("❌ sorry, the database is empty. You need to create cars first")
    else:
        clear_screen()
        print_header()
        print("\n✏️  LIST OFF AVAILABLE CARS")
        print("-"*30)
        for car in cars:
            print(car)
        
        input("Press Enter to continue... ")


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
        input("Press Enter to continue... ")
        
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
    print("\n✏️  DELETE SPECIFIC CAR")
    print("-"*30)
    keyword = input("Which term would you like to use use for SEARCH:    ")
    if not keyword:
        print("❌ The term can not be empty!")
    else:
        result = search_cars(keyword)
        print(f"We found {len(result)} car(s) with this -- : {keyword} : TERM")
        for item in result:
            print(item)
        
        input("Press Enter to continue... ")

    





def main():
    initialize_database()  # Always call this first!
    import_cars()          # Load sample data if the table is empty
    
    while True:
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
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter 1/2/3/4/5/6:   ")




if __name__ == "__main__":
    main()