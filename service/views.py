from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, render

from .models import Cooling, Heating, Post


def heating_view(request):
    heating = Heating.objects.first()
    if heating:  # will remove this if later as we prevented delete permission
        obj_id = heating.id
        content_type = ContentType.objects.get_for_model(Heating)
        posts = Post.objects.filter(content_type=content_type,
                                    object_id=obj_id)
    else:
        posts = None

    context = {
        'heating': heating,
        'posts': posts,
        'active': 'heating'
    }
    return render(request, 'service/heating.html', context)


def cooling_view(request):
    cooling = Cooling.objects.first()
    if cooling:  # will remove this if later as we prevented delete permission
        obj_id = cooling.id
        content_type = ContentType.objects.get_for_model(Cooling)
        posts = Post.objects.filter(content_type=content_type,
                                    object_id=obj_id)
    else:
        posts = None

    context = {
        'cooling': cooling,
        'posts': posts,
        'active': 'cooling'
    }
    return render(request, 'service/cooling.html', context)


def post_heating_view(request, heating_id, post_id):
    heating = get_object_or_404(Heating, id=heating_id)
    obj_id = heating.id
    content_type = ContentType.objects.get_for_model(Heating)
    post = get_object_or_404(Post, content_type=content_type,
                             object_id=obj_id, id=post_id)
    context = {
        'post': post,
        'active': 'heating'
    }
    return render(request, 'service/post_heating.html', context)


def post_cooling_view(request, cooling_id, post_id):
    cooling = get_object_or_404(Cooling, id=cooling_id)
    obj_id = cooling.id
    content_type = ContentType.objects.get_for_model(Cooling)
    post = get_object_or_404(Post, content_type=content_type,
                             object_id=obj_id, id=post_id)
    context = {
        'post': post,
        'active': 'cooling'
    }
    return render(request, 'service/post_cooling.html', context)
