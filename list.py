librarie=[]
wish_list =[]
books=input(print("Enter the name of a book you own:"))
librarie.append(books)

if books:
    books = input(print("Enter the name of another book you own (or press 'Enter' to skip):"))
    librarie.append(books)
    print(f"Your Library: {librarie}")
    if books:
        wish = input(print("Enter the name of another book you wish to have in the future(or press 'Enter' to skip):"))
        wish_list.append(wish)
    else:
      print(f"your own book is:{librarie}")  
    if wish:
        wish=input(print("Enter the name of another book from your wishlist:(or press 'Enter' to skip):"))
        wish_list.append(wish)
        print(f"Your wishlist: {wish_list}")
    else:   
         print(f"your own book is:{librarie}")
    if wish:
        wish=input(print("Enter the name of a book from wishlist that you´ve acquired or (press 'Enter' to skip):"))
        librarie.append(wish)
        wish_list.remove(wish)
        print(f"Updated Library {librarie}")
        print(f"Updated Wishlist: {wish_list}")
    else: 
        print(f"your own book is:{librarie}") 
        print(f"your own book is:{wish_list}")
    if wish:
         books = input(print("Enter the name of a book from your Library you wish to donate (or press 'Enter'):"))
         librarie.remove(books)   
         print(f"Final Library aftrr Donations: {librarie}")
         print(f"Final Wishlist: {wish_list}")      
else:
    print(f"your own book is:{librarie}")
