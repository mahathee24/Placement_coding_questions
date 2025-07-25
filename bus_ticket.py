class Bus:
    def __init__(self, bno, ac, cap):  
        self.bno = bno
        self.ac = ac
        self.cap = cap

    def get_bno(self):
        return self.bno

    def get_cap(self):
        return self.cap

    def get_ac(self):
        return self.ac

    def display(self):
        print(f"{'BUS NO':<15}: {self.get_bno()}")
        print(f"{'AC':<15}: {self.get_ac()}")
        print(f"{'BUS CAPACITY':<15}: {self.get_cap()}")
        print("-" * 30)

BUSES = [Bus(1, True, 2), Bus(2, False, 60), Bus(3, True, 55)]

class Booking:
    BOOKINGS = []  

    def __init__(self, passenger, bus_no, date):
        self.passenger = passenger
        self.bus_no = bus_no
        self.date = date 

    def make_booking(self, buses):
        bus = next((b for b in buses if b.get_bno() == self.bus_no), None)
        if not bus:
            print("Invalid Bus Number")
            return

        count = Booking.count_bookings(bus.get_bno(), self.date)
        if count >= bus.get_cap():
            print("Booking Failed: Bus is Full")
        else:
            Booking.BOOKINGS.append(self)
            print(f"Booking Successful for {self.passenger} on Bus {self.bus_no} ({self.date})")

    @staticmethod
    def count_bookings(bus_no, date):  
        return sum(1 for b in Booking.BOOKINGS if b.bus_no == bus_no and b.date == date)

    @staticmethod
    def check_availability(bus_no, date, buses): 
        bus = next((b for b in buses if b.get_bno() == bus_no), None)
        if not bus:
            print("Bus Not Found")
            return
        booked = Booking.count_bookings(bus_no, date)
        print(f"Available Seats on Bus {bus_no} for {date}: {bus.get_cap() - booked}")

    @staticmethod
    def display_all_bookings():  
        if not Booking.BOOKINGS:
            print("No bookings yet.")
            return
        print("\nAll Bookings:")
        for b in Booking.BOOKINGS:
            print(f"{b.passenger} - Bus {b.bus_no} - Date: {b.date}")

for bus in BUSES:
    bus.display()


b1 = Booking("Alice", 1, "2025-07-22")
b1.make_booking(BUSES)

b2 = Booking("Bob", 1, "2025-07-22")
b2.make_booking(BUSES)

b3 = Booking("Charlie", 1, "2025-07-22")  
b3.make_booking(BUSES)

Booking.check_availability(1, "2025-07-22", BUSES)

Booking.display_all_bookings()
