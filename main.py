from ticketbooking import movie_ticket
class Main:
    def execute(self, choice):
        if choice == 1:
            print('SHow the Seats*******')
            movie_ticket_object.show_seats()
        if choice == 2:
            print('SHow the tickets*******')
            movie_ticket_object.buy_tickets()
        if choice == 3:
            print('**Statistics*******')
            movie_ticket_object.statistics()
        if choice == 4:
            print('***Show the booked tickets*******')
            movie_ticket_object.user_info()
        if choice == 0:
            print('** Thanks visit again*******')
            exit()


if __name__ == '__main__':
    rows = int(input('Enter the number of rows--> '))
    columns = int(input('Enter the number of columns--> '))

    movie_ticket_object = movie_ticket(rows, columns)
    obj = Main()

    while True:
        choice = int(input('Enter the things 1 -- Show the seats, 2-- ticket, 3-- booked seats, 4 -- user info, 0-- Exit'))
        obj.execute(choice)

