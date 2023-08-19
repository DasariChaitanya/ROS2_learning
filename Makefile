# --original
# https://stackoverflow.com/a/14061796
# If the first argument is "run"...
# ifeq (run,$(firstword $(MAKECMDGOALS)))
#   # use the rest as arguments for "run"
#   RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
#   # ...and turn them into do-nothing targets
#   $(eval $(RUN_ARGS):;@:)
# endif

# Define default values for arguments
file ?= docker/dockerfile
target ?= base
image_name ?= test_image
container_name ?= test_container

DOCKER_ARGS = \
	--env="DISPLAY=host.docker.internal:0.0"\
	--env="LIBGL_ALWAYS_INDIRECT=0"
    # --env="DISPLAY" \
	# --env="QT_X11_NO_MITSHM=1" \
    # --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw"
	
.PHONY: build run terminal kill stop
build:
	@docker build -f $(file) --target $(target) -t $(image_name):$(target) .

run:
	@docker run -it ${DOCKER_ARGS} --name $(container_name) $(image_name):$(target) bash

terminal:
	@docker exec -it $(container_name) bash

kill:
	@docker rm $(container_name)

stop:
	@docker stop $(container_name)