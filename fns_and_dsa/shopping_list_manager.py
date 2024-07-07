shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice.isdigit():
            choice = int(choice)
            
            if choice == 1:
                item = input("Enter item to add: ")
                shopping_list.append(item)
                print(f"{item} added to the shopping list.")
            
            elif choice == 2:
                item = input("Enter item to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"{item} removed from the shopping list.")
                else:
                    print(f"Item '{item}' not found in the shopping list.")
            
            elif choice == 3:
                if not shopping_list:
                    print("Shopping list is empty.")
                else:
                    print("Shopping List:")
                    for item in shopping_list:
                        print(item)
            
            elif choice == 4:
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        else:
            print("Invalid input. Please enter a number.")
        
if __name__ == "__main__":
    main()
