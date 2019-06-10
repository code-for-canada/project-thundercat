from rest_framework.views import APIView
from rest_framework import permissions
from views.retrieve_test_view import TEST_INSTRUCTIONS, retrieve_test_data


class PreTestSet(APIView):
    # Can only be accessed by Admin
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        return retrieve_test_data(request, TEST_INSTRUCTIONS)

# http://localhost/api/pre-test/?test_name=emibSampleTest
