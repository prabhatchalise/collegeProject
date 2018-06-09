import pickle
import features

loaded_model = pickle.load(open('learned_model.sav', 'rb'))

def sent_class(sentence):
    id = 1  # features needs an ID passing in at moment - maybe redundant?

    f = features.features_dict(str(id), sentence)
    fseries = features.features_series(f)
    width = len(fseries)
    fseries = fseries[1:width - 1]  # All but the first and last item (strip ID and null class off)

    # Get a classification prediction from the Model, based on supplied features
    sentence_class = loaded_model.predict([fseries])[0].strip()

    return sentence_class