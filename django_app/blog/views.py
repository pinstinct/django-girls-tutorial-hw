from django.shortcuts import render


def post_list(request):
    # request를 넘겨받아 render 메서드 호출
    # render 메서드는 넘겨진 요청(request)과 blog/post_list.html 템플릿 받아
    # 리턴된 내용을 브라우저에 보여줌
    return render(request, 'blog/post_list.html', {})
