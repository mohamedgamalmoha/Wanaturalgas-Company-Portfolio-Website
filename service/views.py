from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Heating, Cooling, Post
from django.contrib.contenttypes.models import ContentType


def HeatingView(request):
    heating = Heating.objects.first()
    if not heating:
        return HttpResponse('No heating posts')
    obj_id = heating.id
    content_type = ContentType.objects.get_for_model(Heating)
    posts = Post.objects.filter(content_type=content_type, object_id=obj_id)
    context = {
        'heating': heating,
        'posts': posts,
    }
    return render(request, 'service/heating.html', context)


def CoolingView(request):
    cooling = Cooling.objects.first()
    if not cooling:
        return HttpResponse('No Cooling posts')
    obj_id = cooling.id
    content_type = ContentType.objects.get_for_model(Heating)
    posts = Post.objects.filter(content_type=content_type, object_id=obj_id)
    context = {
        'Cooling': cooling,
        'posts': posts,
    }
    return render(request, 'service/heating.html', context)


def PostHeatingView(request, heating_id, post_id):
    heating = get_object_or_404(Heating, id=heating_id)
    obj_id = heating.id
    content_type = ContentType.objects.get_for_model(Heating)
    post = get_object_or_404(Post, content_type=content_type, object_id=obj_id, id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'service/post_heating.html', context)


def PostCoolingView(request, heating_id, post_id):
    cooling = get_object_or_404(Cooling, id=heating_id)
    obj_id = cooling.id
    content_type = ContentType.objects.get_for_model(Heating)
    post = get_object_or_404(Post, content_type=content_type, object_id=obj_id, id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'service/post_cooling.html', context)
