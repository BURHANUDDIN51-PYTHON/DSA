from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict([])

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key: 
            self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # Return empty string if there are no key in timemap
        if key not in self.timemap:
            return ""

        # Return the key -> value with the timestamp or the closest 
        for v, t in self.timemap[key]:
            if t <


        return ""

timeMap = TimeMap()
timeMap.set("alice", "happy", 1) # // store the key "alice" and value "happy" along with timestamp = 1.
print(timeMap.get("alice", 1))         #// return "happy"
timeMap.get("alice", 2)          # // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
timeMap.set("alice", "sad", 3)    
print(timeMap.get("alice", 3))  
