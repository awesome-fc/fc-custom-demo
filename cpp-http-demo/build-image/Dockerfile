FROM centos:7
RUN yum update -y
RUN yum  install -y gcc gcc-c++ libcurl-devel.x86_64 openssl openssl-devel tar wget

RUN mkdir -p /tmp/cmake && \
  pushd /tmp/cmake && \
  wget 'https://cmake.org/files/v3.20/cmake-3.20.4-linux-x86_64.sh' && \
  bash cmake-3.20.4-linux-x86_64.sh --prefix=/usr/local --exclude-subdir && \
  popd && \
  rm -rf /tmp/cmake

RUN yum install -y centos-release-scl
RUN yum-config-manager --enable rhel-server-rhscl-7-rpms
RUN yum install -y devtoolset-7
RUN yum update scl-utils