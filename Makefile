.PHONY: build run test

build: 
	bazel build //:dotm

test:
	python3 test/test_modules.py
