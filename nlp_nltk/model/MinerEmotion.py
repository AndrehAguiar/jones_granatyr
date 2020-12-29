import matplotlib.pyplot as plt
from model.Preprocess import Preprocess


class MinerEmotion(Preprocess):

    def __init__(self):
        super(MinerEmotion, self).__init__()

    def getData(self) -> tuple[list[tuple[str, str]], list[tuple[str, str]]]:
        """
        Get de data in de Corpus class
        :return: tuple(data_train, data_test)
        """
        return self.data_train, self.data_test

    def getLabels(self, train: bool = True, plot: bool = False) -> dict:
        """
        Count each label in the data_train or data_test
        :param train: Default True, if False count the data_test
        :param plot: Default False, if True plot a barplot
        :return: dictionary {label: frequency}
        """
        data = self.data_train if train else self.data_test
        labels = [label for (_, label) in data]
        dct_label = {label: labels.count(label) for label in set(labels)}
        if plot:
            self.plotLabels(dct_label)
        return dct_label

    def selectLabels(self, labels: list) -> tuple[list[tuple[str, str]], list[tuple[str, str]]]:
        """
        Select the documents in data with especific label
        :param labels: list of labels chosed
        :return: tuple(data_train, data_test)
        """
        self.data_train = [doc for doc in self.data_train if doc[1] in list(labels)]
        self.data_test = [doc for doc in self.data_test if doc[1] in list(labels)]
        return self.data_train, self.data_test

    def classifyphrase(self, phrase: str) -> dict:
        print(f"\nPhrase: {phrase}")
        phrase = [(phrase, '')]
        case = self.extractfeatures(
            self.builddata(phrase, train=False))

        self.checkproba(case)  # Imprime a lista de probabilidade das classes

        result = self.model.classify(case)
        prob = self.model.prob_classify(case).prob(result)
        print(f"Case: {case}\nClass: {result}, Probability: {prob}")
        print(''.center(50,'-'))
        return {'result': result, 'prob': prob}

    def plotLabels(self, labels: dict):
        """
        Plot the bar plot with the labels and frequency
        :param labels: dictionary {label: frequency}
        :return: None
        """
        plt.bar(list(labels.keys()), list(labels.values()))
        plt.title('Label frequency in data')
        plt.ylabel('FREQUENCY')
        plt.xlabel('LABEL')
        plt.grid()
        plt.show()
