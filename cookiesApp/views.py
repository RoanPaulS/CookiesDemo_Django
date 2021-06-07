from django.shortcuts import render

# Create your views here.

def cookies_count_view(request):
    count = request.COOKIES.get('counts',0)
    totalCount = int(count) + 1
    response = render(request,'cookiescount.html',{'count':totalCount})
    response.set_cookie('counts',totalCount)
    return response
