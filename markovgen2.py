import markovgenerator

with open('../formatted.txt', 'r') as f:
    text = f.read()

text = text.decode('utf-8').replace(u'\u014c\u0106\u014d','-')
text = text.lower()

markov_gen = markovgenerator.markovgenerator.MarkovGenerator(text, 200, 2)

print( markov_gen.generate_words() )