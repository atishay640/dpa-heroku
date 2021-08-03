from .tasks import bulk_insert_from_csv
from django.http import HttpResponse
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from django.db.models import Count
from django.http import JsonResponse
from http import HTTPStatus
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
import logging
from .utils import get_jwt_payload
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Get an instance of a custom logger
logger = logging.getLogger('DPA')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "sales/dashboard.html"
    login_url = '/accounts/login/'

    def get(self, request, *args, **kwargs):
        if request.GET.get("download_url"):
            return render(request,'sales/download.html' , {"download_url" : request.GET.get("download_url")})
        return super().get(request, *args, **kwargs)


@cache_page(60 * 15)
@login_required(login_url='/accounts/login/')
def getDashboardChartView(request):
    """ Prepares chart data to display on dashboard to logged in users."""
    
    logger.debug("Preparing dashboard data for chart.")
    if request.is_ajax and request.method == "GET":
        sales_data =  Order.objects.values("dim_unit_unit_id").annotate(coupon_count=Count('dim_unit_unit_id'))
        data =  {
            "stores" : list(sales_data.values_list('dim_unit_unit_id', flat=True)),
            "redemptions" : list(sales_data.values_list('coupon_count', flat=True))
        }
        logger.debug(f"Store count : {len(data['stores'])}")
        return JsonResponse(data, status = HTTPStatus.OK)
    
    logger.error(f"Neither request if GET nor ajax.")
    return JsonResponse({}, status = HTTPStatus.BAD_REQUEST)


def mediaDownloadView(request, token):
    if request.user.is_anonymous:
        return HttpResponseRedirect(redirect_to=f"/sales/dashboard?download_url={request.path}")

    payload = get_jwt_payload(token)
    file = payload.get("file")
    return HttpResponseRedirect(redirect_to=f"/{file}")

