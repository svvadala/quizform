from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuizForm



def quiz(request):

    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            q1 = form.cleaned_data['question_one']
            q2 = form.cleaned_data['question_two']
            q3 = form.cleaned_data['question_three']
            q4 = form.cleaned_data['question_four']
            q5 = form.cleaned_data['question_five']
            q6 = form.cleaned_data['question_six']

            print(q1,q2,q3,q4,q5,q6)




    form = QuizForm()
    return render(request, 'form.html',{'form': form})
