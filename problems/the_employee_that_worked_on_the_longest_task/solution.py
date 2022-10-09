class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        hardest = (0, [])
        
        start = 0
        for (worker_id, leave_time) in logs:
            task_length = leave_time - start
            start = leave_time
            
            # if have longer task time
            if task_length > hardest[0]:
                hardest = (task_length, worker_id)
                
            # if have equally long task time
            if task_length == hardest[0]:
                min_id = min(worker_id, hardest[1])
                hardest = (task_length, min_id)
                
        return hardest[1]