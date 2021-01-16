import pandas as pd
import numpy as np


class Stats:
    
    def __init__(self):
        super(Stats, self).__init__()
        
        self.media = None
        self.moda = None
        self.mediana = None
        self.q1 = None
        self.q3 = None
        
    def __calculates(self, df: pd.DataFrame, fi: float) -> float:
        """
        Recebe o Pandas DataFrame e o índice do elemento médio da distribuição (fi) e busca a frequência acumulada (Fi) anterior ao elemento (fi)
        :params df: Pandas DataFrame
        :params fi: índice do elemento médio da distribuição
        :return: A mediana dos elementos da distribuição
        """
        
        lim_inferior, freq_class, id_freq_anterior, Fi_anterior = 0, 0, 0, 0
        for line in df.iterrows():

            lim_inferior = line[1][0]
            freq_class = line[1][2]
            id_freq_anterior = line[0]

            if line[1][5] >= fi:
                id_freq_anterior -= 1
                Fi_anterior = df.iloc[[id_freq_anterior]]['Fi']
                break

        return (lim_inferior + ((fi - Fi_anterior) * 4) / freq_class).values[0]
        
        
    def __get_fi(self, df: pd.DataFrame, median: bool = False, q1: bool = False, q3: bool = False) -> float:
        
        """
        Recebe o pandas DataFrame e o flag do valor (median, q1 ou q3)
        :param median: (bool), Default False, se True calcula a mediana
        :param q1: (bool), Default False, se True calcula a quartil 25%
        :param q3: (bool), Default False, se True calcula a quartil 75%
        :return: mediana | quartil 25% | quartil 75%
        """
        
        if median:            
            return df['fi'].sum() / 2        
        else:
            if q1:
                return df['fi'].sum() / 4
            else:
                if q3:
                    return (3 * df['fi'].sum()) / 4
        
        
    def get_stats(self, df: pd.DataFrame, quartis: bool = False) -> tuple:
        
        """
        Recebe o pandas DataFrame de distribuição de frequência (DADOS AGRUPADOS)
        :params df: pandas Dataframe com as colunas [inferior, superior, fi, xi, fi.xi, Fi]
        :params quartis: (bool) default Falsecalcula a média, a moda e a mediana, se True calcula os quartis (0.25, 0.5, 0.75).
        :return: tuple (media, moda, media) | (0.25, 0.5, 0.75)
        """  
        
        if not quartis:
            self.media = df['fi.xi'].sum() / df['fi'].sum()
            self.moda = df.query(f'fi == {df["fi"].max()}')['xi'].values[0]
            
        fi = self.__get_fi(df, median=True)
        self.mediana = self.__calculates(df, fi)

        fi = self.__get_fi(df, q1=True)
        self.q1 = self.__calculates(df, fi)
        
        fi = self.__get_fi(df, q3=True)
        self.q3 = self.__calculates(df, fi)
        
        if quartis:        
            return self.q1, self.mediana, self.q3
        else:
            return self.media, self.moda, self.mediana
        
    def mode(self, data: pd.Series) -> np.array:
        """
        Recebe os dados e calcula a moda
        :params data: Pandas Series, Numpy Array ou list object
        :return: numpy array
        """
        if type(data) != pd.Series:
            data = pd.Series(data)
        return data.mode().values
    
        
    def median(self, data: pd.Series) -> float:
        """
        Recebe os dados e calcula a mediana
        :params data: Pandas Series, Numpy Array ou list object
        :return: float
        """
        
        if type(data) != pd.Series:
            data = pd.Series(data).sort_values().reset_index(drop=True)
            
            
        if len(data) % 2 != 0:
            return data.sort_values().reset_index(drop=True)[(len(data) // 2)]
        
        median = (data[(len(data) / 2) - 1] + data[(len(data) / 2)]) / 2
        return median
        
        
    def mean(self, data: pd.Series) -> float:
        """
        Recebe os dados e calcula a média aritmética
        :params data: Pandas Series, Numpy Array ou list object
        :return: float
        """
        return sum(data) / len(data)
        
        
    def geom_mean(self, data: pd.Series) -> float:
        """
        Recebe os dados e calcula a média geométrica
        :params data: Pandas Series, Numpy Array ou list object
        :return: float
        """
        # return np.prod(data.astype(float)) ** (1/len(data))
        p = 1
        for i in range(0, len(data)-1, 2):
            p *= ((data[i] * data[i + 1]) ** (1 / len(data)))
        if len(data) % 2 != 0:
            p *= (data[len(data)-1]  ** (1 / len(data)))
        return p
    
    
    def harm_mean(self, data: pd.Series) -> float:
        """
        Recebe os dados e calcula a média harmônica
        :params data: Pandas Series, Numpy Array ou list object
        :return: float
        """
        return len(data) / sum(1/data)
    
    
    def sqrt_mean(self, data: pd.Series) -> float:
        """
        Recebe os dados e calcula a média quadrática
        :params data: Pandas Series, Numpy Array ou list object
        :return: float
        """
        return (sum(pow(n, 2) for n in data) / len(data)) ** 0.5