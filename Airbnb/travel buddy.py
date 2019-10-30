class TravelBuddy:
    def __init__(self, myWishList, friendsWishList):
        self.myWishList = myWishList
        self.friendsWishList = friendsWishList

    def getTravelBuddy(self):
        travelBuddies = []
        for k, v in self.friendsWishList.items():
            if len(v & self.myWishList) > len(self.myWishList) // 2:
                travelBuddies.append(k)
        return travelBuddies

    def recommend(self, k):
        travelBuddies = self.getTravelBuddy()
        travelBuddies.sort(key = lambda x : -len(self.myWishList & self.friendsWishList[x]))
        recommend = set()
        for buddy in travelBuddies:
            for place in self.friendsWishList[buddy] - self.myWishList:
                if place not in recommend:
                    recommend.add(place)
                    k -= 1
                    if k == 0:
                        return recommend
        return recommend
travelBuddy = TravelBuddy({'a', 'b', 'c', 'd'}, {'1' : {'a', 'b', 'c', 'd', 'e'}, '2' : {'f'}, '3' : {'a', 'b', 'd', 'f'}})
print(travelBuddy.getTravelBuddy())
print(travelBuddy.recommend(3))
