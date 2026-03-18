from django.shortcuts import render, redirect
from theme.models import Post


def home(request):
    posts = Post.objects.all().order_by("-created")
    return render(request, "base.html", {"posts": posts})

def cms(request):

    if request.method == "POST":
        title = request.POST.get("title")
        writer = request.POST.get("writer")
        content = request.POST.get("content")
        image_url = request.POST.get("image_url")

        Post.objects.create(
            title=title,
            writer=writer,
            content=content,
            image_url=image_url
        )

        return redirect("home")

    return render(request, "school/cms.html")