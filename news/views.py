from django.conf import settings
from django.views.generic import ListView
from news.models import News


class Latest_news(ListView):
    model = News
    ordering = ['-pub_date']
    query_set = News.objects.filter(status=True)
    template_name = 'news/list.html' 
    context_object_name = 'news'
    paginate_by = 1

    # def quesry_set(self):
    #     queryset = super(Latest_news, self).get_queryset()
    #     return queryset.filter(status=True).order_by('-pub_date')
    
    #  def get_context_data(self, **kwargs):
    #         context = super(SoalListView, self).get_context_data(**kwargs) 
    #     list_exam = FileExam.objects.all()
    #     paginator = Paginator(list_exam, self.paginate_by)

    #     page = self.request.GET.get('page')

    #     try:
    #         file_exams = paginator.page(page)
    #     except PageNotAnInteger:
    #         file_exams = paginator.page(1)
    #     except EmptyPage:
    #         file_exams = paginator.page(paginator.num_pages)

    #     context['list_exams'] = file_exams
    #     return context
