# Pickling
import pickle

# example_dict = {1:"6",2:"2",3:"f"}

# opening pickle dict to write bytes
# pickle_out = open("dict.pickle","wb")
# pickle.dump(example_dict, pickle_out)
# pickle_out.close()

# opening same file to read it
pickle_in = open("dict.pickle", "rb")
example_dict = pickle.load(pickle_in)

print(example_dict)
print(example_dict[2])



