from fastapi import FastAPI
from werkzeug.exceptions import HTTPException as wHTTPException

from git_resume.config import config
from git_resume.api import v1
from git_resume.handler import (
    handler_werkzeug_exceptions,
    handler_not_mapped_error_exception,
    handler_starlette_exception
)


app = FastAPI(**config.api_config)

app.include_router(v1, prefix=config.API_BASE_PREFIX)
app.add_exception_handler(404, handler_starlette_exception)
app.add_exception_handler(wHTTPException, handler_werkzeug_exceptions)
app.add_exception_handler(Exception, handler_not_mapped_error_exception)
