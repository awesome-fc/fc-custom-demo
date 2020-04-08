init:
	docker run -it -v $$(pwd):/tmp mcr.microsoft.com/dotnet/core/sdk:3.1 bash -c "cd /tmp && mkdir FSharpDemo && cd FSharpDemo && dotnet new webapi --language F# && python /tmp/init_helper.py"

build:
	docker run -it -v $$(pwd):/tmp mcr.microsoft.com/dotnet/core/sdk:3.1 bash -c "cd /tmp/FSharpDemo && dotnet publish -r linux-x64 -c Release --self-contained true && cd /tmp/FSharpDemo/bin/Release/netcoreapp3.1/linux-x64/publish && mv FSharpDemo bootstrap && chmod +x bootstrap"

deploy: build
	fun deploy -y