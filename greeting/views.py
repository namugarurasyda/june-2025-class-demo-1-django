from django.shortcuts import render

def index(request):
    """Render the home page with the name form"""
    return render(request, 'index.html')

def greet(request):
    """Greet the user by name"""
    if request.method == 'POST':
        name = request.POST.get('name', 'Guest')
        greeting_message = format_greeting(name)
        return render(request, 'greet.html', {'name': name, 'greeting': greeting_message})
    return render(request, 'index.html')

def format_greeting(name):
    """Format greeting message - separate function for testability"""
    return f"Hello, {name}! Welcome to our application."