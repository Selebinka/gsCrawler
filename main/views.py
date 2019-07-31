from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib import auth
from django.http import JsonResponse

from .models import GoogleResultModel
from .filters import ResultFilter
from .forms import RunCrawlForm

from scrapyd_api import ScrapydAPI


scrapyd = ScrapydAPI('http://localhost:6800')

def search_result(request):
    result = GoogleResultModel.objects.all()
    result_filter = ResultFilter(request.GET, queryset=result)
    return render(request, 'result_list.html', {'result_filter': result_filter, 'username': auth.get_user(request).username})

def manager_spider(request):
    form = RunCrawlForm()
    return render(request, 'manager_spider.html', {'form': form, 'username': auth.get_user(request).username})

@csrf_exempt
@require_http_methods(['POST', 'GET'])
def crawl_run(request):
    if request.method == 'POST':
        form = RunCrawlForm(request.POST)

        if form.is_valid():
            keywords = form.cleaned_data['keywords']
            value = abs(form.cleaned_data['value'])
            if not value:
                value = 10

            task = scrapyd.schedule('default', 'googlesearch', keywords=keywords, value=value)
            status = scrapyd.job_status('default', task)
            while status != 'finished':
                status = scrapyd.job_status('default', task)

            search_result = GoogleResultModel.objects.all().order_by('-id')[:value]
            
            return render(request, 'result_crawl.html', {'search_result': search_result, 'username': auth.get_user(request).username})

