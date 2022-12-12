class Allocator:

    def __init__(self, n: int):
        self.memory = [-1]*n # -1 indicates free, 1 indicates occupied

    def allocate(self, size: int, mID: int) -> int:
        free_units = 0
        
        # find starting index of free memory of size n
        start_idx = -1
        for i in range(len(self.memory)):
            # keep track of starting index
            if free_units == 0:
                start_idx = i
            
            # check if current index is occupied or not
            if self.memory[i] == -1: 
                free_units += 1
            else: 
                free_units = 0
                
            # if have enough size, stop
            if free_units == size:
                break
                
        if free_units != size:
            start_idx = -1

        # assign memory id to free memory, if there is room
        if start_idx != -1:
            for i in range(start_idx, start_idx + size):
                self.memory[i] = mID

        
        return start_idx
               

    def free(self, mID: int) -> int:
        count = 0
        for i in range(len(self.memory)):
            if self.memory[i] == mID:
                self.memory[i] = -1
                count += 1
        
        return count
    
# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)