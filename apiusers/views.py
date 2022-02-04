from django.contrib.auth.hashers import make_password
from apiusers.serializers import UserSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from apiusers.models import Users
from django.http import Http404
from rest_framework import status


class UserApiView(APIView):

    def get(self, request):
        return Response({'users': list(Users.objects.all().values())})


class UsersList(APIView):

    def get(self, request):
        return Response({'users': list(Users.objects.all().values())})


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = UserSerializers(snippet)
        return Response(serializer.data)

    def post(self, request):
        kw = {
            'username': request.data.get('username'),
            'email': request.data.get('email'),
            'password': make_password(request.data.get('password'))
        }
        serializer = UserSerializers(data=kw)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        r = self.get_object(pk)
        serializer = UserSerializers(r, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        r = self.get_object(pk)
        r.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        r = self.get_object(pk)
        serializer = UserSerializers(r, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(code=201, data=serializer.data)
        return Response(code=400, data="wrong parameters")
