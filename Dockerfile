FROM python:3.10-alpine

RUN apk add --update --no-cache --virtual .build-deps gcc musl-dev \
&& pip install --upgrade pip \
&& adduser -D manolo

WORKDIR /app

COPY ./app /app
RUN chown -R 1000:1000 /app 
RUN pip3 install  --no-cache-dir -r requirements.txt
RUN rm -rf ~/.cache/pip && apk del .build-deps 

CMD ["python", "main.py"]