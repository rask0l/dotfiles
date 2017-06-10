INSTALL ?= ~/bin

.PHONY: build run test

build:
	bazel build //:dotm

test:
	python3 test/test_modules.py

install:
	mkdir -p $(INSTALL)
	if [ -f $(INSTALL)/dotm ]; then \
		rm -f $(INSTALL)/dotm; \
	fi
	cp -au bazel-bin/dotm.pex $(INSTALL)/dotm
	chmod +rwx $(INSTALL)/dotm
