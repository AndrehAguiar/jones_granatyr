import nltk


class Classifier:

    def __init__(self):
        super(Classifier, self).__init__()
        """
        Recebe corpus: list[('document', 'class')...]
        """
        self.cls = nltk.NaiveBayesClassifier
        self.model = ''

    def fit(self, data_train:list[tuple[dict, str]]) -> nltk.NaiveBayesClassifier:
        """
        Train the model with classified data
        :param data_train: corpus preprecessed
        :return: nltk model trained
        """
        self.model = self.cls.train(data_train)
        return self.model

    def eval(self, data_test:list[tuple[dict, str]]):
        print(f'Accuracy: {nltk.classify.accuracy(self.model, data_test)}')

    def checkproba(self, doc: dict):
        """
        Calculates the probability for each label to document and print resutls
        :param doc: dictionary of words
        :return: None
        """
        prob = self.model.prob_classify(doc)
        for label in prob.samples():
            print('%s: %f' % (label, prob.prob(label)))

