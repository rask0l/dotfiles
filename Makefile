INSTALL ?= ~/bin

.PHONY: build run test

build: 
	bazel build //:dotm

test:
	python3 test/test_modules.py

install: 
	mkdir -p $(INSTALL)
	cp bazel-bin/dotm.pex $(INSTALL)/dotm
	chmod +rwx $(INSTALL)/dotm
