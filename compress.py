import pickle
import bz2

# Load your trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Compress the model
with bz2.BZ2File('model.pkl.bz2', 'wb') as file:
    pickle.dump(model, file)
