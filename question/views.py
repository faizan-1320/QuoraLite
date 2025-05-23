from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question
from .forms import QuestionForm


def home(request):
    questions = Question.objects.all().order_by("-created_at")
    return render(request, "home.html", {"questions": questions})


@login_required(login_url="/user/login/")
def post_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect("home")  # Redirect to home or the page you want
    else:
        form = QuestionForm()
    return render(request, "post_question.html", {"form": form})    
