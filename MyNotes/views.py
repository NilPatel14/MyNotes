from django.http import HttpResponse
from django.shortcuts import render,redirect
from Note.models import MyNote
from django.shortcuts import HttpResponseRedirect


def HomePage(request):
    try:
        if request.method == "POST":
            title = request.POST.get('title')
            content = request.POST.get('content')

            notes = MyNote(title=title,content=content)
            notes.save()
            return redirect('/shownote')
    except:
        pass
    return render(request,'index.html')

def ShowNote(request):
    NoteData = MyNote.objects.all()
    data={
        'NoteData' : NoteData
    }
    return render(request,'show.html',data)

def AddNote(request):
    try:
        if request.method == "POST":
            title = request.POST.get('title')
            content = request.POST.get('content')

            notes = MyNote(title=title,content=content)
            notes.save()
            return redirect('/shownote')
    except:
        pass
    return render(request,'index.html')


def deleteNote(request,id):
    try:
        notes = MyNote.objects.get(id=id)
        notes.delete()
        return redirect('/shownote')
    except:
        pass
    return render(request,'/shownote')

def updateNote(request,id):
    note={}
    notes = MyNote.objects.get(id=id)
    note={
        'title' : notes.title,
        'content' :  notes.content,
        'id' : notes.id
    }
    #notes.delete()
    return render(request,'update.html',note)

def update(request,id):
     if request.method == "POST":
            title = request.POST.get('title')
            content = request.POST.get('content')

            notes = MyNote(id=id,title=title,content=content)
            notes.save()
            return redirect('/shownote')
