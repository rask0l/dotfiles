.PHONY: build run test

build: 
	bazel build //:dotm

run:
	bazel run //:dotm

test:
	python3 test/test_modules.py
