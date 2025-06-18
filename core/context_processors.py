from django.core.exceptions import ObjectDoesNotExist

from config.settings import STATIC_URL
from core.company.models import Company


def extras(request):
    context = {}
    # context['count_total'] = 0
    if request.user.is_authenticated:
        context['company_detail'] = company()
        context['company_logo'] = logo()
    return context

def logo():
    try:
        company_ = Company.objects.first()
        if company_:
            return company_.get_logo()
    except ObjectDoesNotExist:
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

def company():
    try:
        company_detail = Company.objects.first()
        return company_detail
    except ObjectDoesNotExist:
        return False
