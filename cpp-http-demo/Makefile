build-img:
	docker build -t fc-cpp-centos-dev -f build-image/Dockerfile build-image

build: build-img
	docker run --rm -it -v $$(pwd):/tmp fc-cpp-centos-dev bash -c "cd /tmp && ./build.sh"

deploy: build
	fun deploy -y