from rest_framework.response import Response
from django.utils.translation import gettext


def responseModel(data=None, msg=gettext("Successful"), statusCode=None, status=True,):

    return Response(
        data={
            'status': status,
            'msg': msg,
            'response': data,
        },
        status=statusCode,

    )


def errorMsg(errors: dict | list) -> str:
    if isinstance(errors, dict):

        for _, error_list in errors.items():
            return error_list[0] if isinstance(error_list, list) else error_list
    elif isinstance(errors, list):
        for error_list in errors:
            return error_list
    return errors
