import endpoints
from protorpc import remote

from models.messages import Response, MemberRequest, CourseRequest, EventRequest
from utility.member_utility import MemberUtility
from utility.course_utility import CourseUtility
from utility.event_utility import EventUtility

MEMBER_RESOURCE = endpoints.ResourceContainer(MemberRequest)
COURSE_RESOURCE = endpoints.ResourceContainer(CourseRequest)
EVENT_RESOURCE = endpoints.ResourceContainer(EventRequest)

@endpoints.api(name='internal', version='v1')
class InternalApi(remote.Service):
    def __init__(self):
        self.member_utility = MemberUtility()
        self.course_utility = CourseUtility()
        self.event_utility = EventUtility() 

    ## method for member
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

    ## method for course
    @endpoints.method(COURSE_RESOURCE, Response, path='course', http_method='POST', name='get_course')
    def get_course(self, request):
        response = self.course_utility.get_course(request)
        return Response(status=response['status'], message=response['message'], data=response['data'])

    @endpoints.method(COURSE_RESOURCE, Response, path='course', http_method='PUT', name='create_course')
    def create_course(self, request):
        response = self.course_utility.create_course(request)
        return Response(status=response['status'], message=response['message'])

    @endpoints.method(COURSE_RESOURCE, Response, path='course', http_method='PATCH', name='update_course')
    def update_course(self, request):
        response = self.course_utility.patch_course(request)
        return Response(status=response['status'], message=response['message'])

    # @endpoints.method(COURSE_RESOURCE, Response, path='courses', http_method='POST', name='get_courses')
    # def get_course(self, request):
    #     response = self.course_utility.get_courses(request)
    #     return Response(status=response['status'], message=response['message'], data=response['data'])

    ## method for event
    @endpoints.method(EVENT_RESOURCE, Response, path='event', http_method='POST', name='get_event')
    def get_event(self, request):
        response = self.event_utility.get_event(request)
        return Response(status=response['status'], message=response['message'], data=response['data'])

    @endpoints.method(EVENT_RESOURCE, Response, path='event', http_method='PUT', name='create_event')
    def create_event(self, request):
        response = self.event_utility.create_event(request)
        return Response(status=response['status'], message=response['message'])

    @endpoints.method(EVENT_RESOURCE, Response, path='event', http_method='PATCH', name='update_event')
    def update_event(self, request):
        response = self.event_utility.patch_event(request)
        return Response(status=response['status'], message=response['message'])

api = endpoints.api_server([InternalApi])
