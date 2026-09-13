from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        sorted_keys = sorted(count.keys())

        for card in sorted_keys:
            if count[card] > 0:
                start_count = count[card]
                for i in range(groupSize):
                    if count[card + i] < start_count:
                        return False
                    count[card + i] -= start_count            
        
        return True       
