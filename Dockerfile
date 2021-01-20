FROM python:3.8

WORKDIR /croneval

COPY . .

RUN pip install --no-cache-dir .

CMD [ "croneval"]