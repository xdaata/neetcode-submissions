class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand_map = {}
        for d in hand:
            if d in hand_map: hand_map[d] += 1
            else: hand_map[d] = 1

        for _ in range(0, len(hand), groupSize):
            start = min(hand_map)
            for j in range(groupSize):
                if start + j in hand_map:
                    hand_map[start + j] -= 1
                    if hand_map[start + j] == 0:
                        del hand_map[start + j]
                else:
                    return False
        
        return True              


