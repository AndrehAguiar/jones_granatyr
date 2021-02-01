import numpy as np
import scipy.stats as st


class Probability:
    
    def __init__(self):
        super(Probability, self).__init__()
        
        self.samples = {}
        self.targets = []
        
        
    def theor_prob(self, results:float, sample_space:float)->float:
        return results/sample_space
        
        
    def experiment(self, n_experiment:int)->dict:
        
        choices = list(self.samples.keys())
        dct_results = {choice:0 for choice in choices}

        for _ in range(n_experiment):
            dct_results[np.random.choice(choices)]+=1

        dct_results = {
            'Results':dct_results,
            f'Probability':self.theor_prob(dct_results[self.targets[0]],len(choices))
        }

        return dct_results
    
    
    def set_samples(self, samples:dict):
        self.samples = samples
        
        
    def set_targets(self, targets:list):
        self.targets = targets
        
        
    def count_sample(self, samples):

        space = 0
        for i, sample in enumerate(samples):
            space += sum(samples[sample].values())

        return space


    def count_part(self, targets, samples, p_type):
        part = 0
        for i, sample in enumerate(samples):
            part += samples[sample][targets[0][list(targets[0].keys())[0]][p_type]]

        return part
    
    
    def count_known(self, known):
        sum_known = 0
        for i, sample in enumerate(self.samples):
            sum_known += self.samples[sample][known]

        return sum_known


    def random_prob(self, targets, samples, replace, prob=1):
        
        self.s = samples.copy()

        for i, target in enumerate(targets):        
            prob *= self.s[target]/sum(self.s.values()) if target in self.s else 0        
            if not replace:            
                self.s[target]-=1

        return prob


    def and_prob(self, targets, samples, p_type='and'):

        return sum(samples[list(targets[0].keys())[0]].values()) / self.count_sample(samples)\
        * samples[list(targets[0].keys())[0]][targets[0][list(targets[0].keys())[0]][p_type]]\
        / sum(samples[list(targets[0].keys())[0]].values())


    def or_prob(self, targets, samples, p_type='or'):

        return (sum(samples[list(targets[0].keys())[0]].values()) / self.count_sample(samples))\
    + (self.count_part(targets, samples, p_type) / self.count_sample(samples))\
    - (samples[list(targets[0].keys())[0]][targets[0][list(targets[0].keys())[0]][p_type]] / self.count_sample(samples))


    def known_prob(self, targets, samples, p_type='known'):
        return (samples[list(targets[0].keys())[0]][targets[0][list(targets[0].keys())[0]][p_type]] / self.count_sample(samples))\
    /(self.count_part(targets, samples, p_type) / self.count_sample(samples))


    def cond_prob(self, p_type:str='random', event:int=1, replace:bool=False)->float:

        if p_type == 'random':
            return round(self.random_prob(self.targets, self.samples, replace), 4)

        if p_type == 'and':
            return round(self.and_prob(self.targets, self.samples),4)

        if p_type == 'or':
            return round(self.or_prob(self.targets, self.samples),4)

        if p_type == 'known':
            return round(self.known_prob(self.targets, self.samples),4)

        return prob
                                                     
                                                     
    def get_p(self, x:float, n:float)->float:
        return x / n

    def get_q(self, p:float)->float:
        return 1 - p

    def get_z(self, p:float, interval:tuple)->float:
        return (p - interval[0]) / interval[1]

    def get_interval(self, h:float, n:float):
        return h, ((h * self.get_q(h)) / n) ** 0.5

    def conf_interval(self, x:float, n:float, ci:int=90)->list:

        if ci == 90:
            z = 1.645
        elif ci == 95:
            z = 1.960
        elif ci == 99:
            z = 2.576
        else:
            return print('The CI needs to be 90, 95 or 99.')

        p = self.get_p(x, n)
        q = self.get_q(p)
        e = z * ((p * q / n)**0.5)

        return {'Interval':[round(p-e, 3), round(e+p, 3)],'E_margin':round(e, 3)}

    def hip_test(self, z:float):
        return round(0.5 - round(round(st.norm.cdf(round(z,2)),4)-0.5, 4), 4)*2