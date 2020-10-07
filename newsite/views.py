from django.shortcuts import redirect


def redirect_home(request):
    return redirect('posts_list_url', permanent=True)
