from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from polls.models import Question, Choice
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    # model=Question
    template_name='polls/index.html'
    context_object_name="latest_questions_list"
    def get_queryset(self):
        """
        사용 시나리오
        - 인기순으로 정렬
        - 우리 제품중 부가가치가 높은 제품
        - 지금 접속한 고객이 이전에 구매이력을 토대로 오늘 살거 같은 순서
        ......
        """
        return Question.objects.order_by("-pub_date")[:7]
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# 하나의 Question에 Choice를 CRUD 하는 View 만들기
# Question에 대한 Class를 참고해서 기초 코드를 작성하되
# 어떤 내용이 추가적으로 필요한지 고민해 보겠습니다
class CreateChoiceView(generic.CreateView):
    model=Choice
    fields=['choice_text']
    # fields=['question','choice_text']
    template_name='polls/choice_form.html'
    # success_url=reverse_lazy('polls:index')
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["question"] = Question.objects.get(pk=self.kwargs['pk'])
        context["lion"] = "tiger"
        # context = {"question":question}
        return context
    def post(self, request, *args: str, **kwargs: Any) -> HttpResponse:
        # pk를 통해서 question정보는 받아오기
        # 들어오는 데이터로 값을 생성        
        # Choice table 작성
        question = Question.objects.get(pk=self.kwargs['pk'])
        Choice.objects.create(question=question, choice_text=request.POST['choice_text'])
        return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))

        # success url을 우리가 choice를 추가했던 페이지(detail)로 이동
        # return super().post(request, *args, **kwargs)

class UpdataChoiceView:pass
class DeleteChoiceView(generic.DeleteView):
    model=Choice
    template_name = 'polls/choice_confirm_delete.html'  # 삭제 확인 페이지
    context_object_name = 'choice'  # 템플릿에서 사용할 객체 이름
    success_url = reverse_lazy('polls:index')  # 삭제 후 리디렉션할 URL

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class CreateQuestionView(generic.CreateView):
    model = Question
    fields=['question_text','pub_date']
    template_name='polls/question_form.html'
    success_url=reverse_lazy('polls:index')

class UpdateQuestionView(generic.UpdateView):
    model = Question
    fields=['question_text','pub_date']
    template_name='polls/question_form.html'
    success_url=reverse_lazy('polls:index')

class DeleteQuestionView(generic.DeleteView):
    model = Question    
    template_name='polls/delete_question.html'
    success_url=reverse_lazy('polls:index')

def vote(request, question_id):
    # error message 만들기
    # 선택된 choice 항목의 votes 값을 1 증가 시키기
    try:
        choice = Choice.objects.get(pk=request.POST['choice'])
        choice.votes+=1
        #choice.votes = F("votes")+1
        choice.save()
    except Choice.DoesNotExist:      
    # except Exception:      
        question = get_object_or_404(Question, pk=question_id)
        # choice_list = question.choice_set.all()
        context = {
        'question':question, 
        'error_message':"뭔가 잘못됐네요!!!"        
        }
        return render(request,'polls/detail.html', context )

    # 다른 페이지 보여주기
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    # return HttpResponseRedirect("https://www.naver.com")
    