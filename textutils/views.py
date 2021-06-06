#made by shashank
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("hello")
# def about(request):
#     return HttpResponse('''<h1>shashank <a href="http://www.google.com" target="_blank">button</a> <a href="http://www.youtube.com" target="_blank">button2</a></h1>''')
#laying the pipeline
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
# def removepunc(request):
#     djtext = request.POST.get('text', 'default')
#     print(djtext)
#     return HttpResponse("remove punc")    
# def capfirst(request):
#     return HttpResponse("capatilize punc")       
def analyze(request):

    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('capatilize','off')
    countchar=request.POST.get('countchar','off')
    extraspaceremover=request.POST.get('extraspace','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not   in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        
    if fullcaps=="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capatilization', 'analyzed_text': analyzed}
        djtext = analyzed
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed    
    if countchar=="on":
        analyzed=djtext
        count=len(djtext)
        params = {'purpose': 'charcount', 'analyzed_text': analyzed,'count':str(count)}
        return render(request, 'analyze.html', params)
        djtext = analyzed

    if(removepunc != "on" and extraspaceremover!="on" and fullcaps!="on" and countchar!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)