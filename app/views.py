from django.shortcuts import render, redirect
from . models import *

# Create your views here.


def index(request):
    questio_id = 2
    nxt = questio_id + 1
    pre = questio_id - 1
    pp = Questions.objects.all()
    qu = Questions.objects.get(id=questio_id)
    return render(request, 'id/index.html', {'qu': qu, 'nxt':nxt,'pre':pre,'pp':pp})


def question_detail_view(request,id):

    nxt = id + 1 
    pre = id - 1
    qu = Questions.objects.get(id=id)
    pq = Questions.objects.all()
    return render(request, 'id/index.html', {'qu': qu, 'nxt':nxt, 'pre':pre, 'pp':pq})

# def question_detail_view(request, question_id):
#     question = get_object_or_404(Questions, pk=question_id)
#     return render(request, 'id/index.html', {'question': question})


def attem(request):
    if request.method == 'POST':
        queattempt_id = request.POST['queattempt_id']
        queno = request.POST['queno']
        ans = request.POST['ans']
        marking = request.POST['marking']
        aw = Questions.objects.get(id = queno)
        if aw.correct_ans == ans :
            mark = 1
        else:
            mark = 0    



        Attemp.objects.create(queattempt_id=queattempt_id,
                              queno=queno, ans=ans,
                              marking=marking)

    return redirect('/')


def addquestion(request):
    return render(request, 'id/addquestion.html')


def questions(request):
    if request.method == 'POST':
        question = request.POST['question']
        option_1 = request.POST['option_1']
        option_2 = request.POST['option_2']
        option_3 = request.POST['option_3']
        option_4 = request.POST['option_4']
        correct_ans = request.POST['correct_ans']

        Questions.objects.create(question=question,
                                 option_1=option_1,
                                 option_2=option_2,
                                 option_3=option_3,
                                 option_4=option_4,
                                 correct_ans=correct_ans)

        return redirect('/question_detail_view/')
