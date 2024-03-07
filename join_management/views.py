from django.shortcuts import render, redirect
from .forms import JoinManagementForm
from .models import JoinManagement

def management_join_form(request):
    if request.method == 'POST':
        form = JoinManagementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to success page after successful submission
    else:
        form = JoinManagementForm()
    return render(request, 'join_management/management_join_form.html', {'form': form})



from django.shortcuts import render

def success_view(request):
    return render(request, 'join_management/success.html')



def display_data(request):
    data = JoinManagement.objects.all()
    return render(request, 'join_management/display_data.html', {'data': data})

