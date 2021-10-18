from datetime import datetime, date

from django.core.exceptions import ObjectDoesNotExist

from config.settings import STATIC_URL
from core.company.models import Company
from core.erp.models import Document
from core.noconform.models import NoConform, ActionPlan
from core.pqr.models import Complain


def extras(request):
    context = {}
    context['count_total'] = 0
    if request.user.is_authenticated:
        context['count_pqr'] = Complain.objects.filter(status_pqr='Abierto', response_pqr=request.user, date_complain_expire__lte=date.today()).count()
        context['count_nc'] = NoConform.objects.filter(treatment='Abierto', response_nc=request.user).count()
        context['count_ap'] = ActionPlan.objects.filter(state_plan='Abierto', task_response=request.user).count()
        context['company_logo'] = logo()
        context['count_testdoc'] = Document.objects.filter(status='En Prueba').count()
        context['count_vencido'] = Document.objects.filter(status='Vencido').filter(owner=request.user).count()
        context['count_aprobados'] = Document.objects.filter(status='Aprobado').count()
        context['count_elaboracion'] = Document.objects.filter(status='En Elaboración').filter(
            creator=request.user).count()
        context['count_revisar'] = Document.objects.filter(status='En Revisión').filter(reviewer=request.user).count()
        context['count_por_vencer'] = Document.objects.filter(status='Vigente').filter(
            date_alert_exp__lte=datetime.now()).filter(owner=request.user).count()
        context['count_aprobar'] = Document.objects.filter(status='En Aprobación').filter(owner=request.user).count()
        context['count_ruta'] = Document.objects.filter(status='En Revisión').filter(reviewer=None).count()
        context['count_total'] = context['count_elaboracion']+context['count_vencido']+context['count_aprobar']+context['count_revisar']+context['count_por_vencer']+context['count_testdoc']+context['count_nc']+context['count_ap']+context['count_pqr']
    return context

def logo():
    try:
        return Company.objects.get(id=1).get_logo()
    except ObjectDoesNotExist:
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
