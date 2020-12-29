from model.MinerEmotion import MinerEmotion

miner = MinerEmotion()
train_data, test_data = miner.getData()

print(f'length train: {len(train_data)}, length test: {len(test_data)}')

print(train_data[0])

print(miner.getLabels(plot=False))

train_data = miner.builddata(train_data)
test_data = miner.builddata(test_data)
model = miner.fit(train_data)
miner.eval(test_data)
miner.confmatrix(test_data)

test = 'estou feliz, hoje é um belo dia'
test = miner.classifyphrase(test)

test = 'não estou bem, meu cachorro morreu'
test = miner.classifyphrase(test)

test = 'estou com ódio disso, chega!'
test = miner.classifyphrase(test)

train_data, test_data = miner.selectLabels(['raiva', 'medo'])

print(f'length train: {len(train_data)}, length test: {len(test_data)}')

print(train_data[0])

print(miner.getLabels(plot=False))

train_data = miner.builddata(train_data)
test_data = miner.builddata(test_data)
model = miner.fit(train_data)
miner.eval(test_data)
miner.confmatrix(test_data)

test = 'estou com medo dequele homem'
test = miner.classifyphrase(test)

test = 'estou com ódio disso, chega!'
test = miner.classifyphrase(test)
