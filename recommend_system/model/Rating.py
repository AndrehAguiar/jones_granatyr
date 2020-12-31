# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 18:38:40 2020

@author: TOP Artes
"""

class Rating:
    
    def __init__(self, testing:bool):
        super(Rating, self).__init__()
        
        self.movies = {}
        self.__user_history = None
        self.__item_history = None
        self.__setHistory(testing)
    
    def __loadMovieLens(self, path = './ml-100k'):
        for line in open(path + '/u.item'):
            (id, title) = line.split('|')[0:2]
            self.movies[id]=title
            
        return self.__setRatings(self.movies, path)
        
    def __setRatings(self, movies: dict, path: str):
        base_user = {}
        base_item = {}
        for line in open(path + '/u.data'):
            (user, id_movie, rating, time) = line.split('\t')
            
            base_user.setdefault(user, {})
            base_user[user][movies[id_movie]] = float(rating)
            
            base_item.setdefault(id_movie, {})
            base_item[id_movie][user] = float(rating)
        
        self.__user_history = base_user
        self.__item_history = base_item
        
    
    def __setHistory(self, testing):
        if testing:
            self.__item_history = self.__getItemHist()
            self.__user_history = self.__getUserHist()
        else:
            self.__loadMovieLens()
        
    def __getUserHist(self):
        
        user_history = {
             'Ana': 
        		{'Freddy x Jason': 2.5, 
        		 'O Ultimato Bourne': 3.5,
        		 'Star Trek': 3.0, 
        		 'Exterminador do Futuro': 3.5, 
        		 'Norbit': 2.5, 
        		 'Star Wars': 3.0},
        	 
        	  'Marcos': 
        		{'Freddy x Jason': 3.0, 
        		 'O Ultimato Bourne': 3.5, 
        		 'Star Trek': 1.5, 
        		 'Exterminador do Futuro': 5.0, 
        		 'Star Wars': 3.0, 
        		 'Norbit': 3.5}, 
        
        	  'Pedro': 
        	    {'Freddy x Jason': 2.5, 
        		 'O Ultimato Bourne': 3.0,
        		 'Exterminador do Futuro': 3.5, 
        		 'Star Wars': 4.0},
        			 
        	  'Claudia': 
        		{'O Ultimato Bourne': 3.5, 
        		 'Star Trek': 3.0,
        		 'Star Wars': 4.5, 
        		 'Exterminador do Futuro': 4.0, 
        		 'Norbit': 2.5},
        				 
        	  'Adriano': 
        		{'Freddy x Jason': 3.0, 
        		 'O Ultimato Bourne': 4.0, 
        		 'Star Trek': 2.0, 
        		 'Exterminador do Futuro': 3.0, 
        		 'Star Wars': 3.0,
        		 'Norbit': 2.0}, 
        
        	  'Janaina': 
        	     {'Freddy x Jason': 3.0, 
        	      'O Ultimato Bourne': 4.0,
        	      'Star Wars': 3.0, 
        	      'Exterminador do Futuro': 5.0, 
        	      'Norbit': 3.5},
        			  
        	  'Leonardo': 
        	    {'O Ultimato Bourne':4.5,
                 'Norbit':1.0,
        	     'Exterminador do Futuro':4.0}
        }
        return user_history
    
        
    def __getItemHist(self):        

        item_history = {
            'Freddy x Jason': 
        		{'Ana': 2.5, 
        		 'Marcos': 3.0 ,
        		 'Pedro': 2.5, 
        		 'Adriano': 3.0, 
        		 'Janaina': 3.0 },
        	 
        	 'O Ultimato Bourne': 
        		{'Ana': 3.5, 
        		 'Marcos': 3.5,
        		 'Pedro': 3.0, 
        		 'Claudia': 3.5, 
        		 'Adriano': 4.0, 
        		 'Janaina': 4.0,
        		 'Leonardo': 4.5 },
        				 
        	 'Star Trek': 
        		{'Ana': 3.0, 
        		 'Marcos': 1.5,
        		 'Claudia': 3.0, 
        		 'Adriano': 2.0 },
        	
        	 'Exterminador do Futuro': 
        		{'Ana': 3.5, 
        		 'Marcos': 5.0 ,
        		 'Pedro': 3.5, 
        		 'Claudia': 4.0, 
        		 'Adriano': 3.0, 
        		 'Janaina': 5.0,
        		 'Leonardo': 4.0},
        				 
        	 'Norbit': 
        		{'Ana': 2.5, 
        		 'Marcos': 3.0 ,
        		 'Claudia': 2.5, 
        		 'Adriano': 2.0, 
        		 'Janaina': 3.5,
        		 'Leonardo': 1.0},
        				 
        	 'Star Wars': 
        		{'Ana': 3.0, 
        		 'Marcos': 3.5,
        		 'Pedro': 4.0, 
        		 'Claudia': 4.5, 
        		 'Adriano': 3.0, 
        		 'Janaina': 3.0}
        }  
        return item_history