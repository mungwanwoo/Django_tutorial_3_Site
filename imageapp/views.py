from django.shortcuts import render, redirect, get_object_or_404
from .models import ImagePost
from django.contrib.auth.decorators import login_required
from .forms import ImagePostForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# Create your views here.

# 전체 이미지 갤러리 보여주기
def index(request):
    images = ImagePost.objects.all()
    context = {"images":images}
    return render(request, 'imageapp/index.html', context)

# detail
def  image_detail(request, image_id):
    image = get_object_or_404(ImagePost, pk=image_id)
    context = {'image':image,'liked':image.is_liked(request.user)}
    return render(request, 'imageapp/image_detail.html', context)
# 새 게시글
@login_required
def image_write(request):
    if request.method =="POST":
        # 전송된 데이터를 저장
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            image_post = form.save(commit=False)
            image_post.author=request.user
            image_post.save()
            return redirect('imageapp:index')
    else:
        # 폼 생성
        form = ImagePostForm()
        return render(request, 'imageapp/image_form.html', {"form":form})

# 수정
@login_required
def image_edit(request, image_id):
    image_post = get_object_or_404(ImagePost, pk=image_id)
    if request.method =="POST":
        # 전송된 데이터를 저장
        form = ImagePostForm(request.POST, request.FILES, instance=image_post)
        if form.is_valid():
            image_post = form.save(commit=False)
            image_post.author=request.user
            image_post.save()
            return redirect('imageapp:index')
    else:
        # 폼 생성        
        form = ImagePostForm(instance=image_post)
        return render(request, 'imageapp/image_form.html', {"form":form})
# 삭제
@login_required
def image_delete(request, image_id):
    image_post = get_object_or_404(ImagePost, pk=image_id)
    image_post.delete()
    return redirect('imageapp:index')


@login_required  # 로그인한 사용자만 접근 가능
@require_POST    # POST 요청만 허용
def toggle_like(request, image_id):
    post = ImagePost.objects.get(pk=image_id)
    user=request.user

    if post.is_liked(user):
        post.unlike(user)
        status= "unliked"
    else:
        post.like(user)
        status="liked"
    
    context={
        'status':status,
        'liker_count':post.get_liker_count()

    }
    return JsonResponse(context)






































    # try:
    #     # 게시물을 가져옵니다
    #     post = ImagePost.objects.get(id=post_id)
    #     user = request.user

    #     # 현재 구독 상태에 따라 다른 동작을 수행합니다
    #     if post.is_liked(user):
    #         post.unlike(user)
    #         message = "좋아요가 취소되었습니다"
    #         status = "unliked"
    #     else:
    #         post.like(user)
    #         message = "좋아요가 완료되었습니다"
    #         status = "liked"

    #     # 성공 응답을 반환합니다
    #     return JsonResponse({
    #         'status': 'success',
    #         'subscription_status': status,
    #         'message': message,
    #         'subscriber_count': post.get_liker_count()
    #     })

    # except ImagePost.DoesNotExist:
    #     # 게시물이 존재하지 않는 경우의 에러 처리
    #     return JsonResponse({
    #         'status': 'error',
    #         'message': '게시글을 찾을 수 없습니다'
    #     }, status=404)
    # except Exception as e:
    #     # 기타 예외 상황 처리
    #     return JsonResponse({
    #         'status': 'error',
    #         'message': str(e)
    #     }, status=400)





