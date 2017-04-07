import operator
class smart_traffic: 
    signal_timeout = 5
    max_traffic = 15
    def __init__(self, north_count, east_count, south_count, west_count):
        self.north_count = north_count
        self.east_count = east_count
        self.south_count = south_count
        self.west_count = west_count
        self.sorted_list = []
        self.allowed_time = {}
        # self.directionArray = {"northRight":nc, "eastDown":ec, "southLeft":sc, "westUp":wc}
    def get_sorted_dir_list(self):
        '''sorting the direction array, return is a list which inherently stored tuples with direction and count'''
        directionArray = {"northRight":self.north_count, "eastDown":self.east_count, "southLeft":self.south_count, "westUp":self.west_count}
        sorted_direction = sorted(directionArray.items(), key=operator.itemgetter(1))
        return sorted_direction
    def time_mapping(self,traffic):
        if traffic>smart_traffic.max_traffic:
            return smart_traffic.signal_timeout
        else: 
            return traffic*smart_traffic.signal_timeout/smart_traffic.max_traffic
    def get_time_for_each_dir(self):
        '''It returns a dictionary where key is the direction and value is the allowed time for that direction'''
        sorted_list = self.get_sorted_dir_list()
        for entries in sorted_list:
            self.allowed_time[entries[0]] = self.time_mapping(entries[1])
        return self.allowed_time        


'''By uncommenting the below lines you can test this code, whether it is returning the correct time for all direction or not.'''
'''Now the time is coming in decimal, changes can be made in the code to always return an integer value.'''

'''
if __name__=="__main__":
    ans=smart_traffic(10,15,8,4).get_time_for_each_dir()
    print(ans)
'''        
        
