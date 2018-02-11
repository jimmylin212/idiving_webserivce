import json
class CommonUtility:
    def __init__(self):
        self.message_mapping = {
            'SUCCESS': 'success',
            'FAILED': 'error',
            'SUCCESS_GET_MEMBER_MSG': 'SUCCESS_GET_MEMBER_MSG',
            'SUCCESS_CREATE_MEMBER_MSG': 'SUCCESS_CREATE_MEMBER_MSG',
            'SUCCESS_PATCH_MEMBER_MSG': 'SUCCESS_PATCH_MEMBER_MSG',
            'FAILED_DUPLICATE_MEMBER_MSG': 'FAILED_DUPLICATE_MEMBER_MSG',
            'FAILED_COLUMN_MISSING_MSG': 'FAILED_COLUMN_MISSING_MSG',
            'FAILED_MEMBER_NOT_FOUND_MSG': 'FAILED_MEMBER_NOT_FOUND_MSG',
            'SUCCESS_GET_COURSE_MSG': 'SUCCESS_GET_COURSE_MSG',
            'SUCCESS_CREATE_COURSE_MSG': 'SUCCESS_CREATE_COURSE_MSG',
            'SUCCESS_PATCH_COURSE_MSG': 'SUCCESS_PATCH_COURSE_MSG',
            'FAILED_DUPLICATE_COURSE_MSG': 'FAILED_DUPLICATE_COURSE_MSG',
            'FAILED_COURSE_NOT_FOUND_MSG': 'FAILED_COURSE_NOT_FOUND_MSG',
            'FAILED_COLUMN_INCORRECT': 'FAILED_COLUMN_INCORRECT'
        }

        return

    def responseHandler(self, status, message, data=None):
        response = {}
        response['status'] = self.message_mapping[status]
        response['message'] = self.message_mapping[message]
        if data != None:
            response['data'] = json.dumps(data, ensure_ascii=True)

        return response