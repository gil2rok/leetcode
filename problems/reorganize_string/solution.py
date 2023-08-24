import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        # init heap and res
        heap = [(-count, time, char)for time, (char, count) in enumerate(Counter(s).items())]
        heapq.heapify(heap)

        self.time = len(s)
        res = ""
        
        # add most freq char to res
        print(res, "\t", heap)

        count, char = self.my_pop(heap)
        res += char
        count -= 1
        self.my_push(heap, count, char)
        self.time += 1

        for _ in range(len(s) - 1):
            print(res, "\t", heap)
            count, char = self.my_pop(heap) 

            # if most freq char was just added to res
            if char == res[-1]:
                if (len(heap) == 0) or (len(heap) == 1):
                    return ""

                count2, char2 = self.my_pop(heap)
                res += char2
                count2 -= 1
                self.my_push(heap, count2, char2)
                self.time += 1

                self.my_push(heap, count, char)
                self.time += 1
            else:
                res += char
                count -= 1
                self.my_push(heap, count, char)
                self.time += 1

        print(res, "\t", heap)
        return res
            
    def my_push(self, heap, count, char):
        if count > 0:
            neg_count = -count
            heapq.heappush(heap, (neg_count, self.time, char))

    def my_pop(self, heap):
        neg_count, _, char = heapq.heappop(heap)
        count = -neg_count
        return count, char
