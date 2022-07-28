from fastapi import Request
from fastapi.responses import JSONResponse
from werkzeug.exceptions import HTTPException as wHTTPException
from starlette.exceptions import HTTPException as sHTTPException


def handler_werkzeug_exceptions(request, exc: wHTTPException):
    return JSONResponse(
        status_code=exc.code,
        content={
            'status_code': exc.code,
            'message': str(exc)
        }
    )


def handler_not_mapped_error_exception(request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            'status_code': 500,
            'message': 'Server error'
        }
    )


def handler_starlette_exception(request: Request, exc: sHTTPException):
    message = 'Application error'
    if exc.status_code == 404:
        message = 'Router not found'
    return JSONResponse(
        status_code=exc.status_code,
        content={
            'status_code': exc.status_code,
            'message': str(exc) or message
        }
    )
