import logging, json, datetime
from db_utility import DBUtility
from common_utility import CommonUtility

class CourseUtility:
    def __init__(self):
        ## Initialize logger
        #client = google.cloud.logging.Client()
        #handler = CloudLoggingHandler(client, name="member")
        handler = logging.StreamHandler()
        self.logger = logging.getLogger('cloudLogger')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)
    
    def prettify_request(self, request):
        updated_input = {}
        db_utility = DBUtility()
        
        for each_property in db_utility.course_properties:
            if (each_property == 'unique_code' and not request.get_assigned_value(each_property)):
                updated_input[each_property] = '%s-%s' % (request.type, request.dates.split(',')[0].replace('/', ''))
            elif (each_property == 'start_date'):
                if request.dates:
                    updated_input[each_property] = datetime.datetime.strptime(request.dates.split(',')[0], '%Y/%m/%d')
                else:
                    updated_input[each_property] = None
            elif ((each_property == 'members' or each_property == 'dates') and request.get_assigned_value(each_property)):
                updated_input[each_property] = json.dumps(request.get_assigned_value(each_property))
            elif (each_property == 'price' and not request.get_assigned_value(each_property)):
                updated_input[each_property] = 0
            else:
                updated_input[each_property] = request.get_assigned_value(each_property)

        return updated_input

    def get_course(self, request):
        query_result = {}
        final_result = {}
        db_utility = DBUtility()
        common_utility = CommonUtility()

        if not request.unique_code:
            return common_utility.responseHandler('FAILED', 'FAILED_COLUMN_MISSING_MSG')

        query_course_result = db_utility.get_course(request.unique_code)
        query_result.update(query_course_result.to_dict())

        self.logger.info(query_result)
        for key in query_result:
            if isinstance(query_result[key], datetime.date):
                final_result[key] = query_result[key].strftime('%Y/%m/%d')
            else:
                final_result[key] = query_result[key]

        self.logger.info(final_result)
        return common_utility.responseHandler('SUCCESS', 'SUCCESS_GET_COURSE_MSG', final_result)

    def get_courses(self):
        return

    def create_course(self, request):
        db_utility = DBUtility()
        common_utility = CommonUtility()

        if (request.type and request.type not in db_utility.member_lincense_types):
            return common_utility.responseHandler('FAILED', 'FAILED_COLUMN_INCORRECT')

        updated_input = self.prettify_request(request)

        target_course_info = db_utility.get_course(updated_input['unique_code'])
        if not target_course_info:
            db_utility.upsert_course(updated_input)
        else:
            return common_utility.responseHandler('FAILED', 'FAILED_DUPLICATE_COURSE_MSG')

        return common_utility.responseHandler('SUCCESS', 'SUCCESS_CREATE_COURSE_MSG')

    def patch_course(self, request):
        db_utility = DBUtility()
        common_utility = CommonUtility()

        if not request.unique_code:
            return common_utility.responseHandler('FAILED', 'FAILED_COLUMN_MISSING_MSG')

        target_course_info = db_utility.get_course(request.unique_code)
        if target_course_info:
            updated_input = self.prettify_request(request)
            db_utility.upsert_course(updated_input)
        else:
            return common_utility.responseHandler('FAILED', 'FAILED_COURSE_NOT_FOUND_MSG')

        return common_utility.responseHandler('SUCCESS', 'SUCCESS_PATCH_COURSE_MSG')