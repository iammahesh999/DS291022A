
def uber_eats():
    print('Welcome! User What you want to eat')
    print('###################### Welcome to Uber Eats ###################')
    print('###################### Please Make your Order ###################')

    print('\t(O)--> Order\n'
          '\t(P)--> Payment\n',
          '\t(R)--> Report\n'
          '\t(E)--> Exit')
    a = input("Please select one of them")
    if a == 'O':
        def_order()
        break
    elif a == 'P':
        def_payment()
        break
    elif a == 'R':
        def_report()
        break
    elif a == 'E':
        def_exit()
        break
    else:
        print('Invalid Input Please try again')



def def_order():
    print('######################Welcome to the Order Page Please make an Order #########################')
    print('We have \n(F)--> Food Items\n(M)--> Main Menu\n(E)--> Exit')
    b = input("Please select one item")
    if b == 'F':
        def_food_items()
    elif b == 'M':
        def_main_menu()
    elif b == 'E':
        def_exit()
    else:
        def_order()

order_list = {}
def def_payment():
    print('Your Bill Is here')
    print('How would you like to payment \nCard\nCash\nATM')
    print('You Have order These things', order_list)
    if len(order_list) > 0:
        for i,j in order_list.items():
            print('And Your Total Payment is ', order_list[i], order_list[j])
        print('Yoru Total Payable bill is ', sum(order_list.values()))

    else:
        print("Your have'nt order something")



def def_report():
    rating = []
    print('Hoep you Enjoy the Food')
    print('Would you like to gvie the rating to the food')
    c = input('Enter the Feedback into Yes Or No')
    if c == 'Yes':
        d = int(input('Please give the rating into 1 to 5'))
        rating.append(d)
        print('Thankyou Please visit again')

    else:
        print('Will meet next time!')

print(uber_eats())

