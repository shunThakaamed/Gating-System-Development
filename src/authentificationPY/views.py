# your-repo/src/authentication/views.py

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer
from web3 import Web3

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyNFTView(APIView):
    def post(self, request):
        wallet_address = request.data.get('wallet_address')
        contract_address = request.data.get('contract_address')
        token_id = request.data.get('token_id')

        # Initialize Web3 and contract
        w3 = Web3(Web3.HTTPProvider('<Your_Infura_or_Alchemy_HTTP_URL>'))
        contract = w3.eth.contract(address=contract_address, abi='<Your_Contract_ABI>')

        # Verify ownership of the NFT
        owner = contract.functions.ownerOf(token_id).call()
        if owner.lower() == wallet_address.lower():
            return Response({"message": "NFT ownership verified"}, status=status.HTTP_200_OK)
        return Response({"message": "NFT ownership not verified"}, status=status.HTTP_400_BAD_REQUEST)
