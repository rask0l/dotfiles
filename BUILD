load(
    "@io_bazel_rules_pex//pex:pex_rules.bzl",
    "pex_binary",
    "pex_library",
    "pex_test",
    "pex_pytest",
)

#load(
#    "//tools/pypi_package.bzl",
#    "pypi_package",
#)

pex_binary(
    name = "dotm_pex",
    main = "dotm.py",
    deps = [
        "//dotm:dotm"
    ],
    srcs = [
        "dotm.py",
    ],
    interpreter = "python3",
)

#pypi_package(
#    name = "dotm_pkg",
#    version = "1.0.0",
#    description = "Dotfiles manager for python3",
#    long_description = "README.md",
#    classifiers = [
#        "Development Status :: 4 - Beta",
#        "Environment :: Console",
#        "Intended Audience :: Developers",
#        "License :: OSI Approved :: MIT License",
#        "Operating System :: POSIX",
#        "Programming Language :: Python :: 3",
#        "Programming Language :: Python :: 3.6",
#        "Topic :: Software Development :: Libraries :: Python Modules"
#    ],
#    keywords = "dotfiles",
#    url = "https://github.com/nckturner/dotm",
#    author = "Nick Turner",
#    author_email = "nturner4@gmail.com",
#    license = "MIT",
#    packages = [":dotm"],
#    test_suite = "nose.collector",
#    tests_require = ["nose"],
#)
