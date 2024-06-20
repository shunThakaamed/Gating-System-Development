# your-repo/tests/unit/test_authentication.py

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class AuthenticationTests(APITestCase):
    def test_register_user(self):
        url = reverse('register')
        data = {
            "username": "testuser",
            "password": "testpassword",
            "wallet_address": "0x1234567890abcdef1234567890abcdef12345678"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_verify_nft(self):
        url = reverse('verify_nft')
        data = {
            "wallet_address": "0x1234567890abcdef1234567890abcdef12345678",
            "contract_address": "<Your_Contract_Address>",
            "token_id": 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
