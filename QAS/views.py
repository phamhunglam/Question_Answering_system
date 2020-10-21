from django.shortcuts import render
from django import forms
from QAmodel.main import system

class QuestionForm(forms.Form):
    question = forms.CharField(widget=forms.TextInput(attrs={'class':'special', 'size': '100'}))

questions = ""
labels = ""


def index(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question =form.cleaned_data["question"]
            questions,labels = system(question)
            print(question)
            return render(request, 'QAS/index.html',{
                "form":form,
                "questions":questions,
                "label": labels

            })
        else:
            return render(request,'QAS/index.html',{
                "form": form,
                "questions":questions
            })
    return render(request, "QAS/index.html",{
        "form": QuestionForm(),

    })