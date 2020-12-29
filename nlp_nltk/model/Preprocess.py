import nltk
from model.EmotionNBClassifier import Classifier


class Preprocess(Classifier):

    def __init__(self):
        super(Preprocess, self).__init__()

        self.stoptwords = nltk.corpus.stopwords.words('portuguese')
        self.stemmer = nltk.stem.RSLPStemmer()

    def cleancorpus(self, corpus: list[tuple]) -> list[tuple[list, str]]:
        """
        Remove stop words from each doc
        :param corpus: List of tuples ('document','label')
        :return: List of tuples (['word',...'word_n'],'label')
        """
        self.stoptwords.extend(['palavra','palavras','vou','tão','ser','todo','toda','tudo','vai','minha','meu','fico','fica','pode','posso',
                                'algum', 'alguém','criança','ninguem','hoje','deixa','alguma','acho','acha','alguns','algumas','alguém',
                                'alguem','ver','dinheiro','lugar','parece','ficou','vamos','olho','olhou','olhar','perto','longe','ficou','ficar',
                                'todos','todas','completo','completa','nada','pessoa','quero','quer','nunca','sempre','passo','passa','passou',
                                'completa','assim','sei','como','com','tanto','conto','conta','contou','conto','contar','comer','olhando','estou',
                                'está','esta','a', 'agora', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e',
                                'ir', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
                                'tenha', 'teve', 'tive', 'um', 'uma', 'umas', 'uns'])
        phrases = []
        for (words, label) in corpus:
            cleanwords = [word.replace('?', '').replace('!', '') for word in words.split() if
                          word not in self.stoptwords]
            phrases.append((cleanwords, label))
        return phrases

    def applystemmer(self, corpus: list[tuple]) -> list[tuple[list, str]]:
        """
        Extract the root of each word
        :param corpus: List of tuples ('document','label')
        :return: List of tuples (['word',...'word_n'],'label')
        """
        phrases = []
        for (words, label) in corpus:
            rootword = [str(self.stemmer.stem(word)) for word in words]
            phrases.append((rootword, label))
        return phrases

    def searchwords(self, corpus: list[tuple]) -> list[str]:
        """
        List each root word in the corpus
        :param corpus: List of tuples ('document','label')
        :return: List of ['rootword',...'rootword_n']
        """
        allwords = []
        for (words, label) in corpus:
            allwords.extend(words)
        return allwords

    def countwords(self, words: list) -> list[tuple[str, int]]:
        """
        List of words in the corpus
        :param words: List of tuples ('document','label')
        :return: List of ['rootword',...'rootword_n']
        """
        words = nltk.FreqDist(words)
        return words

    def setwords(self, words: list) -> list[tuple['str', int]]:
        """
        nltk.FreqDist object
        :param words: List of tuples ('rootword', freq)
        :return: List of ['rootword',...'rootword_n']
        """
        freq = words.keys()
        return freq

    def extractfeatures(self, document: list) -> dict:
        """
        Check if the word exits in dictionary
        :param document: List of root words ['rootword',...,'rootword_n']
        :return: List of ['rootword',...'rootword_n']
        """
        doc = set(document)
        features = {}
        for word in doc:
            features['%s' % word] = (word in doc)
        return features

    def builddata(self, corpus: list[tuple], train: bool = True) -> list[tuple[dict, str]]:
        """
        Build the corpus with the format to train, test and classify
        :param corpus:  Data raw -> List of tuples ('document','label') if train else string
        :param train: Default True, if False preprocess the document without label
        :return: prerpocessed corpus or document
        """
        data_train = nltk.classify.apply_features(self.extractfeatures,
                                                  self.applystemmer(self.cleancorpus(corpus)))
        if train:
            return data_train
        else:
            return list(data_train[0][0].keys())
