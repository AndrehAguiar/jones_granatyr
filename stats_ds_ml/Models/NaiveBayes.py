import pandas as pd


class NaiveBayes:
    
    
    def __init__(self, df:pd.DataFrame, target:str):
        super(NaiveBayes, self).__init__()
        self.data = df
        self.target = target
        self.df = self.__build_df()
        
        
    def __format_columns(self, cols:list) -> pd.MultiIndex:
        
        micolumns = []
        for col in cols:
            for val in self.data[col].unique():
                micolumns.append((col, val))

        micolumns.append(('Total','Proba'))
        
        return pd.MultiIndex.from_tuples(micolumns, names=['Classe',self.target])
    
    
    def __prob_calculates(self) -> pd.DataFrame:
        
       
        for classe, col in self.df.columns[:-1]:
            values = []
            for idx in self.df.index:
                freq = len(self.data.query(f'{self.target} == "{idx}" & {classe} == "{col}"'))
                freq_cls = len(self.data.query(f'{self.target} == "{idx}"'))
                if freq == 0:
                    freq = 1

                values.append(freq / freq_cls)

            self.df.loc[tuple(self.df.index),(classe, col)] = values
            
        self.df.loc[tuple(sorted(self.data[self.target].unique())),("Total")] = (
            self.data[self.target].value_counts() / len(self.data)).values
            
        return self.df
        
    
    def __build_df(self) -> pd.DataFrame:
        
        cols = self.data.drop(self.target, axis=1).columns
        
        df_mult = self.__format_columns(cols)
        self.df = pd.DataFrame(columns = df_mult, index=sorted(self.data[self.target].unique()))
        
        return self.__prob_calculates()
    
    def __sum_calculates(self, df_x:pd.DataFrame):
        sum_probs = []
        for line in df_x.iterrows():
            p = 1
            for val in line[1].values:
                p*=val
            sum_probs.append(p)
        
        return sum_probs
    
        
    def get_nb(self):
        return self.df
    
    
    def classify(self, x: list) -> dict:
        cols = self.data.drop(self.target, axis=1).columns
        x = [col for col in zip(cols, x)]
        
        df_x = self.df.loc[tuple(self.df.index), (x)].copy()
        df_x[('Total','Proba')] = self.df[('Total','Proba')]
        
        cls_prob = {}
        sum_probs = self.__sum_calculates(df_x)
        for i, val in enumerate(sum_probs):
            cls_prob[df_x.index[i]] = f'{round((val / sum(sum_probs)) * 100,2)}%'
            
        return cls_prob