class movie_ticket:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.user_details = {}

    def show_seats(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if i == 0:
                    if j == 0:
                        print(' ', end = " ")
                    else:
                        print(j, end = ' ')
                elif j == 0:
                    print(i, end = ' ')
                else:
                    if self.is_seat_booked(i, j):
                        print('B', end=' ')
                    else:
                        print('S', end=' ')

    def buy_tickets(self):
        row = int(input('ENter the Rows no---> '))
        columns = int(input('ENter the columns no---> '))
        total_seat = self.rows * self.columns
        ticket_price = 10
        if total_seat <= 60:
            total_price = 10
        else:
            first_half = self.rows//2
            if row > first_half:
                total_price = 8
            else:
                ticket_price = 10

        seat_no = row * columns
        option = int(input(f'you have selected row {row} and column no is {columns}, so the price of your seats are in Rupees. {ticket_price}, if you still book the ticket please enter 1 - Yes, 2 - No'))
        if option == 1:
            name = input('Enter the Name')
            gender = input('ENter the Gender, Male or Female')
            age = int(input('Enter your Age'))
            phone = int(input('Enter Your MNo'))
            self.user_details[seat_no] = [name, gender, age, phone]
            print(self.user_details)
            print('Seats booked Successfully!!')
        else:
            print('No Problem , Thatks for connecting with Book My show App!!')




    def statistics(self):
        total_seats = self.rows * self.columns
        ticket_purchased = len(self.user_details)
        percentage_sold = ((self.user_details)/total_seats)*100
        price_list = []
        for k,v in self.user_details.items():
            price_list.append(v[3])
        current_income = sum(price_list)
        if total_seats <= 60:
            total_income = total_seats * 10
        else:
            front_price = 10
            back_price = 8
            total_income = front_price + back_price
        print(f'TOtal Income from the tickets {total_income}')

    def user_info(self):
        row = int(input('Enter the Rows'))
        column = int(input('Enter the columns'))
        seat_no = row * column
        user_details = self.user_details.get(seat_no, None)
        if user_details: # True
            print(f'Name of user :{user_details[0]}')
            print(f'Gender of user :{user_details[1]}')
            print(f'Age of user :{user_details[2]}')
            print(f'Phone of user :{user_details[3]}')

        else:
            print('Seat is not Booked!!')

    def is_seat_booked(self, row, column):
        seat_no = row * column
        if seat_no in self.user_details.keys():
            return True
        return False

