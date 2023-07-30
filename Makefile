DOCKER_ARGS = \
    --env="DISPLAY=host.docker.internal:0.0"

# @ suppresses the command to be printed before it is executed which is default behavior
.PHONY: build
build:
	@docker build -f docker/dockerfile --target overlay -t test_image:overlay .

.PHONY: term
term:
	@docker run -it ${DOCKER_ARGS} --name test_container test_image:overlay bash
