from rest_framework.views import exception_handler
from rest_framework import status

from daan_i_backend.utils.response_model import responseModel


def custom_exception_handler(exc, context):
    # Call the default handler first to get the standard error response.
    response = exception_handler(exc, context)

    # Now add your custom logic or replace the default response entirely
    if response is not None and "token_not_valid" in str(exc):

        return responseModel(
            msg="Your session has expired. Please login again.",
            status=False,
            statusCode=status.HTTP_401_UNAUTHORIZED,
        )
    if (
        response is not None
        and "authentication_failed" in str(exc)
        and "404" in str(exc)
    ):

        return responseModel(
            msg="Data NOt Found", status=False, statusCode=status.HTTP_404_NOT_FOUND
        )
    elif (
        response is not None
        and "authentication_failed" in str(exc)
        and "400" in str(exc)
    ):

        return responseModel(
            msg="Token Is Required",
            status=False,
            statusCode=status.HTTP_400_BAD_REQUEST,
        )
    elif response is not None and response.status_code == status.HTTP_401_UNAUTHORIZED:
        return responseModel(
            msg="Authentication failed. Please provide a valid token.",
            status=False,
            statusCode=status.HTTP_401_UNAUTHORIZED,
        )

    return response
