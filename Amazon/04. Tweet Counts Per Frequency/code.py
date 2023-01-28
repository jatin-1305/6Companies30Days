from collections import defaultdict, Counter
class TweetCounts:
    def __init__(self):
        self.tweets = defaultdict(Counter)

    def recordTweet(self, tweetName: str, time: int) -> None:            
        self.tweets[tweetName][time] += 1

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            delta = 60
        elif freq == 'hour':
            delta = 3600
        elif freq == 'day':
            delta = 86400
        results = [0 for _ in range(startTime, endTime+1, delta)]
        for time in self.tweets[tweetName]:
            if time >= startTime and time <= endTime:
                results[(time-startTime+1) // delta] += self.tweets[tweetName][time]
        return results
