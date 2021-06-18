FROM centos:7
COPY ./libcppruntime.so /usr/lib/libcppruntime.so
ENV LD_LIBRARY_PATH=/usr/lib
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ./bootstrap  ./bootstrap
ENTRYPOINT ["/usr/src/app/bootstrap"]