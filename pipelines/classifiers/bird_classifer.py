from fastbook import *

MODEL_PATH = 'pipelines/models/bird_res34_v1.pkl'
def classify(image):
    learn_inferance = load_learner(MODEL_PATH)
    bird_class, index, probabilities = learn_inferance.predict(image)
    return_ =  {
        'bird_class' : bird_class,
        'probability' : probabilities[index].item()
    }
    return return_


