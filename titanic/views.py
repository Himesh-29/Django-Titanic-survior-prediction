from django.shortcuts import render
from . import myPredictor


def home(request):
    return render(request, 'index.html')


def wrongInput(request):
    return render(request, 'wrongInput.html')


def predict(request):
    user_pclass = float(request.GET['pclass'])
    user_sex = request.GET['sex']
    user_age = float(request.GET['age'])
    user_sibsp = float(request.GET['sibsp'])
    user_parch = float(request.GET['parch'])
    user_fare = float(request.GET['fare'])
    user_embarked = request.GET['embarked']
    user_title = request.GET['title']

    if(user_pclass == '' or user_sex == '' or user_age == '' or user_sibsp == '' or user_fare == '' or user_embarked == '' or user_title == ''):
        return render(request, 'wrongInput.html')

    if user_sex.lower() == 'male':
        user_sex = 0
    else:
        user_sex = 1

    if user_embarked.lower() == 's':
        user_embarked = 0
    elif user_embarked.lower() == 'c':
        user_embarked = 1
    elif user_embarked.lower() == 'q':
        user_embarked = 2

    if user_title.title() == 'Mr':
        user_title = 0
    elif user_title.title() == 'Miss':
        user_title = 1
    elif user_title.title() == 'Mrs':
        user_title = 2
    elif user_title.title() == 'Master':
        user_title = 3
    elif user_title.title() == 'Officer':
        user_title = 4
    elif user_title.title() == 'Dr':
        user_title = 5
    elif user_title.title() == 'Royalty':
        user_title = 6

    user_survived = myPredictor.prediction_model(
        user_pclass, user_sex, user_age, user_sibsp, user_parch, user_fare, user_embarked, user_title)

    return render(request, 'predict.html', {'user_survived': user_survived})
