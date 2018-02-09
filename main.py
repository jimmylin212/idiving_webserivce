import endpoints
from protorpc import remote

from models.messages import Response, MemberRequest
from utility.member_utility import MemberUtility

MEMBER_RESOURCE = endpoints.ResourceContainer(MemberRequest)

@endpoints.api(name='internal', version='v1')
class InternalApi(remote.Service):
    def __init__(self):
        self.member_utility = MemberUtility()

    @endpoints.method(MEMBER_RESOURCE, Response, path='member', http_method='POST', name='get_member')
    def get_member(self, request):
        response = self.member_utility.get_member(request)
        return Response(status=response['status'], message=response['message'], data=response['data'])

    @endpoints.method(MEMBER_RESOURCE, Response, path='member', http_method='PUT', name='create_member')
    def create_member(self, request):
        response = self.member_utility.create_member(request)
        return Response(status=response['status'], message=response['message'])

    @endpoints.method(MEMBER_RESOURCE, Response, path='member', http_method='PATCH', name='update_member')
    def update_member(self, request):
        response = self.member_utility.patch_member(request)
        return Response(status=response['status'], message=response['message'])

api = endpoints.api_server([InternalApi])
