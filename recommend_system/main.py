# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 19:30:48 2020

@author: TOP Artes
"""

from model.Recommend import Recommend

""" TEST base Ratings History """
#recommend = Recommend(testing = True)

""" recommend.getSimilar(<MOVIE TITLE or USER NAME>, <USER or ITEM>) """
#print(recommend.getSimilar('Star Trek', 'item'),'\n')
#print(recommend.getSimilar('Leonardo', 'user'),'\n')

#=======================================================#

""" recommend.getSimilarItems(<USER or ITEM>) """
#print(recommend.getSimilarItems('item'),'\n')
#print(''.center(50, '='),'\n\n')
#print(recommend.getSimilarItems('user'),'\n')
#print(''.center(50, '='),'\n\n')

#=======================================================#

""" recommend.getRecommendation(<MOVIE TITLE or USER NAME>) """
#print(recommend.getRecommendation('Star Wars', 'item'),'\n')
#print(recommend.getRecommendation('Janaina', 'user'),'\n')

#=======================================================#

""" recommend.getRecommendItems(<LIST ALL SIMILARITIES (USER or ITEM)>, <USER NAME or MOVIE TITLE>, <CONTEXT USER or ITEM>) """
#print(recommend.getRecommendItems(recommend.getSimilarItems('item'), 'Claudia', 'user'))
#print(recommend.getRecommendItems(recommend.getSimilarItems('user'), 'Freddy x Jason', 'item'))


"""######################################################"""

""" Movie Lens Ratings History """
recommend = Recommend()

""" recommend.getSimilar(<MOVIE ID or USER ID>, <CONTEXT USER or ITEM>) """
#print(' (Similarity between 0 and 1, id) '.center(50, '='))
#print(recommend.getSimilar('112', 'item'),'\n')
#print(''.center(50, '='),'\n\n')

#print(recommend.movies['112'], '(Movie title, Similarity between 0 and 1) '.ljust(50, '<'),'\n')
#print([(recommend.movies[id], si) for si, id in recommend.getSimilar('112', 'item')])
#print(''.center(50, '='),'\n\n')

#print(' (Similarity between 0 and 1, id) '.center(50, '='))
#print(recommend.getSimilar('3', 'user'),'\n')
#print(''.center(50, '='),'\n\n')

#=======================================================#

""" recommend.getSimilarItems(<CONTEXT USER or ITEM>) """
#print(recommend.getSimilarItems('item'),'\n') # It might take a while
#print(''.center(50, '='),'\n\n')
#print(recommend.getSimilarItems('user'),'\n') # It might take a while
#print(''.center(50, '='),'\n\n')

#=======================================================#

""" recommend.getRecommendation(<MOVIE ID or USER ID>, <CONTEXT USER or ITEM>) """
#print(recommend.movies['212'], ' Similar items recommendation (USER RATING PREDICTION between 1 and 5, id) '.center(50, '='), '\n')
#recommendations = recommend.getRecommendation('212', 'item')
#print(recommendations,'\n')
#print(''.center(50, '-'),'\n\n')
#print([(recommend.movies[id], si) for si, id in recommendations])
#print(''.center(50, '='),'\n\n')

#print(' USER recommendations (USER RATING PREDICTION between 1 and 5, Movie title) '.center(50, '='), '\n')
#print(recommend.getRecommendation('57', 'user'),'\n')
#print(''.center(50, '='),'\n\n')

#=======================================================#

""" recommend.getRecommendItems(<LIST ALL SIMILARITIES (USER or ITEM)>, <USER NAME or MOVIE TITLE>, <CONTEXT USER or ITEM>) """
#print(' Similar users recommendation (USER RATING PREDICTION between 1 and 5, Movie title) '.center(50, '='), '\n')
#recommendations = recommend.getRecommendItems(recommend.getSimilarItems('item'), '16', 'user') # It might take a while
#print([(recommend.movies[id], si) for si, id in recommendations])
#print(recommend.getRecommendItems(recommend.getSimilarItems('item'), '16', 'user')) # It might take a while
#print(''.center(50, '='),'\n\n')

print(recommend.movies['212'], ' Similar items recommendation (Movie title, USER RATING PREDICTION between 1 and 5) '.center(50, '='), '\n')
recommendations = recommend.getRecommendItems(recommend.getSimilarItems('user'), '212', 'item') # It might take a while
print([(recommend.movies[id], si) for si, id in recommendations])
print(''.center(50, '='),'\n\n')

