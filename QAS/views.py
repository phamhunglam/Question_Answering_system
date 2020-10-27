from django.shortcuts import render
from django import forms
from QAmodel.main import system

class QuestionForm(forms.Form):
    question = forms.CharField(widget=forms.TextInput(attrs={'class':'special', 'size': '100'}))

questions_ans = []
labels = ""


def index(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question =form.cleaned_data["question"]
            answer,labels = system(question)
            questions_ans.append(question + ": " + answer)
            return render(request, 'QAS/index.html',{
                "form":form,
                "questions_ans":questions_ans,
                "label": labels,
                "localanswer": answer

            })
        else:
            return render(request,'QAS/index.html',{
                "form": form,
                "questions_ans":questions_ans,
            })
    return render(request, "QAS/index.html",{
        "form": QuestionForm(),

    })