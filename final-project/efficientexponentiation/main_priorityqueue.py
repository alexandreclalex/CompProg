import sys
import heapq

class prioritizedChain(object):
    def __init__(self, chain):
        self.chain = chain
    
    def __repr__(self):
        return str(self.chain)
    
    def __lt__(self, other):
        return len(self.chain) < len(other.chain)
    
def solve(n):
    best_score = [n]*(n+1)
    best_score[0] = 0
    best_score[1] = 1

    heap = [prioritizedChain((1,))]
    
    while len(heap) > 0:
        next_chain = heapq.heappop(heap).chain
        for elem in next_chain[::-1]:
            next_val = elem + next_chain[-1]
            if next_val == n:
                return len(next_chain)
            # if next_val < n and len(next_chain) + 1 < best_score[next_val]:
                # best_score[next_val] = len(next_chain) + 1
            heapq.heappush(heap, prioritizedChain(next_chain + (next_val,)))

if __name__ == '__main__':
    n = int(sys.stdin.readline())  
    print(solve(n))