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

    medicamento = Medicamento.objects.all().order_by('via')
    selected_remedies = request.GET.get('selected_remedies')
    if selected_remedies:
        medicamentos_selecionados = Medicamento.objects.filter(pk__in=selected_remedies.split(','))
    else:
        medicamentos_selecionados = []
    

    return render(request, 'home.html' , {'form': form, 'medicamentos': medicamento, 'medicamentos_selecionados': medicamentos_selecionados})
