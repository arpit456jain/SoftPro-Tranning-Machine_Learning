from django.shortcuts import render,redirect
from django.http import  HttpResponse
import os
import pickle

# priceperweek
# population
# monthlyincome
# avgparking
# Create your views here.
def home(request):

    return render(request,"index.html")
def test(request):
    if request.method == "POST":
        priceperweek = int(request.POST['priceperweek'])
        population = int(request.POST['population'])
        monthlyincome = int(request.POST['monthlyincome'])
        avgparking = int(request.POST['avgparking'])
        print(priceperweek,population,monthlyincome,avgparking)
        path = os.path.dirname(__file__) #this will provide root path of appliction
        print(path)
        model = pickle.load(open(os.path.join(path,"taxi.pkl"),'rb'))
        print(model)
        res = str(model.predict([[priceperweek,population,monthlyincome,avgparking]])[0].round(2))
        params={"res":res}
        return render(request,"index.html",params)
    else:
        return redirect('/')