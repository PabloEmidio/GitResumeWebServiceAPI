import base64
from json import loads, dumps

from fastapi import APIRouter, Response
from nameko.standalone.rpc import ServiceRpcProxy
from werkzeug.exceptions import BadRequest, NotFound


from git_resume.config import config
from git_resume.models.redis import GitHubDocumentCache


v1 = APIRouter(prefix=config.API_ROUTER_V1)
github_document = GitHubDocumentCache()


@v1.get('/gihub/pdf/{username}/')
def github_resume(username: str):
    with ServiceRpcProxy(
        config.GITHUB_RESUME_SERVICE, config.amqp_config
    ) as grpc:
        content = grpc.generate_pdf({'profile_name': username})
    filename = content.get('filename', username + '.pdf')
    github_document.set(content.get('filename', username), dumps(content))

    return {'success': True, 'filename': filename}


@v1.get('/github/files/{filename:path}')
def github_document_download(filename: str):
    if '/' in filename:
        raise BadRequest('Invalid filename')

    response_content = github_document.get(filename.upper())
    if not response_content:
        raise NotFound('File not found')

    response_content = loads(response_content)['file']

    headers = dict()
    headers['Content-Disposition'] = f'inline; filename="{filename}'

    return Response(
        base64.b64decode(response_content),
        headers=headers,
        media_type='application/pdf'
    )
