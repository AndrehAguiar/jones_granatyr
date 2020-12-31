# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 18:56:47 2020

@author: TOP Artes
"""
from math import sqrt
from model.Rating import Rating


class Recommend(Rating):
    
    def __init__(self, testing: bool=False):
        super(Recommend, self).__init__(testing=testing)
        """
        Recomend Class
        :param testing: Default False, if True the test base will be set
        """
        
        self.similar = []
        self.similarItems = {}
        self.rankings = []
        self.rankItems = []
        self.history = {}
        
    def checkContext(self, by:str):
        if by == 'user':
            self.history = self._Rating__user_history
        elif by == 'item':
            self.history = self._Rating__item_history
        
    
    def __euclidean(self, target:str, ref:str, by:str) -> float:
        """
        Calculates the euclidean distance between two users
        :param user_1: User target to compare and get recommendations
        :param user_2: Second user to compare preferences
        :param by: 'user' or 'item', if by = 'user' calculates the euclidean distance between the users else between the items
        :return: Similarity by = 1 / (1 + euclidean distance)
        """
        si = {}
        self.checkContext(by)
        # Check each user/item history
        for item in self.history[target]:
            if item in self.history[ref]:
                si[item] = 1
            
        # Check if the others users have the movie in their history
        if len(si) == 0:
            return 0
        
        # Calculates the summatory of each user history
        summatory = sum([pow(self.history[target][item] - self.history[ref][item], 2)
                         for item in self.history[target]
                         if item in self.history[ref]])  
        
        return 1 / (1 + sqrt(summatory))
        
    
    def getSimilar(self, target: str, by:str) -> list:
        """
        List all users/items similarities for target
        :param user: User target
        :param by: 'user' or 'item', if by = 'user' calculates the euclidean distance between each user else between each item
        :return: list with [(similarity, id_1)...(similarity, id_n)]
        """        
        self.checkContext(by)
        # Call the function to get the similarity with each user
        self.similar = [(self.__euclidean(target, other, by), other)
                   for other in self.history
                   if other != target]
        
        # Sort the list and Reverse the values
        self.similar.sort(reverse=True)
        
        if len(self.similar) > 30: self.similar = self.similar[0:30]
        
        return self.similar
    
    def getSimilarItems(self, by:str) -> dict:
        """
        List all users/items similarities for each user/item
        :return: Dictionary with {id_1:[(similarity, 'user_1/item_1')...(similarity, 'user_n/item_n')]...id_n:[(similarity, 'user_1/item_1')...(similarity, 'user_n/item_n')]}
        """
        self.similarItems = {}
        self.checkContext(by)
        
        for item in self.history:
            rating = self.getSimilar(item, by)
            if by == 'user':
                self.similarItems[item] = rating
            else:
                self.similarItems[self.movies[item]] = rating
            "TODO: save similarItens.JSON / similarUsers.JSON"
        return self.similarItems
    
    def getRecommendation(self, user: str, by: str) -> list:
        """
        Calculates the similars users weghted mean ratings 
        :param user: User target
        :return: list with Weighted similarity rank [(similarity, item_1)...(similarity, item_n)]
        """
        totals = {}
        sumSimilar = {}
        self.checkContext(by)
        for other in self.history:
            if other == user: continue
            # Get the similarity by euclidean distance
            similarity = self.__euclidean(user, other, by)
            
            if similarity <= 0: continue
            
            for item in self.history[other]:
                if item not in self.history[user]:
                    totals.setdefault(item, 0)
                    # Calculates the wheight for each user and item
                    totals[item] += self.history[other][item] * similarity                    
                    
                    sumSimilar.setdefault(item, 0)
                    # Sum all item ratings by each user
                    sumSimilar[item] += similarity
         
        # Calculates weighted mean similarities
        self.rankings = [(total / sumSimilar[item], item) for item, total in totals.items()]
        self.rankings.sort(reverse=True)
        
        if len(self.rankings) > 30: self.rankings = self.rankings[0:30]
        
        return self.rankings
    
    def getRecommendItems(self, similarItems:list, target: str, by: str) -> list:
        """
        
        :return:
        """
        ratings = {}
        allSimilarities = {}
            
        self.checkContext(by)
        targetRatings = self.history[target]
        
        for (item, rating) in targetRatings.items():
            
            if item not in similarItems.keys(): continue
                
            for (similarity, item_2) in similarItems[item]:
                
                if item_2 in targetRatings: continue
            
                ratings.setdefault(item_2, 0)
                # Calculates the Weghted similarity
                ratings[item_2] += similarity * rating
                
                allSimilarities.setdefault(item_2, 0)                
                # Summatory each Weghted similarity
                allSimilarities[item_2] += similarity
                
        ## Claculates and List each Predict the rating user
        self.rank=[(score / allSimilarities[item], item) for item, score in ratings.items()]
        self.rank.sort(reverse=True)
        
        if len(self.rank) > 30: self.rank = self.rank[0:30]
        
        return self.rank
        
                
        