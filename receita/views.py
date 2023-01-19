from django.shortcuts import render
from .forms import MedicamentoForm
from .models import Medicamento, Via
from django.shortcuts import redirect
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MedicamentoForm()  

    medicamento = Medicamento.objects.all()
    medicamento = reversed(medicamento)

    return render(request, 'home.html' , {'form': form, 'medicamentos': medicamento})
