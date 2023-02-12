FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN make dev-install



