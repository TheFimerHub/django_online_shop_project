from django.shortcuts import render  # type: ignore


def home_page(request):
    return render(request, 'catalog/home.html')

def contacts_page(request):
    if request.method == 'POST':
        # доп. задание
        name = request.POST.get('name')
        email = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {email} {message}')
    return render(request, 'catalog/contacts.html')