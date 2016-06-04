from django.http import HttpResponse
from django.template import loader
from django.dispatch import receiver
from django.db.models.signals import post_save
from models import Invites


def main(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


@receiver(post_save, sender=Invites)
def callback(**kwargs):
    # return HttpResponse('a')
    print('callback')
