import logging, json, datetime
from db_utility import DBUtility
#import google.cloud.logging
#from google.cloud.logging.handlers import CloudLoggingHandler

SUCCESS_STATUS = 'success'
FAILED_STATUS = 'error'
SUCCESS_GET_MEMBER_MSG = 'SUCCESS_GET_MEMBER_MSG'
SUCCESS_CREATE_MEMBER_MSG = 'SUCCESS_CREATE_MEMBER_MSG'
SUCCESS_PATCH_MEMBER_MSG = 'SUCCESS_PATCH_MEMBER_MSG'
FAILED_DUPLICATE_MEMBER_MSG = 'FAILED_DUPLICATE_MEMBER_MSG'
FAILED_COLUMN_MISSING_MSG = 'FAILED_COLUMN_MISSING_MSG'
FAILED_MEMBER_NOT_FOUND_MSG = 'FAILED_MEMBER_NOT_FOUND_MSG'

class MemberUtility:
    def __init__(self):
        ## Initialize logger
        #client = google.cloud.logging.Client()
        #handler = CloudLoggingHandler(client, name="member")
        handler = logging.StreamHandler()
        self.logger = logging.getLogger('cloudLogger')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)
    
    def pre_process(self, request):
        db_utility = DBUtility()
        member_info = {}
        member_eq = {}
        member_licenses = []

        for each_property in db_utility.member_info_properties:
            if (request.get_assigned_value(each_property) and each_property == 'birthday'):
                member_info[each_property] = datetime.datetime.strptime(request.get_assigned_value(each_property), '%Y/%m/%d')
            elif (request.get_assigned_value(each_property) and (each_property == 'height' or each_property == 'weight')):
                member_info[each_property] = float(request.get_assigned_value(each_property))
            else:
                member_info[each_property] = request.get_assigned_value(each_property)
        
        for each_property in db_utility.member_eq_properties:
            if (each_property == 'id_number'):
                member_eq[each_property] = request.id_number
            elif (request.get_assigned_value(each_property) and each_property == 'counterweight'):
                member_eq[each_property] = float(request.get_assigned_value(each_property))
            else:
                if (request.get_assigned_value(each_property)):
                    member_eq[each_property] = True
                else:
                    member_eq[each_property] = False

        for license_type in db_utility.member_lincense_types:
            member_license = {}
            for each_property in db_utility.member_license_properties:
                if (each_property == 'license_type'):
                    member_license['license_type'] = license_type
                elif (each_property == 'id_number'):
                    member_license['id_number'] = request.id_number
                elif (each_property == 'tank_card'):
                    if (license_type == 'owd'):
                        if (request.get_assigned_value('%s_%s' % (license_type, each_property))):
                            member_license['tank_card'] = int(request.get_assigned_value('%s_%s' % (license_type, each_property)))
                else:
                    if (request.get_assigned_value('%s_%s' % (license_type, each_property))):
                        member_license[each_property] = datetime.datetime.strptime(
                            request.get_assigned_value('%s_%s' % (license_type, each_property)), '%Y/%m/%d')
                    else:
                        member_license[each_property] = None
                
            member_licenses.append(member_license)

        return member_info, member_eq, member_licenses

    def get_member(self, request):
        query_result = {}
        final_result = {}
        db_utility = DBUtility()
      
        if (request.id_number):
            self.logger.info('Get member %s' % request.id_number)
            member_info_result = db_utility.get_member_info(id_number = request.id_number)
            query_result.update(member_info_result.to_dict())
        elif (request.ch_name):
            self.logger.info('Get member %s' % request.ch_name)
            member_info_result = db_utility.get_member_info(ch_name = request.ch_name)
            query_result.update(member_info_result.to_dict())
        else:
            return {'status': FAILED_STATUS, 'message': FAILED_COLUMN_MISSING_MSG}
        
        if member_info_result:
            request_id_number = query_result['id_number']

            member_eq_result = db_utility.get_member_eq(id_number = request_id_number)
            query_result.update(member_eq_result.to_dict())

            member_license_results = db_utility.get_member_license(id_number = request_id_number)
            for member_license_result in member_license_results:
                license_type = member_license_result.license_type
                query_result['%s_apply' % license_type] = member_license_result.apply
                query_result['%s_deposit' % license_type] = member_license_result.deposit
                query_result['%s_license' % license_type] = member_license_result.license
                query_result['%s_material' % license_type] = member_license_result.material
                query_result['%s_payment' % license_type] = member_license_result.payment
                query_result['%s_status' % license_type] = member_license_result.status
                if license_type == 'owd':
                    query_result['%s_tank_card' % license_type] = member_license_result.tank_card
        
        for key in query_result:
            if (isinstance(query_result[key], datetime.date)):
                final_result[key] = query_result[key].strftime('%Y/%m/%d')
            else:
                final_result[key] = query_result[key]


        return {'status': SUCCESS_STATUS, 'message': SUCCESS_GET_MEMBER_MSG, 'data': json.dumps(final_result, ensure_ascii=True)}

    def create_member(self, request):
        db_utility = DBUtility()
        # member_data, member_eq_data, license_data = self.request2Dict(request)
        self.logger.info('Create member %s' % request.id_number)

        if (request.id_number == None):
            return {'status': FAILED_STATUS, 'message': FAILED_COLUMN_MISSING_MSG}

        target_member_info = db_utility.get_member_info(id_number = request.id_number)

        if (target_member_info == None):
            ## get the key value of each member data
            member_info, member_eq, member_licenses = self.pre_process(request)

            db_utility.upsert_member_info(member_info)
            db_utility.upsert_member_eq(member_eq)
            for member_license in member_licenses:
                db_utility.upsert_member_license(member_license)
        else:
            return {'status': FAILED_STATUS, 'message': FAILED_DUPLICATE_MEMBER_MSG}

        return {'status': SUCCESS_STATUS, 'message': SUCCESS_CREATE_MEMBER_MSG}

    def patch_member(self, request):
        db_utility = DBUtility()
        self.logger.info('Patch member %s' % request.id_number)

        if (request.id_number == None):
            return {'status': FAILED_STATUS, 'message': FAILED_COLUMN_MISSING_MSG}

        target_member_info = db_utility.get_member_info(id_number = request.id_number)

        if (target_member_info):
            member_info, member_eq, member_licenses = self.pre_process(request)
            db_utility.upsert_member_info(member_info)
            db_utility.upsert_member_eq(member_eq)
            for member_license in member_licenses:
                db_utility.upsert_member_license(member_license)

        else:
            return {'status': FAILED_STATUS, 'message': FAILED_MEMBER_NOT_FOUND_MSG}

        return {'status': SUCCESS_STATUS, 'message': SUCCESS_PATCH_MEMBER_MSG}
        