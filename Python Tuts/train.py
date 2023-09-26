seatsList = []
for i in range(1,101):
    seatsList.append(i)


class Train:
    seats = seatsList
    
    def __init__(self,name):
        self.name = name
    
    def getStatus(self):
       
        return print(f'{self.name} | {len(self.seats)} tickets \n{self.seats}')
    
    
    def bookTicket(self):
        if len(self.seats) != 0:
            T = self.seats[len(self.seats)-1]
            print(f'Your ticket is booked for seat number {T}')
            self.seats.remove(T)
        else:
            print('Sorry, no seat is available')
    
    def cancelTicket(self,ticketNumber):
        if ticketNumber not in range(1,101):
            print("Invalid Ticket Number")
       
        elif ticketNumber in self.seats :
            print("Invalid Ticket Number")
        else:
            self.seats.append(ticketNumber)
            print(f'Your ticket {ticketNumber} is cancelled')

        

Rajdhani = Train('Rajdhani X30000X91')
Rajdhani.bookTicket()
Rajdhani.getStatus()
Rajdhani.bookTicket()
Rajdhani.getStatus()
Rajdhani.bookTicket()
Rajdhani.getStatus()

Rajdhani.cancelTicket(98)
Rajdhani.getStatus()

Rajdhani.cancelTicket(1000000)

