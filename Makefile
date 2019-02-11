DOCKER_USERNAME := dalloriam

.PHONY: deps
deps:
	@echo "+ $@"
	@pip install -r requirements.txt


.PHONY: build
build: deps
	@echo "+ $@"
	@python make_all.py --uname $(DOCKER_USERNAME)


.PHONY: push
push: deps
	@echo "+ $@"
	@python make_all.py --uname $(DOCKER_USERNAME) --push