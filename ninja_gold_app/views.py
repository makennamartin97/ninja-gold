from django.shortcuts import render, redirect
import random

def index(request):
    #request.session['gold_amt'] = 'gold_amt'
    if 'gold_amt' not in request.session:
        request.session['gold_amt'] = 0

    if 'activity_log' not in request.session:
        request.session['activity_log'] = ['']
    
    return render(request,'index.html')

def process_money(request):
    if request.POST['place'] == 'farm':
        gold_earned = random.randint(10,20)
        request.session['gold_amt'] += gold_earned
        activity_string = f'Earned {gold_earned} golds from the farm!'
        request.session['activity_log'].append(activity_string)
    
    if request.POST['place'] == 'cave':
        gold_earned = random.randint(5, 10)
        request.session['gold_amt'] += gold_earned
        activity_string = f'Earned {gold_earned} golds from the cave!'
        request.session['activity_log'].append(activity_string)
    
    if request.POST['place'] == 'house':
        gold_earned = random.randint(2, 5)
        request.session['gold_amt'] += gold_earned
        activity_string = f'Earned {gold_earned} golds from the house!'
        request.session['activity_log'].append(activity_string)

    if request.POST['place'] == 'casino':
        gold_earned = random.randint(-50, 50)
        request.session['gold_amt'] += gold_earned
        if gold_earned >= 0:
            activity_string = f'Earned {gold_earned} from the casino!'
        else:
            activity_string = f'Lost {abs(gold_earned)} from the casino!'

        request.session['activity_log'].append(activity_string)

    return redirect('/')

#def place_process(request, place):
#    if place == "farm":
#        #request.session['gold_amt']

    
#    elif place == "cave":

    
#    elif place == "house":


#    elif place == "casino":

    
#    return redirect('/')

#def activity_string(request, activity_string):
