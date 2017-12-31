import logging, json
from db_utility import DBUtility
#import google.cloud.logging
#from google.cloud.logging.handlers import CloudLoggingHandler

RETURN_SUCCESS = 'success'
RETURN_ERROR = 'error'

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
            member_info_result = db_utility.get_member_info(id_number = request.id_number)
            final_result.update(member_info_result.to_dict())
        elif (request.ch_name):
            self.logger.info('Get member %s' % request.ch_name)
            member_info_result = db_utility.get_member_info(ch_name = request.ch_name)
            final_result.update(member_info_result.to_dict())
        else:
            return RETURN_ERROR
        
        if member_info_result:
            request_id_number = final_result['id_number']

            member_eq_result = db_utility.get_member_eq(id_number = request_id_number)
            final_result.update(member_eq_result.to_dict())

            member_license_results = db_utility.get_member_license(id_number = request_id_number)
            for member_license_result in member_license_results:
                license_type = member_license_result.license_type
                final_result['%s_apply' % license_type] = member_license_result.apply
                final_result['%s_deposit' % license_type] = member_license_result.deposit
                final_result['%s_license' % license_type] = member_license_result.license
                final_result['%s_material' % license_type] = member_license_result.material
                final_result['%s_payment' % license_type] = member_license_result.payment
                final_result['%s_status' % license_type] = member_license_result.status
                if license_type == 'owd':
                    final_result['%s_tank_card' % license_type] = member_license_result.tank_card

        return RETURN_SUCCESS, json.dumps(final_result, ensure_ascii=True)

    def create_member(self, request):
        db_utility = DBUtility()
        # member_data, member_eq_data, license_data = self.request2Dict(request)
        self.logger.info('Create member %s' % request.id_number)

        if (request.id_number == None):
            return RETURN_ERROR

        ## create member info into database
        db_utility.upsert_member_info(request)

        ## create member equipment info into database
        db_utility.upsert_member_eq(request)

        ## create member license data into data, only OWD has tank card
        db_utility.upsert_member_license(request)

        return RETURN_SUCCESS

    def patch_member(self, request):
        db_utility = DBUtility()
        self.logger.info('Patch member %s' % request.id_number)

        if (request.id_number == None):
            return RETURN_ERROR

        target_member_info = db_utility.get_member_info(id_number = request.id_number)

        if (target_member_info):
            db_utility.upsert_member_info(request)
            db_utility.upsert_member_eq(request)
            db_utility.upsert_member_license(request)

        else:
            return RETURN_ERROR

        return RETURN_SUCCESS
        