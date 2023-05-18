preinstall:
	# Go to the project root directory before installation
	python3 -m venv ./venv
	source venv/bin/activate #【Execute it manually】
install:
	# install commands
	pip install --upgrade pip
	pip install -r requirements.txt
format:
	# format code
	black --diff --color ./

lint:
	# flask8 or pylint
	pylint --disable=R,C *.py
test:
	# test
build:
	# build container
deploy:
	# deploy

all: install lint test deploy

#proto make
#GRPC_ROOT = ./_grpc
#PROTO_DIR = $(GRPC_ROOT)/protos
#PY_DIR = $(GRPC_ROOT)/py
#PROTO_FILES = $(wildcard $(PROTO_DIR)/*.proto)
## lib
#PROTOBUF_DIR=venv
#GRPC_DIR=venv
#
#generate:
#	python -m grpc_tools.protoc \
#	-I$(PROTO_DIR) \
#	--python_out=$(PY_DIR) \
#	--grpc_python_out=$(PY_DIR) \
#	$(PROTO_FILES)
#	$<