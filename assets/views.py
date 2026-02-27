import csv
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView
from django.db.models import Sum
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Department, Asset, MaintenanceLog

class DashboardView(ListView):
    model = Asset
    template_name = 'assets/dashboard.html'
    context_object_name = 'assets'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department_costs'] = Department.objects.annotate(
            total_cost=Sum('user__asset__cost')
        )
        return context
    
class AssetListView(ListView):
    model = Asset
    template_name = 'assets/asset_list.html'
    context_object_name = 'assets'
    paginate_by = 5  

    def get_queryset(self):
        return Asset.objects.annotate(
            repair_total=Sum('maintenance_logs__cost')
        ).order_by('id')

class MaintenanceCreateView(CreateView):
    model = MaintenanceLog
    template_name = 'assets/maintenance_form.html'
    fields = ['description', 'cost', 'service_date']
    success_url = reverse_lazy('asset_list')

    def form_valid(self, form):
        asset_id = self.kwargs.get('pk')
        form.instance.asset = get_object_or_404(Asset, pk=asset_id)
        return super().form_valid(form)

def export_assets_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="asset_report.csv"'

    writer = csv.writer(response)
    
    writer.writerow(['Asset Name', 'Type', 'Cost', 'Assigned User'])

    assets = Asset.objects.all().select_related('assigned_to')
    for asset in assets:
        user_name = asset.assigned_to.username if asset.assigned_to else "Unassigned"
        
        writer.writerow([asset.name, asset.asset_type, asset.cost, user_name])

    return response