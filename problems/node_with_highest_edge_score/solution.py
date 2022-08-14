class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        
        def return_zero():
            return 0
        
        scores = collections.defaultdict(return_zero)
        
        # directed edge u --> v
        for u, v in enumerate(edges):
            scores[v] += u
            
        max_node = -1
        max_score = -1
        for node, score in scores.items():
            if score > max_score:
                max_score = score
                max_node = node
            elif score == max_score and node < max_node:
                max_score = score
                max_node = node
        return max_node
            