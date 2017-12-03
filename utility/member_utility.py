import logging
from db_utility import DBUtility
#import google.cloud.logging
#from google.cloud.logging.handlers import CloudLoggingHandler

class MemberUtility:
    def __init__(self):
        ## Initialize logger
        #client = google.cloud.logging.Client()
        #handler = CloudLoggingHandler(client, name="member")
        handler = logging.StreamHandler()
        self.logger = logging.getLogger('cloudLogger')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)
    
    def get_member(self, request):
        final_result = {}
        db_utility = DBUtility()
      
        if (request.id_number):
            self.logger.info('Get member %s' % request.id_number)
            query_result = db_utility.get_member_info(id_number = request.id_number)
            final_result.update(query_result.to_dict())
        elif (request.ch_name):
            self.logger.info('Get member %s' % request.ch_name)
            query_result = db_utility.get_member_info(ch_name = request.ch_name)
            final_result.update(query_result.to_dict())
        else:
            return 'error'
        
        if query_result:
            request_id_number = final_result['id_number']

            query_result = db_utility.get_member_eq(id_number = request_id_number)
            final_result.update(query_result.to_dict())

            query_result = db_utility.get_member_license(id_number = request_id_number)
            final_result.update(query_result.to_dict())

        return final_result

    def create_member(self, request):
        db_utility = DBUtility()
        # member_data, member_eq_data, license_data = self.request2Dict(request)
        self.logger.info('Create member %s' % request.id_number)

        if (request.id_number == None):
            return 'error'

        ## create member info into database
        db_utility.upsert_member_info(request)

        ## create member equipment info into database
        db_utility.upsert_member_eq(request)

        ## create member license data into data, only OWD has tank card
        db_utility.upsert_member_license(request)

        return 'success'

    def patch_member(self, request):
        db_utility = DBUtility()

        if (request.id_number == None):
            return 'error'

        target_member_info = db_utility.get_member_info(id_number = request.id_number)

        if (target_member_info):
            db_utility.upsert_member_info(request)
            db_utility.upsert_member_eq(request)
            db_utility.upsert_member_license(request)

        else:
            return 'error'

        return
        