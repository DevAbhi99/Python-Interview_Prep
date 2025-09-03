#Low level Design parking system

#Assume there are total 25 parking spots 

class Parkinglot:   #Track ticket details and parking spots
    def __init__(self):
        self.tickets={}
        self.parkingspots={}
    
    def ticketDetails(self):
        return self.tickets
    
    def parkingDetails(self):
        return self.parkingspots


class Vehicle:                    #Register vehicle in the parking spot
    def __init__(self, licensePlate):
        self.licensePlate=licensePlate

    def sendVehicleData(self):
        return self.licensePlate


class Ticket:                       #Generate ticket on the basis of the vehicle registered
    def __init__(self, vehicle:Vehicle):
        self.add=vehicle

    def ticketGenerate(self):
        return f'{self.add.sendVehicleData()}tc'
    
class Parkingspot:    #Book a parking spot or leave a parking spot
    def __init__(self, parkinglot:Parkinglot, vehicle:Vehicle, ticket:Ticket):
        self.lot=parkinglot
        self.vehicle=vehicle
        self.ticket=ticket

    
    def parkingSpotAdd(self):
        if(len(self.lot.parkingspots)<=25):
            if self.ticket.ticketGenerate() in self.lot.parkingspots: 
                if self.lot.parkingspots[self.ticket.ticketGenerate()]:
                    return 'Vehicle already parked'
                else:
                    self.lot.parkingspots.update({self.ticket.ticketGenerate():True})
                    self.lot.tickets.update({self.ticket.ticketGenerate():self.vehicle.sendVehicleData()})
                    return 'parking spot booked'
            else:
                self.lot.parkingspots.update({self.ticket.ticketGenerate():True})
                self.lot.tickets.update({self.ticket.ticketGenerate():self.vehicle.sendVehicleData()})
                return 'parking spot booked'
        else:
            return 'Parking spot is full'

    def parkingSpotLeave(self):
        if self.lot.parkingspots[self.ticket.ticketGenerate()]:
            self.lot.parkingspots.update({self.ticket.ticketGenerate():False})
            self.lot.tickets.pop(self.ticket.ticketGenerate())
            return 'parking spot left'
        else:
            return 'Vehicle not in the parking spot'
            

#Demonstration

obj1=Parkinglot()

obj2=Vehicle('HR1234')

obj3=Ticket(obj2)

obj4=Parkingspot(obj1, obj2, obj3)


print(obj3.ticketGenerate())

print(obj4.parkingSpotAdd())

print(obj1.ticketDetails(), obj1.parkingDetails())

print(obj4.parkingSpotLeave())



    
