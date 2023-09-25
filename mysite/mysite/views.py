from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return  render(request,'index.html')
def analyze(request):
    text=request.POST.get('text')
    operation=request.POST.get('punc')
    operation1=request.POST.get('upper')
    operation2=request.POST.get('NewlineRemover')
    operation3=request.POST.get('extraspaceremover')
    operationDone=""
    if operation=='on':
        operationDone = operationDone + "  Punctuation Removed"
        analyzed=""
        punctuation='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for i in text:
            if i not in punctuation:
                analyzed=analyzed+i
        # textutils={'purpose':' Removed  Punctuation',"analyzed_text":analyzed}
        text=analyzed
        # return render(request, 'analyze.html', textutils)
    if operation1=='on':
        operationDone=operationDone+"  UpperCase Conversion"
        analyzed=""
        for i in text:
            analyzed=analyzed+i.upper()
        # textutils = {'purpose': 'Changed to Uppercase', "analyzed_text": analyzed}
        text = analyzed
        # return render(request, 'analyze.html', textutils)
    if operation2=='on':
        operationDone = operationDone + "  New Line Removed"
        analyzed = ""
        for i in text:
            if i!='\n' and i!='\r':
                analyzed = analyzed + i
        # textutils = {'purpose': 'Removed New Line', "analyzed_text": analyzed}
        text = analyzed
        # return render(request, 'analyze.html', textutils)
    if operation3=='on':
        operationDone = operationDone + "  ExtraSpace Removed"
        analyzed = ""
        for index,char in enumerate(text):
            print(index)
            if not(text[index]==" " and text[index+1]==" "):
                analyzed = analyzed + char
        # textutils = {'purpose': 'Removed Extra Line', "analyzed_text": analyzed}
        text = analyzed
        # return render(request, 'analyze.html', textutils)
    textutils = {'purpose': operationDone, "analyzed_text": text}
    if(operation3!='on' and operation2!='on' and operation1!='on' and operation!='on'):
        return HttpResponse("You have not Selected any operation")
    return render(request, 'analyze.html', textutils)