class UndergroundSystem:
    def __init__(self):
        self.persons = {}
        self.stationMap = {}
        
    def checkIn(self, id_, st1, t1):
        if not self.persons.get(id_):
            self.persons[id_] = (st1, t1)
        
    def checkOut(self, id_, st2, t2):
        st1, t1 = self.persons.get(id_)
        
        if not self.stationMap.get((st1, st2)):
            totalTime, count = 0, 0
        else:
            totalTime, count = self.stationMap.get((st1, st2))
        
        totalTime += (t2 - t1)
        count += 1
        
        self.stationMap[(st1, st2)] = (totalTime, count)
        del self.persons[id_]
        
    def getAverageTime(self, st1, st2):
        totalTime, count = self.stationMap.get((st1, st2))
        return totalTime / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)