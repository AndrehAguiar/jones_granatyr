import pandas as pd


class NaiveBayes:
    
    """
    ##################################################################
    
    NaiveBayes(df:pd.DataFrame, target:str)
    
    -----------------------------------------------------------------
    
    get_nb() -> pd.DataFrame:
        Quando invocado retorna a tabela de probabilidades Naive Bayes
        :return: Pandas DataFrame
    
    -----------------------------------------------------------------
    
    get_data() -> pd.DataFrame:
        Quando invocado retorna os dados originais
        :return: Pandas DataFrame
    
    -----------------------------------------------------------------
    
    get_raw() -> pd.DataFrame:
        Quando invocado retorna a tabela com os dados originais actegorizados para classificação Naive Bayes
        :return: Pandas DataFrame
        
    ------------------------------------------------------------------
    
    classify(x: list) -> dict:
        Recebe a lista de propriedades do elemento para classificação
        :param x: list ['prop_1',...,'prop_n']
        :return: Pandas DataFrame
        
    ##################################################################
    """
    
    
    def __init__(self, df:pd.DataFrame, target:str):
        super(NaiveBayes, self).__init__()
        self.__df_raw = pd.DataFrame()
        self.__data = df
        self.__target = target
        self.__df = self.__build_df()
        
        
    def __format_columns(self, cols:list) -> pd.MultiIndex:
        """
        Quando invocado formata as colunas da tabela de probabilidades Naive Bayes
        :param cols: Lista de features do dataset original
        :return: Pandas MultiIndex
        """        
        
        if len(self.__df_raw) == 0: 
            df = self.__data
        else:
            df = self.__df_raw
            
        micolumns = []
        for col in cols:
            for val in df[col].unique():
                micolumns.append((col, val))

        micolumns.append(('Total','Proba'))
        
        return pd.MultiIndex.from_tuples(micolumns, names=['Classe',self.__target])
    
    
    def __prob_calculates(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        Quando invocado calcula as probabilidades de cada feature da tabela de probabilidades Naive Bayes
        :return: Pandas DataFrame
        """        
        for classe, col in self.__df.columns[:-1]:
            values = []
            
            for idx in self.__df.index:
                freq = len(df.query(f'{self.__target} == "{idx}" & {classe} == "{col}"'))
                freq_cls = len(df.query(f'{self.__target} == "{idx}"'))
                
                if freq == 0:
                    freq = 1

                values.append(freq / freq_cls)

            self.__df.loc[tuple(self.__df.index),(classe, col)] = values
            
        self.__df.loc[tuple(sorted(df[self.__target].unique())),("Total")] = (
            df[self.__target].value_counts() / len(df)).values
        
        return self.__df
    
    
    def __sum_calculates(self, df_x:pd.DataFrame) -> list:
        """
        Recebe o 'x' formatado como Pandas DataFrame e multiplica as probabilidades de cada classe
        :param x: Pandas DataFrame
        :return: List [prod_cls_1,...prod_cls_n
        """
        pro_probs = []
        for line in df_x.iterrows():
            p = 1
            for val in line[1].values:
                p*=val
            pro_probs.append(p)
        
        return pro_probs
    
    
    def __map_categ(self, x: float, quants: tuple) -> str:
        """
        Mapea o valor de acordo com o quartis da feature
        :param x: (float) Valor da feature de entrada
        :param quants: (tuple) Valores dos quartis específicos (q_25, q_75)
        :return: (str) Categoria 'Low'|'Normal'|'High'
        """
        if x <= quants[0]:
            return 'Low'
        elif x >= quants[1]:
            return 'High'
        else:
            return 'Normal' 
    
    
    def __format_df(self, col:str, classify:bool = False) -> None:
        """
        Quando invocado classifica cada dado em ['Low','Normal','High'], de acordo com a coluna [<= q_25, > q_25 & < q_75, >= q_75]
        :param col: (str) Nome da feature
        :param classify: (bool) Default False, se True retorna o (q_25, q_75) para classificação da entrada
        :return: None
        """
        
        q1 = self.__data[col].quantile(0.25)
        q3 = self.__data[col].quantile(0.75)
        
        if classify:
            return q1, q3
            
        self.__df_raw[col] = self.__data[col].apply(lambda x: self.__map_categ(x, (q1, q3)))
        
        
    def __check_types(self, cols:list) -> None:
        """
        Quando invocado verifica o tipo de dado de cada coluna
        :param cols: lista de features do Pandas DataFrame
        :return: None
        """
        for col in cols:
            if self.__data[col].dtype != 'object':
                self.__format_df(col)
        
    
    def __build_df(self) -> pd.DataFrame:
        """
        Quando invocado constroi a tabela de probabilidades Naive Bayes
        :return: Pandas DataFrame
        """        
        
        cols = self.__data.drop(self.__target, axis=1).columns
        self.__check_types(cols)
        
        df_mult = self.__format_columns(cols)
        
        print(len(self.__df_raw) == 0)
        
        if len(self.__df_raw) == 0:        
            self.__df = pd.DataFrame(columns = df_mult, index=sorted(self.__data[self.__target].unique()))
            return self.__prob_calculates(self.__data)
            
        else:
            self.__df_raw[self.__target] = self.__data[self.__target]
            self.__df = pd.DataFrame(columns = df_mult, index=sorted(self.__df_raw[self.__target].unique()))
            return self.__prob_calculates(self.__df_raw)
            
    
        
    def get_nb(self) -> pd.DataFrame:
        """
        Quando invocado retorna a tabela de probabilidades Naive Bayes
        :return: Pandas DataFrame
        """
        return self.__df
    
    
    def get_raw(self) -> pd.DataFrame:
        """
        Quando invocado retorna o DataFrame categórico formatado para classificação Naive Bayes
        :return: Pandas DataFrame
        """
        return self.__df_raw
    
    
    def get_data(self) -> pd.DataFrame:
        """
        Quando invocado retorna od dados originais
        :return: Pandas DataFrame
        """
        return self.__data
    
    
    def classify(self, x: list) -> dict:
        """
        Recebe a lista de propriedades do elemento para classificação
        :param x: list ['prop_1',...,'prop_n']
        :return: Pandas DataFrame
        """
        cols = self.__data.drop(self.__target, axis=1).columns
        for i, val in enumerate(x):
            if type(val) != str:
                x[i] = self.__map_categ(x[i], self.__format_df(cols[i], classify=True))
                
        x = [col for col in zip(cols, x)]
    
        df_x = self.__df.loc[tuple(self.__df.index), (x)].copy() 
        
        df_x[('Total','Proba')] = self.__df[('Total','Proba')]
        
        print(df_x)
        
        cls_prob = {}
        sum_probs = self.__sum_calculates(df_x)
        for i, val in enumerate(sum_probs):
            cls_prob[df_x.index[i]] = f'{round((val / sum(sum_probs)) * 100,2)}%'
            
        return cls_prob