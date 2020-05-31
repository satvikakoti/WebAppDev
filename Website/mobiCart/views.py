from django.shortcuts import render
import csv

def first(request):
    return render(request,'frontpage.html')
def data(request):
    if request.method == 'POST':
        dict1 = request.POST
        with open('regdata.csv','a') as csvfile:
            wrt=csv.writer(csvfile)
            for key,value in dict1.items():
                wrt.writerow([key,value])

    return render(request, 'registerpage.html')
# Create your views here.
