FROM python:3.9

RUN mkdir -p /opt/api

COPY . /opt/api
WORKDIR /opt/api

RUN apt-get update
RUN pip3 install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "8000"]
CMD ["git_resume.app:app"]
