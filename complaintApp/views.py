from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Complaint, FeedbackUser
from django.db.models import Count

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('dashboard')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# def login_view(request):
#     # Check if the user is already authenticated
#     if request.user.is_authenticated:
#         # Redirect to dashboard if the user is already logged in
#         return redirect('dashboard')
    
#     # Handle login form submission
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('dashboard')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})







def login_view(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        # Redirect staff users to the admin dashboard
        if request.user.is_staff:
            return redirect('admin_dashboard')
        else:
            return redirect('dashboard')
    
    # Handle login form submission
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect staff users to the admin dashboard
                if user.is_staff:
                    return redirect('admin_dashboard')
                else:
                    return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})







# @login_required
# def dashboard(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         category = request.POST.get('category')
#         attachment = request.FILES.get('attachment')

#         if title and description and category:
#             Complaint.objects.create(
#                 user=request.user,
#                 title=title,
#                 description=description,
#                 category=category,
#                 attachment=attachment,

#             )

#     complaints = Complaint.objects.filter(user=request.user)
#     return render(request, 'dashboard.html', {'complaints': complaints})






@login_required
def dashboard(request):
    # Prevent staff from accessing the regular user dashboard
    if request.user.is_staff:
        return redirect('admin_dashboard')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        attachment = request.FILES.get('attachment')

        if title and description and category:
            Complaint.objects.create(
                user=request.user,
                title=title,
                description=description,
                category=category,
                attachment=attachment,
            )

    complaints = Complaint.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'complaints': complaints})





@login_required
def add_feedback(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback')
        if feedback_text:
            FeedbackUser.objects.create(
                complaint=complaint,
                user=request.user,
                text=feedback_text
            )
    return redirect('dashboard')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def signout_view(request):
    user = request.user
    user.delete()
    logout(request)
    return redirect('home')

@login_required
def user_complaints(request):
    complaints = Complaint.objects.filter(user=request.user)
    return render(request, 'user_complaints.html', {'complaints': complaints})

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')
    complaints = Complaint.objects.all()
    return render(request, 'admin_dashboard.html', {'complaints': complaints})

@login_required
def update_complaint_status(request, complaint_id, new_status):
    complaint = Complaint.objects.get(id=complaint_id)
    complaint.status = new_status
    complaint.save()
    send_mail(
        'Complaint Status Updated',
        f'Your complaint "{complaint.title}" status has been updated to {new_status}.',
        'admin@college.com',
        [complaint.user.email],
        fail_silently=False,
    )
    return redirect('admin_dashboard')

