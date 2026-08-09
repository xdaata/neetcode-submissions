class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet_map = defaultdict(list)  # кто что пишет
        self.follow_map = defaultdict(set)  # кто на кого подписан

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweet_map[userId].append([self.time, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        users = self.follow_map[userId]
        users.add(userId)

        for u in users:
            for tweet in self.tweet_map[u][-10:]:
                max_heap.append(tweet)
        heapq.heapify(max_heap)

        news = []
        while max_heap and len(news) < 10:
            news.append(heapq.heappop(max_heap)[1])

        return news     


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)

        
