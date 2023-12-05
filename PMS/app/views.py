from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication






class UserList(APIView):
    """
    List all user, or create a new user.
    """
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DepartmentList(APIView):
    """
    List all Department, or create a new Department.
    """
    def get(self, request, format=None):
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DepartmentDetail(APIView):
    """
    Retrieve, update or delete a Department instance.
    """
    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        department = self.get_object(pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ProfileList(APIView):
    """
    List all Profile, or create a new Profile.
    """
    def get(self, request, format=None):
        department = Profile.objects.all()
        serializer = ProfileSerializer(department, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ProfileDetail(APIView):
    """
    Retrieve, update or delete a Profile instance.
    """
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = ProfileSerializer(department)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = ProfileSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        department = self.get_object(pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ProjectList(APIView):
    """
    List all Project, or create a new Project.
    """
    def get(self, request, format=None):
        project = Project.objects.all()
        
        serializer = ProjectSerializer(project, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ProjectDetail(APIView):
    """
    Retrieve, update or delete a Project instance.
    """
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






from django.db.models import Count, F


class CountProject(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        month = self.request.query_params.get('month')

        if not month:
            # Handle the case where month is not provided in the query parameters
            return Project.objects.none()

        # Filter projects started in the specified month and annotate with count
        queryset = Project.objects.filter(project_start_date__month=month)

        return queryset


class AttachmentList(APIView):
    """
    List all Attachment, or create a new Attachment.
    """
    def get(self, request, format=None):
        attachment = Attachment.objects.all()
        serializer = AttachmentSerializer(attachment, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# from rest_framework.permissions import IsAuthenticated

class AttachmentDetail(APIView):
    # authentication_class = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    """
    Retrieve, update or delete a Attachment instance.
    """
    def get_object(self, pk):
        try:
            return Attachment.objects.get(pk=pk)
        except Attachment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        attachment = self.get_object(pk)
        serializer = AttachmentSerializer(attachment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        attachment = self.get_object(pk)
        serializer = AttachmentSerializer(attachment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        attachment = self.get_object(pk)
        attachment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



from django_filters.rest_framework import DjangoFilterBackend

class AttachmentListView(generics.ListAPIView):

    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['attachment_date', 'project__department']


# from django.db.models import Count


# class Count(generics.ListAPIView):

#     def get(self, request, format=None):
#         project_count = Project.objects.filter('project_start_date').annotate(num_products=Count('project_name'))
#         serializer = AttachmentSerializer(project_count)
#         return Response(serializer.data)


# class ProjectFilterByDepartment()