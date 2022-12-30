from django.contrib.auth.models import User
from api.models import Friends

def people_list(request, *args, **kwargs):
    people = User.objects.exclude(username=request.user)
    return {'people':people}

# def user_followings(request, *args, **kwargs):
#     followings = Friends.objects.filter(follower=request.user)
#     return {'followings':followings}