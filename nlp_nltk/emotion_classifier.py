from model.Preprocess import Preprocess
from model.Corpus import Corpus

preprocess = Preprocess()
corpus = Corpus()

data_train = corpus.data_train
data_test = corpus.data_test

data_train = preprocess.cleancorpus(data_train)  # Remove stop words
data_train = preprocess.applystemmer(data_train)  # Extrai a raiz da palavra
lst_words = preprocess.searchwords(data_train)  # Lista todas as palavras
set_words = preprocess.countwords(lst_words)  # Lista e conta cada palavra
set_words = preprocess.setwords(set_words)  # Lista as palavras (únicas)
features = preprocess.extractfeatures(data_train[0][0])  # Extrai as features do documento

data_train = preprocess.builddata(corpus.data_train)  # Constroi a base de dados com os documentos pré-processados
model = preprocess.fit(data_train)
labels = model.labels() # Imprime a lista de probabilidade das classes

# print(labels)

data_test = preprocess.builddata(corpus.data_test)
preprocess.eval(data_test)

def classifyphrase(phrase: str):
    phrase = [(phrase, '')]
    test = preprocess.extractfeatures(
        preprocess.builddata(phrase, train=False))

    preprocess.checkproba(test) # Imprime a lista de probabilidade das classes

    result = model.classify(test)
    prob = model.prob_classify(test).prob(result)
    print(f"Class: {result}, Probability: {prob}")
    return {'result': result, 'prob': prob}


# test = classifyphrase('hoje é um belo dia')
# test = classifyphrase('eu sinto amor por voce')
print(model.show_most_informative_features(30))
