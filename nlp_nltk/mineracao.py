import nltk

# nltk.download()

base = [('eu sou admirada por muitos', 'alegria'),
        ('me sinto completamente amado', 'alegria'),
        ('amar e maravilhoso', 'alegria'),
        ('estou me sentindo muito animado novamente', 'alegria'),
        ('eu estou muito bem hoje', 'alegria'),
        ('que belo dia para dirigir um carro novo', 'alegria'),
        ('o dia está muito bonito', 'alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem', 'alegria'),
        ('o amor e lindo', 'alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]

# print(base[0])

stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

stopwordsnltk = nltk.corpus.stopwords.words('portuguese')


# print(stopwordsnltk)


def removestopwords(texto: list) -> list[tuple[list, str]]:
    frases = []
    for (palavras, emocao) in texto:
        semstop = [p for p in palavras.split() if p not in stopwordsnltk]
        frases.append((semstop, emocao))
    return frases


# print(removestopwords(base))


def aplicastemmer(texto) -> list[tuple[list, str]]:
    stemmer = nltk.stem.RSLPStemmer()
    frasesemstemming = []
    for (palavras, emocao) in texto:
        constemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwordsnltk]
        frasesemstemming.append((constemming, emocao))
    return frasesemstemming


frasescomstemming = aplicastemmer(base)


# print(frasescomstemming)

def buscapalavras(texto):
    todaspalavras = []
    for (palavras, emocao) in texto:
        todaspalavras.extend(palavras)
    return todaspalavras


# print(buscapalavras(aplicastemmer(base)))


def buscafrequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras


frequencia = buscafrequencia(
    buscapalavras(
        aplicastemmer(base)))


# print(frequencia.most_common(50))


def buscapalavrasunicas(frequencia):
    freq = frequencia.keys()
    return freq


palavrasunicas = buscapalavrasunicas(frequencia)


# print(palavrasunicas)


def extratorpalavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavras in palavrasunicas:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas


caracteristicasfrase = extratorpalavras(['am', 'nov', 'dia'])
# print(caracteristicasfrase)

basecompleta = nltk.classify.apply_features(extratorpalavras, frasescomstemming)
# print(basecompleta)
