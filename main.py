from collections import defaultdict
from functools import reduce


class Person:
    def __init__(self, name, age, exp):
        self.name = name
        self.age = age
        self.exp = exp

    def show(self):
        print("Name: " + self.name + " Age: " + str(self.age) + " Exp: " + str(self.exp))


class Employee(Person):
    def __init__(self, name, age, exp, supervisor):
        Person.__init__(self, name, age, exp)
        self.supervisor = supervisor

    def show(self):
        print("Employee name: " + self.name + "age: " + str(self.age) + " exp: " + str(
            self.exp) + " Supervisor: " + self.supervisor.name)


class Supervisor(Person):
    def __init__(self, name, age, exp):
        Person.__init__(self, name, age, exp)
        self.employee = list()

    def assign_employee_to_supervisor(self, emp):
        self.employee.append(emp)

    def show(self):
        Person.show(self)
        print("Supervisor has employees: ")
        for emp in self.employee:
            print("-" + emp.name + " age: " + str(emp.age))


class Customer:
    def __init__(self, name, passport, nationality, phone_number, email, total_flight, distance):
        self.name = name
        self.passport = passport
        self.nationality = nationality
        self.phone_number = phone_number
        self.email = email
        self.total_flight = total_flight
        self.distance = distance

    def show(self):
        print("Customer name: " + self.name + " Passport: " + str(self.passport))


class Ticket:
    ticket_id = 0

    def __init__(self, date, flight, customer):
        self.ticket_id = Ticket.ticket_id
        Ticket.ticket_id += 1
        self.date = date
        self.customer = customer
        self.flight = flight

    def show(self):
        print("Ticket with ID:" + str(self.ticket_id) + " Booked for: " + self.customer)


class Flight:
    flight_id = 0

    def __init__(self, source, destination, departure_date, arrival_date, duration, airplane, business_cost,
                 economy_cost):
        self.id = Flight.flight_id + 1
        Flight.flight_id += 1
        self.source = source
        self.destination = destination
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.duration = duration
        self.airplane = airplane
        self.business_cost = business_cost
        self.economy_cost = economy_cost

    def show(self):
        print("Flight ID: " + str(
            self.id) + " --- Source: " + self.source + " --- Destination: " + self.destination + " --- Used Airplane: " + self.airplane)


class Airplane:
    def __init__(self, name, numberOfBusinessSeats, numberOfEconomySeats):
        self.name = name
        self.numberOfBusinessSeats = numberOfBusinessSeats
        self.numberOfEconomySeats = numberOfEconomySeats
        self.state = "available"

    def set_state(self, val):
        self.state = val

    def show(self):
        print("Airplane name :" + self.name + "  ----  Number of business seats :" + str(
            self.numberOfBusinessSeats) + "  -----  Number of economy seats :" + str(
            self.numberOfEconomySeats) + " --- State: " + self.state)


class Airport:
    def __init__(self, name):
        self.name = name
        self.employees = list()
        self.incoming_flights = list()
        self.outgoing_flights = list()
        self.customers = list()
        self.supervisor = list()
        self.tickets = list()
        self.airplans = list()

    def add_supervisor(self, name, age, exp):
        s = Supervisor(name, age, exp)
        self.supervisor.append(s)

    def add_employee(self, name, age, exp, sup_name):
        for sup in self.supervisor:
            bool = 0
            if sup.name == sup_name:
                bool = 1
                emp = Employee(name, age, exp, sup_name)
                sup.assign_employee_to_supervisor(emp)
                self.employees.append(emp)
                break
        if bool == 0:
            print("ERROR: Supervisor not found --- failed to add employee: " + name)

    def add_customer(self, name, passport, nationality, phone_number, email, total_flight, distance):
        c = Customer(name, passport, nationality, phone_number, email, total_flight, distance)
        self.customers.append(c)

    def add_flight(self, source, destination, departure_date, arrival_date, duration, airplane, business_cost,
                   economy_cost):
        f = Flight(source, destination, departure_date, arrival_date, duration, airplane, business_cost, economy_cost)
        for airpl in self.airplans:
            bool = 0
            if airpl.name == airplane and airpl.state == "available":
                airpl.set_state("not available")
                bool = 1
                if source == "Syria":
                    self.outgoing_flights.append(f)
                else:
                    self.incoming_flights.append(f)
                break
        if bool == 0:
            print("ERROR airplane does not exist or it's not available.")

    def add_airplane(self, name, nob, noe):
        a = Airplane(name, nob, noe)
        self.airplans.append(a)

    def book_a_ticket(self, date, flight_id, customer):
        flights = self.incoming_flights + self.outgoing_flights
        for fli in flights:
            bool1 = 0
            if flight_id == fli.id:
                bool1 = 1
                break
        for cust in self.customers:
            bool2 = 0
            if customer == cust.name:
                bool2 = 1
                break
        if bool1 == 0 and bool2 == 0:
            print("ERROR: customer not found")
            print("ERROR: flight not found")
        if bool1 == 0 and bool2 == 1:
            print("ERROR: flight not found")
        if bool1 == 1 and bool2 == 0:
            print("ERROR: customer not found")
        if bool1 == 1 and bool2 == 1:
            t = Ticket(date, flight_id, customer)
            self.tickets.append(t)

    def cancel_ticket(self, id):
        for tick in self.tickets:
            if tick.ticket_id == id:
                self.tickets.remove(tick)

    def edit_passport(self, name, passport):
        for customer in self.customers:
            bool = 0
            if customer.name == name:
                bool = 1
                oldpass = customer.passport
                customer.passport = passport
                print("--Passport changed form: " + str(oldpass) + " To: " + str(
                    customer.passport) + " For customer: " + customer.name)
                break
        if bool == 0:
            print("ERROR: customer not found.")

    def show_supervisors(self):
        for sup in self.supervisor:
            sup.show()

    def show_customers(self):
        for customer in self.customers:
            customer.show()

    def show_tickets(self):
        for ticket in self.tickets:
            ticket.show()

    def show_airplans(self):
        for airplane in self.airplans:
            airplane.show()

    def show_flights(self):
        print("Incoming flights")
        for inc in self.incoming_flights:
            inc.show()
        print("Outgoing flights")
        for out in self.outgoing_flights:
            out.show()

    def show_tickets_onboard(self, flight_id):
        for tick in self.tickets:
            bool = 0
            if flight_id == tick.flight:
                tick.show()
                bool = 1
                break
        if bool == 0:
            print("Tikcet doesn't exist")

    def search_flight(self, src, des):
        flights = self.incoming_flights + self.outgoing_flights
        for fli in flights:
            bool = 0
            if fli.source == src and fli.destination == des:
                print("Flight id: " + str(fli.id) + " Source: " + fli.source + " Destination: " + fli.destination)
                bool = 1
                break
        if bool == 0:
            print("Flight does not exist")

airport = Airport("Awakener Lore")

airport.add_supervisor("Majd", 21, 100)
airport.add_supervisor("Mohammad", 20, 50)

airport.add_employee("Yassen1", 22, 100, "Majd")
airport.add_employee("Yassen2", 20, 100, "Majd")
airport.add_employee("Yassen3", 21, 100, "Majd")
airport.add_employee("Yassen4", 23, 100, "Mohammad")
airport.add_employee("Yassen5", 21, 100, "Mohammad")
airport.add_employee("Yassen6", 20, 100, "Mohammad")

airport.add_customer("Jhin", 184672, "Syrian", "093232123", "Jhin@outlook.com", 2, "200KM")
airport.add_customer("Blitz", 284672, "Syrian", "092112123", "Blitz@outlook.com", 1, "400KM")
airport.add_customer("Drox", 384672, "Syrian", "0932329435", "Drox@outlook.com", 3, "1000KM")
airport.add_customer("Scout", 484672, "Syrian", "0932435123", "Scout@outlook.com", 10, "200KM")

airport.add_airplane("Choas", 10, 20)
airport.add_airplane("Vaal", 11, 30)
airport.add_airplane("Grace", 12, 40)
airport.add_airplane("Haste", 13, 35)
airport.add_airplane("Lacerate", 14, 20)

airport.add_flight("Syria", "USA", "1/2/2020", "1/2/2020", 20, "Choas", "200$", "100$")
airport.add_flight("Syria", "Spain", "1/2/2020", "1/2/2020", 20, "Vaal", "200$", "100$")
airport.add_flight("USA", "Syria", "1/2/2020", "1/2/2020", 20, "Haste", "200$", "100$")
airport.add_flight("Spain", "Syria", "1/2/2020", "1/2/2020", 20, "Lacerate", "200$", "100$")

print("<--------------- Printing Supervisors with their employees -------------------------> ")
airport.show_supervisors()

print("<--------------- Printing customers ------------------------------------------------> ")
airport.show_customers()
airport.edit_passport("Jhin", 13241)

print("<--------------- Printing Airplanes ------------------------------------------------> ")
airport.show_airplans()

print("<--------------- Printing Flights --------------------------------------------------> ")
airport.show_flights()

print("<--------------- Printing Flights on search ----------------------------------------> ")
airport.search_flight("Syria", "USA")

airport.book_a_ticket("1/2/2020", 3, "Drox")
airport.book_a_ticket("1/2/2020", 1, "Jhin")
airport.book_a_ticket("1/2/2020", 2, "Blitz")
airport.book_a_ticket("1/2/2020", 3, "Scout")

print("<--------------- Printing tickets --------------------------------------------------> ")
airport.show_tickets()

print("<--------------- Printing tickets on-board of flight -------------------------------> ")
airport.show_tickets_onboard(3)

airport.cancel_ticket(0)
airport.cancel_ticket(2)
print("<--------------- Printing tickets after delete -------------------------------------> ")
airport.show_tickets()


f1 = open("test1.txt", "r")
f2 = open("test2.txt", "r")
f3 = open("test3.txt", "r")
files = list()

for x in f1:
    files.append(x)
for x in f2:
    files.append(x)
for x in f3:
    files.append(x)

dic = {}
for doc in files:
    d = doc.split(",")
    company = d[0].strip()
    if company in dic.keys():
        dic[company] += 1
    else:
        dic[company] = 1


def call(name):
    for ac in f1:
        if name in ac:
            dic[name] += 1


mapper = map(call, list(dic.keys()))
list(mapper)
zz = reduce(lambda x, y: max(x, y), list(dic.values()))


def get_keys(value):
    for key, valu in dic.items():
        if value == valu:
            return key


print("the big number :", get_keys(zz), max(dic.values()))

