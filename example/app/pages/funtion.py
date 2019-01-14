from django.shortcuts import render


def post1(self, request):
    name = request.POST.get('data')
    print name
    return name
    # return render(request, 'arpschne.html', locals())