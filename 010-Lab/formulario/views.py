from django.shortcuts import render

# Create your views here.
def post_form(request):
    return render(request,'formulario/post_form.html',{})
