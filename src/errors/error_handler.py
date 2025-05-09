from .errors_types.http_bad_request import HttpBadRequest
from .errors_types.http_not_found import HttpNotFound
from .errors_types.http_unprocessable_entity import HttpUnprocessableEntity
from src.views.http_types.http_response import HttpResponse

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance (error, (HttpBadRequest, HttpNotFound, HttpUnprocessableEntity)):
        return HttpResponse (
            status_code= error.status_code,
            body= {
                "errors":[{
                    "title" : error.name,
                    "detail" : error.message
                }]
            }
        )
    
    return HttpResponse (
        status_code= 500,
            body= {
                "errors":[{
                    "title" : "Server Error",
                    "detail" : str(error)
                }]
            }
    )
