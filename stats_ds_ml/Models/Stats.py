import pandas as pd
import numpy as np


class Stats:
    
    def __init__(self):
        """
        ######################################################################
        
        
        df_stats(data: pd.Series, h: int= None):
            -> data: Pandas Series, Numpy Array ou list object
            -> h: (int) Default None calcula o intervalo a partir da fórmula, se especificado, utiliza o valor como intervalo das classes.
            return: pd.DataFrame
        ----------------------------------------------------------------------- 
        
        get_stats(df: pd.DataFrame, quartis: bool = False):
            -> quartis: (bool) default False calcula a média, a moda e a mediana, se True calcula os quartis (0.25, 0.5, 0.75).
            return: tuple (media, moda, mediana) | quartil(0.25, 0.5, 0.75)
        -----------------------------------------------------------------------
        
        mode(data):
            return: numpy array
        -----------------------------------------------------------------------
        
        median(data):
            return: float
        -----------------------------------------------------------------------
        
        mean(data):
            return: float
        -----------------------------------------------------------------------
        
        geom_mean(data):
            return: float
        -----------------------------------------------------------------------
        
        harm_mean(data):
            return: float
        -----------------------------------------------------------------------
        
        sqrt_mean(data):
            return: float
        -----------------------------------------------------------------------
        
        variance(data):
            return: float
        -----------------------------------------------------------------------
        
        std_deviation(data):
            return: float
        -----------------------------------------------------------------------
        
        coef_deviation(data):
            return: float
        -----------------------------------------------------------------------
        
        grp_std_deviation(df):
            return: float
        
        ########################################################################
        """
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
        
        
    def __get_positon(self, df: pd.DataFrame, median: bool = False, q1: bool = False, q3: bool = False) -> float:
        
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
    
    def __rest(self, AA:int, h:int) -> int:
        """
        Recebe os valores da amplitude e intervalo e calcula o resto para ajuste
        :param AA: Amplitude dos dados
        :param h: Intervalo das classes
        :return: O resto para completar a última classe
        """
        last = (AA + h) // h 
        
        if AA % h != 0:
            last = AA // h
            
        return last
    
    
    def __get_interval(self, data: pd.Series, h: int = None) -> np.array:
        """
        Recebe os dados e o intervalo e calcula a almplitude com a fómula de 'sturges'
        :param data: Pandas Series, Numpy Array ou list object
        :param h: (int) Default None calcula o intervalo a partir da fórmula, se especificado, utiliza o valor como intervalo das classes.
        :return: Lista(int) com os valores do limite inferior das clases.
        """
        data = np.sort(data)
        data_min, data_max = data.min(), data.max()
        
        i = (1 + 3.3) * np.log10(len(data))
        if i % 2 != 0:
            i = ((i // 1) + 1)
            
        AA = data_max - data_min
        if h is None:
            h = AA // i        
            if AA % i != 0:
                h += 1
            
        return np.arange(data_min, data_max + self.__rest(AA, h), step = h).astype(int)
    
    
    def __get_classes(self, data: pd.Series, interval: np.array) -> list:
        """
        Recebe os dados e o intervalo e formata as classes
        :param data: Pandas Series, Numpy Array ou list object
        :return: Lista(str) com as classes
        """
        return [f'{str(interval[i])}-{str(interval[i + 1])}' for i in range(len(interval) - 1)]
    
    
    def __get_inferior(self, classes: list) -> list:
        """
        Recebe os dados e as classes e especifica o limite inferior de cada classe
        :param data: Pandas Series, Numpy Array ou list object
        :return: Lista(int) com os limites inferiores de cada classe
        """
        return [int(cls[:3]) for cls in classes]
    
            
    def __get_superior(self, classes: list) -> list:
        """
        Recebe os dados e as classes e especifica o limite superior de cada classe
        :param data: Pandas Series, Numpy Array ou list object
        :return: Lista(int) com os limites superiores de cada classe
        """
        return [int(cls[-3:]) for cls in classes]
    
    
    def __get_fi(self, data: pd.Series, interval: float) -> np.array:
        """
        Recebe os dados e o intervalo e calcula a frequência de cada intervalo(fi)
        :param data: Pandas Series, Numpy Array ou list object
        :return: Lista(int) com a frequência de cada classe
        """
        fi = []
        counter = 0
        for i in range(len(interval) - 1):
            for val in np.sort(data):
                if val in list(range(interval[i], interval[i + 1])):
                    counter +=1
            fi.append(counter)
            counter = 0
            
        return fi
                

    def __get_xi(self, classes: list) -> list:
        """
        Recebe as classes e calcula a mediana de cada classe(xi)
        :param data: Pandas Series, Numpy Array ou list object
        :return: Lista(int) com a mediana de cada classe
        """
        xi = []
        for cls in classes:
            xi.append(int(int(cls[:3]) + (int(cls[-3:]) - int(cls[:3])) / 2))
        
        return xi
                

    def __get_xi2(self, xi: list) -> list:
        """
        Recebe a mediana(xi) e calcula o quadrado da mediana de cada classe(xi**2)
        :param data: Pandas Series, Numpy Array ou list object
        :return: Lista(int) com o quadrado da mediana de cada classe
        """        
        return np.array(xi) ** 2
    
    
    def __get_fixi(self, fi: list, xi: list) -> list:
        """
        Recebe a frequência(fi) e a mediana(xi) e calcula o produto de fi pela mediana de cada classe(fi * xi)
        :param data: Pandas Series, Numpy Array ou list object
        :return: Lista(int) com o produto da frequência pela mediana de cada classe
        """
        return np.array(fi) * np.array(xi)
                

    def __get_fi_xi2(self, fi:list, xi_2: list) -> list:
        """
        Recebe a frequência(fi) e o quadrado da mediana(xi**2) e calcula o produto de fi pela mediana de cada classe(fi * xi)
        :param data: Pandas Series, Numpy Array ou list object
        :return: Lista(int) com o produto da frequência pela mediana de cada classe
        """        
        return np.array(fi) * np.array(xi_2)
    
    
    def __get_Fi(self, fi: list) -> list:
        """
        Recebe a frequência(fi) e calcula a soma acumulada para cada classe(Fi)
        :param data: Pandas Series, Numpy Array ou list object
        :return: Lista(int) com a soma acumulada de cada classe
        """
        Fi = []
        j = 0
        for i in fi:
            j += i
            Fi.append(j)
        
        return Fi
    
        
    def df_stats(self, data: pd.Series, h: int= None) -> pd.DataFrame:
        """
        Recebe os dados e faz os cálculos para geração do dataset (Pandas DataFrame)
        :param data:  Pandas Series, Numpy Array ou list object
        :param h: (int) Default None calcula o intervalo a partir da fórmula, se especificado, utiliza o valor como intervalo das classes.
        :return: Pandas DataFrame com as colunas [inferior, superior, fi, xi, fi_xi, xi2, fi_xi2, Fi]
        """
        
        if h is not None:
            interval = self.__get_interval(data, h)
        else:
            interval = self.__get_interval(data)
        
        classes = self.__get_classes(data, interval)
        fi = self.__get_fi(data, interval)
        xi = self.__get_xi(classes)
        xi_2 = self.__get_xi2(xi)
        
        data = {'gap':classes,
                'inferior':self.__get_inferior(classes),
                'superior':self.__get_superior(classes),
                'fi': fi,
                'xi': xi,
                'fi_xi': self.__get_fixi(fi, xi),
                'xi2':xi_2,
                'fi_xi2':self.__get_fi_xi2(fi, xi_2),
                'Fi':self.__get_Fi(fi)}
        
        df = pd.DataFrame(data)
        df.set_index('gap', drop=True, inplace=True)
        
        return df
    
    
    def grp_std_deviation(self, df: pd.DataFrame) -> float:
        """
        Recebe o pandas DataFrame de distribuição de frequência (DADOS AGRUPADOS)
        :params df: pandas Dataframe com as colunas [inferior, superior, fi, xi, fi_xi, xi2, fi_xi2, Fi]
        :return: (float) Desvio padrão dos dados agrupados
        """
        return ((df.fi_xi2.sum() / df.fi.sum()) - (df.fi_xi.sum() / df.fi.sum()) ** 2) ** 0.5
    
        
    def get_stats(self, df: pd.DataFrame, quartis: bool = False) -> tuple:
        
        """
        Recebe o pandas DataFrame de distribuição de frequência (DADOS AGRUPADOS)
        :params df: pandas Dataframe com as colunas [inferior, superior, fi, xi, fi_xi, Fi]
        :params quartis: (bool) default False calcula a média, a moda e a mediana, se True calcula os quartis (0.25, 0.5, 0.75).
        :return: tuple (media, moda, mediana) | (0.25, 0.5, 0.75)
        """  
        
        if not quartis:
            self.media = df['fi_xi'].sum() / df['fi'].sum()
            self.moda = df.query(f'fi == {df["fi"].max()}')['xi'].values[0]
            
        pos = self.__get_positon(df, median=True)
        self.mediana = self.__calculates(df, pos)

        pos = self.__get_positon(df, q1=True)
        self.q1 = self.__calculates(df, pos)
        
        pos = self.__get_positon(df, q3=True)
        self.q3 = self.__calculates(df, pos)
        
        if quartis:        
            return self.q1, self.mediana, self.q3
        else:
            return self.media, self.moda, self.mediana
        
        
    def mode(self, data: pd.Series) -> tuple:
        """
        Recebe os dados e calcula a moda
        :params data: Pandas Series, Numpy Array ou list object
        :return: numpy array
        """
        if type(data) != pd.Series:
            data = pd.Series(data)
        return data.mode().values, pd.Series(data).value_counts().max()
    
        
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
    
    
    def variance(self, data: pd.Series) -> float:
        """
        Recebe os dados e calcula a variância
        :params data: Pandas Series, Numpy Array ou list object
        :return: float
        """
        desvio = abs(data - self.mean(data)) ** 2
        soma_deviation = desvio.sum()
        return soma_deviation / len(data)
    
    
    def std_deviation(self, data: pd.Series) -> float:
        """
        Recebe os dados e calcula a desvio padrão
        :params data: Pandas Series, Numpy Array ou list object
        :return: float
        """
        return self.variance(data) ** 0.5
    
    def coef_deviation(self, data: pd.Series) -> float:
        """
        Recebe os dados e calcula coeficiante do desvio padrão
        :params data: Pandas Series, Numpy Array ou list object
        :return: float
        """
        return (self.std_deviation(data) / self.mean(data)) * 100
    