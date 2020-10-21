FROM aliyunfc/runtime-custom:base
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak
COPY ./sources.list  /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y cmake