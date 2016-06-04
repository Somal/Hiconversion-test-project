from django.test import TestCase
from django.test.client import Client
from models import *


class Testing(TestCase):
    def test_allInviteRequestsIsSatisfied(self):
        invite_users = Invites.objects.exclude(email__in=User.objects.values_list('email'))
        self.assertEqual(invite_users.count(), 0)

    def test_allEmailsAreDifferent(self):
        flag = True
        try:
            for email in User.objects.values_list('email'):
                user = User.objects.get(email=email)
        except:
            flag = False

        self.assertEqual(flag, True)

    def test_allInvitessAreDifferent(self):
        flag = True
        try:
            for invite in User.objects.values_list('invite'):
                user = User.objects.get(invite=invite)
        except:
            flag = False

        self.assertEqual(flag, True)