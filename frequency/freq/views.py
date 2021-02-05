from django.shortcuts import render,redirect
from .forms import URLForm
from .func import freq
from django.views.generic import FormView 
# Create your views here.
from .models import Url
from django.contrib import messages

class URLFormView(FormView):
    template_name = "url.html"
    form_class = URLForm
    success_url = "/result/"

    def post(self, request, *args, **kwargs):
        form = URLForm(self.request.POST or None)    
        if form.is_valid():
            url = form.cleaned_data.get("url")
                
            request.session['url'] = url        
               
            return redirect("freq")
        else:
            messages.warning(request, "wrong uuid or key")
            return redirect("/result")

def noti(request):
    url = request.session.get('url')
    x= freq(url) 
        
    if Url.objects.filter(url=url).exists():
        y=Url.objects.get(url=url)
        messages.warning(request, "Data is already avaliable!")
        return render(request,"result.html",{'y':y})
    y=Url.objects.create(url=url,word1=x[0][0],freq1=x[0][1],word2=x[1][0],freq2=x[1][1],word3=x[2][0],freq3=x[2][1],word4=x[3][0],freq4=x[3][1],word5=x[4][0],freq5=x[4][1],word6=x[5][0],freq6=x[5][1],word7=x[6][0],freq7=x[6][1],word8=x[7][0],freq8=x[7][1],word9=x[8][0],freq9=x[8][1],word10=x[9][0],freq10=x[9][1])
    messages.info(request, "Data Created Successfully!")
    return render(request,"result.html",{'y':y})
    