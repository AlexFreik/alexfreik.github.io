JEKYLL_VERSION := 4.0

docker:
	docker run \
		--rm -it \
		--mount type=bind,source="$(shell pwd)",target=/srv/jekyll \
		jekyll/jekyll:$(JEKYLL_VERSION) \
		jekyll build
docker-build:
	docker build -t alexfreik-webpage .
