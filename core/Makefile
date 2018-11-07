# This Makefile is to compile SRW C++ core

root_dir = $(realpath .)
gcc_dir = $(root_dir)/gcc
py_dir = $(root_dir)/py


all: core pylib

core: 
	cd $(gcc_dir); make -j8 clean lib

pylib:
	cd $(py_dir); make python

.PHONY: all core pylib
