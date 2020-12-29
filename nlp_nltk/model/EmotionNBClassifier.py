from nltk.metrics import ConfusionMatrix
from model.Corpus import Corpus
import nltk


# Uncomment the line below to download the NLTK contents
# nltk.download()

class Classifier(Corpus):

    def __init__(self):
        super(Classifier, self).__init__()
        """
        Recebe corpus: list[('document', 'class')...]
        """
        self.cls = nltk.NaiveBayesClassifier
        self.model = ''

    def fit(self, data_train: list[tuple[dict, str]]) -> nltk.NaiveBayesClassifier:
        """
        Train the model with classified data
        :param data_train: corpus preprecessed
        :return: nltk model trained
        """
        self.model = self.cls.train(data_train)
        return self.model

    def eval(self, data_test: list[tuple[dict, str]]) -> dict:
        """
        Calculates the model accuracy to test data
        :param data_test:  corpus preprocessed
        :return:  Dictionary {Accuracy: model accuracy}
        """
        acc = nltk.classify.accuracy(self.model, data_test)
        print(f'Accuracy: {acc}')
        return {'Accuracy': acc}

    def checkerrors(self, data_test: list[tuple[dict, str]]) -> list[tuple[str, bool]]:
        """
        Ckeck if words exists in the model and wrong classifies
        :param data_test: list of Documents preprocessed
        :return: list with the wrong classifies documents
        """
        errors = []
        for (phrase, label) in data_test:
            result = self.model.classify(phrase)
            if result != label:
                errors.append((label, result, phrase))

        return errors

    def checkproba(self, doc: dict) -> dict:
        """
        Calculates the probability for each label to document and print resutls
        :param doc: dictionary of words
        :return: Dictionary {label: probability}
        """
        dct_prob = {}
        prob = self.model.prob_classify(doc)
        print(' Probabilities Labels '.center(50, '='))
        for label in prob.samples():
            print('%s: %f' % (label, prob.prob(label)))
            dct_prob[label] = prob.prob(label)

        print(''.center(50, '='))
        return dct_prob

    def confmatrix(self, data_test: list[tuple[dict, str]]) -> ConfusionMatrix:
        """
        Classify each document in the test data and print the confusion matrix
        :param data_test: list of Documents preprocessed
        :return: NLTK Metrics ConfusionMatrix
        """
        expected = []
        predicted = []
        for (phrase, label) in data_test:
            result = self.model.classify(phrase)
            predicted.append(result)
            expected.append(label)

        matrix = ConfusionMatrix(expected, predicted)
        print(matrix)
        return matrix
