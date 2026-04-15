print ('Welcome to West Shark Cafe!')
print ('Our Menu; Coffee, Mocha, Red Bull')
menu = {"Coffee": 5.0,
        "Mocha": 3.5,
       "Red Bull": 3.0
}
orders = []
total = [] 
while True: 
    choice = input("Type a menu item to add, 'remove' to delete something, or type 'Done' to quit:").lower()
    
    if choice == "menu":
                if input is not menu:
                      print ('This is not a menu item.')
                if choice == "remove" or "done":
                       continue
                
                
        
    else:
                item_to_add = choice
                orders.append(item_to_add)
                print('Added', orders)

    if choice == "done":
        print ('Shutting Down...')
        break 

    if choice == "remove":
         if len(orders) == 0:
               print("Your order is empty.")
               continue
         
         item_to_remove = input("What would you like to remove?")
         if item_to_remove in orders:
                orders.remove(item_to_remove)
                print(item_to_remove, "removed")
                if item_to_remove is not orders:
                    print('This item does not exist')
    
    

                print("Final Order", orders)


