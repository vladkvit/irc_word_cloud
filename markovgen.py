from pymarkovchain import MarkovChain
# Create an instance of the markov chain. By default, it uses MarkovChain.py's location to
# store and load its database files to. You probably want to give it another location, like so:
mc = MarkovChain("./markovdb.txt")

with open("../formatted.txt", "r") as myfile:
    data=myfile.read()

# To generate the markov chain's language model, in case it's not present
mc.generateDatabase(data)

# To let the markov chain generate some text, execute
#print( mc.generateString() )
print( mc.generateStringWithSeed("time") )