class NationalPark:
    #Stores all parks for most visited classmethod
    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception("Name cannot be changed.")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list(set([trip.visitor for trip in Trip.all if trip.national_park == self]))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors = [trip.visitor for trip in Trip.all if trip.national_park == self]
        return max(visitors, key = visitors.count)

    @classmethod
    def most_visited(cls):
        #first argument of max is what were comparing(iterating through) and we create the key park with value of its total visits
        #lambda is a key function to sort through a list
        return max(cls.all, key = lambda park: park.total_visits())

class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
    
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
        else:
            raise Exception
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
        else: 
            raise Exception


class Visitor:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in Trip.all if trip.visitor == self]))
    
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])