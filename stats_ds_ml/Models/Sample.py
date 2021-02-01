"""
Uncomment the lines below to install the libraries
"""
# Necessaries libraries
#!pip install pandas
#!pip install numpy
#!pip install random
#!pip install sklearn

# Importing libs
import pandas as pd
import numpy as np
import random as rd

from sklearn.model_selection import StratifiedShuffleSplit


class Sample:
    """
    simple_sample(df, sample_size, seed):
        return a random simple sample pandas DataFrame
    --------------------------------------------------
    systematic_sample(df, sample_size, seed):
        return a systematic sample pandas DataFrame
    -------------------------------------------------
    group_sample(df, n_groups, seed):
        return a group sample pandas DataFrame
    -------------------------------------------------
    stratify_sample(df, feat, sample_size, seed):
        return: stratified sample pandas DataFrame
    -------------------------------------------------
    reservoir_sample(df, sample_size):
        return: reservoir sample pandas DataFrame
    """
    
    def __init__(self):
        super(Sample, self).__init__()
        
        self.df_sp_sample = None
        self.df_sys_sample = None
        self.df_grp_sample = None
        self.df_stf_sample = None
        self.df_res_sample = None
        
        
    def simple_sample(self, df: pd.DataFrame, sample_size: int, seed: int = None) -> pd.DataFrame:
        """
        Receive the DataFrame and select randomly individuals.
            :param df: Pandas DataFrame with the population
            :param sample_size: Number of individuals in sample
            :param seed: Number to generate the random seed
            :return: random simple sample pandas DataFrame
        """
        self.df_sp_sample = df.sample(n = sample_size, random_state = seed)
        return self.df_sp_sample
    
    def systematic_sample(self, df: pd.DataFrame, sample_size: int, seed: int = None)->pd.DataFrame:
        """
        Receive the DataFrame and select systematically the individual in each interval.
            :param df: Pandas DataFrame with the population
            :param interval: Interval between each individual
            :param seed: Number to generate the random seed
            :return: systematic sample pandas DataFrame
        """
        interval = len(df) // sample_size
        rd.seed(seed)
        start = rd.randint(0, interval)
        idx = np.arange(start, len(df), step = interval)
        self.df_sys_sample = df.iloc[idx]
        
        return self.df_sys_sample
    
    def group_sample(self, df:pd.DataFrame, n_groups: int, seed: int = None) -> pd.DataFrame:
        """
        Receive the DataFrame and select a group from the population divided by n_groups.
            :param df: Pandas DataFrame with the population
            :param n_groups: Number of groups to select
            :param seed: Number to generate the random seed
            :return: group sample pandas DataFrame
        """
        df_grp = df.copy()
        interval = len(df_grp) / n_groups
        groups = []
        id_group = 0
        counter = 0

        for _ in df.iterrows():
            groups.append(id_group)
            counter += 1
            if counter >= interval:
                counter = 0
                id_group += 1

        df_grp['group'] = groups
        rd.seed(seed)
        grp_selected = rd.randint(df_grp.index[0], n_groups)

        self.df_grp_sample = df_grp[df_grp['group'] == grp_selected] 

        return  self.df_grp_sample
    
    def stratify_sample(self, df:pd.DataFrame, feat:str, sample_size: int, seed: int = None) -> pd.DataFrame:
        """
        Receive the DataFrame and select by the specified feature proportionally.
            :param df: Pandas DataFrame with the population
            :param feat: Specif feature to balance the sample
            :param sample_size: Number of individuals in sample
            :param seed: Number to generate the random seed
            :return: balanced sample pandas DataFrame
        """
        test_size = sample_size / len(df)
        split = StratifiedShuffleSplit(test_size = test_size, random_state = seed)

        for _, y in split.split(df, df[feat]):
            self.df_stf_sample = df.iloc[y]

        return self.df_stf_sample
    
    
    def reservoir_sample(self, df: pd.DataFrame, sample_size: int) -> pd.DataFrame:
        """
        Receive the DataFrame and select randomly each individual in population.
            :param df: Pandas DataFrame with the population
            :param sample_size: Number of individuals in sample
            :param seed: Number to generate the random seed
            :return: reservoir sample pandas DataFrame
        """
        i = 0
        size = len(df)
        stream = list(range(0, size))
        reservoir = list(np.zeros(sample_size).astype(int))

        while i < size:
            j = rd.randrange(i + 1)
            if j < sample_size:
                reservoir[j] = stream[i]
            i += 1
            
        self.df_res_sample = df.iloc[reservoir]

        return self.df_res_sample

