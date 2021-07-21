def prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title):
    import pickle
    x = [[pclass, sex, age, sibsp, parch, fare, embarked, title]]
    randomforest = pickle.load(open(
        'C:/Users/Admin/Desktop/Himesh/Courses taken/Udemy/Paid courses/Full stack web development and AI with Python (Django)/8. Setting up the site/titanic/titanic/myPredictor.sav', 'rb'))
    predictions = randomforest.predict(x)
    if predictions==0:
        predictions='survived'
    elif predictions==1:
        predictions=='not survived'
    else:
        predictions=='Error occured'
    return predictions
