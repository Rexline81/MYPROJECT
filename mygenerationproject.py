# Dictionary of cafe items for sale
cafe_items = {
    "espresso": 2.50,
    "cappuccino": 3.00,
    "latte": 3.25,
    "mocha": 3.50,
    "americano": 2.75,
    "macchiato": 3.25,
    "iced coffee": 3.00,
    "chai latte": 3.75,
    "hot chocolate": 3.50,
    "tea": 2.00
}
# Dictionary of books for sale
books = {
    'to kill a mockingbird': 25.00,
    'unsafe': 25.00,
    'the great gatsby': 30.00,
    'jane eyre': 25.00,
    'of mice and men': 30.00,
    '1984': 20.00,
    'pride and prejudice': 30.00,
    'diary of a ceo': 10.00,
    'hustle harder hustle smarter': 10.00
}
# Dictionary of books on special offer
books_offer = {
    'harry potter': 10.00,
    'diary of a ceo': 10.00,
    'hustle harder hustle smarter': 10.00
}
def menu():
    print('\nChoose an option: '.title())
    print('[1] customer'.title())
    print('[2] employee'.title())
    print('[0] exit'.title())
customer_database = {}
def customer_update(customer_name, customer_address, customer_email):
    customer_database['name'] = customer_name
    customer_database['address'] = customer_address
    customer_database['email'] = customer_email
# Created shopping cart to hold cafe items and books
customer_cart = {}
def option1():
    while True:
        print('\nCustomer Options:')
        print('[1] View cafe menu')
        print('[2] View book menu')
        print('[0] Exit to main menu')
        customer_option = input('Please, choose an option: ')
        if customer_option == '0':
            break
        elif customer_option == '1':
            print('\nCafe Menu:')
            for item, price in cafe_items.items():
                print(f'[{item}] - £{price}')
            cafe_order = input('Please, choose a cafe item to order (or 0 to go back): ')
            if cafe_order == '0':
                break
            elif cafe_order in cafe_items:
                if cafe_order in customer_cart:
                    customer_cart[cafe_order] += 1
                else:
                    customer_cart[cafe_order] = 1
                print(f'You ordered {cafe_order} for £{cafe_items[cafe_order]}')
            else:
                print('Invalid cafe item. Please choose a valid item.')
        elif customer_option == '2':
            print('\nThese are the books we sell:')
            for book, price in books.items():
                print(f'{book} : £{price}')
            print('\nBut, these books are on special offer:')
            for book, price in books_offer.items():
                print(f'{book} : £{price}')
            while True:
                print('\nBook Menu:')
                print('[1] Order a book')
                print('[2] Checkout')
                print('[0] Return to previous menu')
                book_option = input('Please, choose an option: ')
                if book_option == '1':
                    print('Here are the available books:')
                    for book, price in books.items():
                        print(f'[{book}] - £{price}')
                    book_choice = input('Please, choose a book to order (or 0 to go back): ')
                    if book_choice == '0':
                        break
                    elif book_choice in books:
                        if book_choice in customer_cart:
                            customer_cart[book_choice] += 1
                        else:
                            customer_cart[book_choice] = 1
                        print(f'You ordered {book_choice} for £{books[book_choice]}')
                    else:
                        print('Invalid book selection. Please choose a valid book.')
                elif book_option == '2':
                    customer_update(input("What is your name?"), input("What is your address?"), input("What is your email?"))
                    print(customer_database)
                    print('\nYour Cart:')
                    for item, quantity in customer_cart.items():
                        print(f'{item} x{quantity}')
                    total_cost = sum(
                        (books[item] if item in books else cafe_items[item]) * quantity
                        for item, quantity in customer_cart.items()
                    )
                    print(f'Total Cost: £{total_cost}')
                    print(f'\nCustomer information:')
                    print(customer_database)
                elif book_option == '0':
                    break
                else:
                    print('Invalid option. Please choose a valid option.')
        else:
            print('Invalid option. Please choose a valid option.')
def option2():
    while True:
        print('\nEmployee Options:')
        print('[1] Update/Add')
        print('[2] Delete')
        print('[0] Return to main menu')
        employee_option = input('Please, choose an option: ')
        if employee_option == '0':
            break
        elif employee_option == '1':
            print(customer_database)
            update_name = input('Enter new/updated name:')
            update_address = input('Enter new/updated address:')
            update_email = input('Enter the new/updated email:')
            print(f'\nYou have successfully added/updated the details for user "{update_name}" ')
        elif employee_option == '2':
            delete_user = input('Would you like to delete a user? ')
            if delete_user == 'yes':
               update_name = input('Please, enter user name: ')
               print(f'\nYou have successfully deleted the details for user "{update_name}" ')
            else:
                break
        else:
            print('Invalid option. Please choose a valid option.')
while True:
    menu()
    user_input = input('Please, choose an option: ')
    if user_input.isdigit():
        option = int(user_input)
        if option == 0:
            print('Thanks for using this program!\nTake Care :D')
            break
        elif option == 1:
            option1()
        elif option == 2:
            print('Welcome employee!')
            employee_option = input('Please enter your name: ')
            print(f'Hello, {employee_option}! How can we assist you?')
            option2()
        else:
            print('The option you have chosen is invalid. Please Try Again!')
    else:
        print('Invalid input. Please enter a valid option.')