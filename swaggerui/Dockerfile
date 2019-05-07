FROM ubuntu:16.04
WORKDIR /build

RUN apt-get update && apt-get -y install git && git clone https://github.com/dalloriam/swagger-ui.git && cd swagger-ui && git checkout 2.x

FROM nginx:latest
WORKDIR /data
COPY --from=0 /build/swagger-ui/dist /usr/share/nginx/html
