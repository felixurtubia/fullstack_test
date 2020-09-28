FROM python:3-alpine
ADD . /fullstack_test
WORKDIR /fullstack_test

RUN apk update && apk add gcc python3-dev musl-dev libffi-dev
RUN pip install -r requirements.txt
RUN pip install uwsgi

ENV PORT=8000
EXPOSE 8000

RUN chmod +x /fullstack_test/initialize.sh
CMD ["/fullstack_test/initialize.sh"]
