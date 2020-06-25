from django.shortcuts import render, redirect
import random

def index(request):
    if 'totalgold' not in request.session:
        request.session['totalgold'] = 0
        # context = []
    if 'activity_log' not in request.session:
        request.session['activity_log'] = ['']

    #reverse(request.session['activity_log'])

        return render(request,'indexexample.html')

def process(request, location):
    if request.POST['location']== 'farm':
        goldearned = random.randint(10,20)
        request.session['totalgold']+=  goldearned
        event = f"went to farm and earned {goldearned}"
        request.session['activity_log'].append(event)


    elif request.POST['location']=='cave':
        goldearned = random.randint(2,5)
        request.session['totalgold']+= goldearned
    
    elif request.POST['location']=='casino':
        goldearned = random.randint[-50,50]
        request.session['totalgold'] += goldearned
        if goldearned >=0:
            event = f'went to casino and earned {goldearned}'
        else:
            event = f'went to casino and lost {abs(goldearned)}'
            request.session['activity_string'] = 'lost'

        request.session['activity_log'].append(event)


   # print(request.POST)
    return redirect('/')
