from django.shortcuts import render, redirect, reverse
from . models import *
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


def registration(request):
    return render(request, 'id/registration.html')


def login(request):
    return render(request, 'id/login.html')


def dashboard(request):
    return render(request, 'id/dashboard.html')


def paper(request):
    return render(request, 'id/paper.html')


def ranking(request):
    rank = Submission.objects.all()
    return render(request, 'id/ranking.html', {'rank': rank})


def userregistration(request):
    if request.method == 'POST':
        name = request.POST['name']
        Email = request.POST['email']
        phone = request.POST['phone']
        password = make_password(request.POST['password'])
        if User.objects.filter(phone=phone).exists():
            messages.error(request, "phone number already exists")
            return redirect('registration/')

        elif User.objects.filter(email=Email).exists():
            messages.error(request, "email is already exists")
            return redirect('registration/')

        else:
            User.objects.create(name=name, email=Email,
                                phone=phone, password=password)
            return redirect('/login/')


def userlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_password = request.POST['password']
        if User.objects.filter(email=email).exists():
            obj = User.objects.get(email=email)
            password = obj.password
            user_name = obj.name
            user_id = obj.id
            if check_password(user_password, password):
                request.session['name'] = user_name
                request.session['user_id'] = user_id
                print(request.session)
                return redirect('/')
            else:
                return HttpResponse('password incorrect')
        else:
            return HttpResponse('email  is not registered')


def index(request):
    questio_id = 1
    nxt = questio_id + 1
    pre = questio_id - 1
    qm = questio_id
    pp = Questions.objects.all()
    qu = Questions.objects.get(id=questio_id)
    return render(request, 'id/index.html', {'qu': qu, 'nxt': nxt, 'pre': pre, 'pp': pp, 'qm': qm})


def question_detail_view(request, id):

    nxt = id + 1
    pre = id - 1
    qm = id

    qus = Questions.objects.all().count()
    print("qus")
    if qm > qus:
        return redirect('/index/')
    else:
        qu = Questions.objects.get(id=id)
        pq = Questions.objects.all()
        return render(request, 'id/index.html', {'qu': qu, 'nxt': nxt, 'pre': pre, 'pp': pq, 'qm': qm, 'qus': qus})

# def question_detail_view(request, question_id):
#     question = get_object_or_404(Questions, pk=question_id)
#     return render(request, 'id/index.html', {'question': question})


def attem(request):
    if request.method == 'POST':
        queattempt_id = request.POST['queattempt_id']
        queno = request.POST['queno']
        ans = request.POST['ans']
        student_id = request.POST['student_id']
        # marking = request.POST['marking']
        aw = Questions.objects.get(id=queno)
        if aw.correct_ans == ans:
            mark = True
        else:
            mark = False

        Attemp.objects.create(queattempt_id=queattempt_id,
                              queno=queno, ans=ans,
                              marking=mark, student_id=student_id
                              )

    return redirect(reverse('question', args=[queno]))


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

        return redirect('/index/')


def Sub_test(request):
    if request.method == 'POST':
        submitstatus = request.POST['submitstatus']
        attm = request.POST['attm']
        # corr_ans = request.POST['corr_ans']
        # totq = request.POST['totq']
        userid = request.POST['user_id']
        studentid = request.session["user_id"]
        att = User.objects.all()
        at = Attemp.objects.all()
        attemptt = 0
        for a in at:
            if a.student_id == studentid:
                attemptt = attemptt+1
        print(attemptt)

        apt = Questions.objects.all().count()
        counts = 0
        for b in at:
            if b.student_id == studentid:
                if b.marking == True:
                    counts = counts+1
        print(counts)
        percentage = 100*counts/int(apt)
        ot = Submission.objects.filter(user_id=studentid).delete()

        Submission.objects.create(submitstatus=submitstatus,
                                  corr_ans=counts,
                                  totq=apt,
                                  persentage=percentage,
                                  user_id=userid, attm=attm
                                  )

    return redirect('/ranking/', {'apt': apt})


def last_question_view(request, id):
    if int(id) == len(question):
        return redirect('index')
