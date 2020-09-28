FROM python:3-alpine
ADD . /fullstack_test
WORKDIR /fullstack_test

RUN pip install -r requirements.txt
RUN pip install uwsgi

ENV PORT=8000
EXPOSE 8000

CMD ["/fullstack_test/initialize.sh"]
