"""
1. 파이썬 셸에서 Post를 추가하고 저장해보기
2. id가 2인 Post객체를 발행해보기
3. 템플릿의 post_list키에 빈 리스트가 전달 될 경우 포스트 없음을 출력

Detail view를 만들어봅니다
    1. view에 post_detail함수 추가
        post_detail은 인자로 post_id를 받는다

    2. urls.py에 해당 view와 연결하는 url을 추가
        정규표현식으로 패턴네임 post_id이름을 갖는 숫자1개이상의 패턴을 등록

    3. post_detail뷰가 원하는 URL에서 잘 출력되는지 확인 후 (stub메서드 사용)
        get 쿼리셋을 사용해서 (Post.objects.get(...))
        id값이 인자로 전달된 post_id와 같은 Post객체를 context에 담아
        post-detail.html을 render한 결과를 리턴

    4. 템플릿에 post-detail.html을 만들고,
        인자로 전달된 Post객체의
        title, content, created_date, published_date를 출력
"""
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post


def post_list(request):
    context = {
        # 'post_list': Post.objects.filter(
        #     published_date__lte=timezone.now()
        # ),
        'post_list': Post.objects.all(),
    }
    return render(request, 'blog/post-list.html', context)


def post_detail(request, post_id):
    # try:
    #     # ORM을 이용해서 id가 전달받은 post_id와 일치하는 Post객체를 post변수에 할당
    #     post = Post.objects.get(id=post_id)
    # except Post.DoesNotExist as e:
    #     # DoesNotExist예외 발생시 해당 예외를 리턴
    #     return HttpResponse(e)
    post = get_object_or_404(Post, id=post_id)
    # 전달할 context 딕셔너리의 키 'post'에 post변수를 전달
    context = {
        'post': post,
    }
    # blog/post-detail.html 템플릿을 render한 결과를 리턴
    return render(request, 'blog/post-detail.html', context)


def post_add(request):
    if request.method == 'POST':
        # 요청의 method가 POST일 경우
        # 요청받은 데이터를 출력
        data = request.POST
        title = data['input_title']
        content = data['input_content']
        author = User.objects.get(id=1)

        # 받은 데이터를 사용해서 Post객체를 생성
        p = Post(title=title, content=content, author=author)
        p.save()

        # redirect메서드는 인자로 주어진
        #   URL또는
        #   urlpattern의 name을 이용해 만들어낸 URL을 사용해서
        #   브라우저가 해당 URL로 이동하도록 해줌
        return redirect('post_list')
    else:
        # 요청의 method가 POST가 아닐 경우,
        # 글 쓰기 양식이 있는 템플릿을 렌더해서 리턴
        return render(request, 'blog/post-add.html')
