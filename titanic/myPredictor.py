def prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title):
    import pickle
    x = [[pclass, sex, age, sibsp, parch, fare, embarked, title]]
    randomforest = pickle.load(open(
        'titanic\myPredictor.sav', 'rb'))
    predictions = randomforest.predict(x)
    if predictions==0:
        predictions='survived'
    elif predictions==1:
        predictions=='not survived'
    else:
        predictions=='Error occured'
    return predictions
