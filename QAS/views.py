from django.shortcuts import render
from django import forms
from QAmodel.main import system

class QuestionForm(forms.Form):
    question = forms.CharField()

questions = ""



def index(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question =form.cleaned_data["question"]
            questions = system(question)
            print(question)
            return render(request, 'QAS/index.html',{
                "form":form,
                "questions":questions

            })
        else:
            return render(request,'QAS/index.html',{
                "form": form,
                "questions":questions
            })
    return render(request, "QAS/index.html",{
        "form": QuestionForm(),

    })