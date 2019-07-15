FROM alpine:3.7

WORKDIR /app
COPY . /app

RUN apk add python-dev
RUN apk add py-pip
RUN pip install flask
RUN apk add --update sqlite
RUN pip install uuid
RUN pip install requests

EXPOSE 80

ENV TEAM_ID =CC_037_043_048_051

CMD ["python","acts.py"]
