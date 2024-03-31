from rest_framework.response import Response


def ResponseModel( data=None,msg="Successful", statusCode=None,status=True,):
   
    return Response(
        data={
            'status':status,
            'msg':msg,
            'response':data,
        },
        status=statusCode,

    )
