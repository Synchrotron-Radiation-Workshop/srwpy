# This Makefile is to compile SRW with optional compilation of FFTW-2.1.5.

root_dir = $(realpath .)
gcc_dir = $(root_dir)/gcc
fftw_version = fftw-2.1.5
fftw_dir = $(fftw_version)
fftw_file = $(fftw_version).tar.gz

nofftw: core

all: clean fftw core

fftw:
	wget http://www.fftw.org/$(fftw_file) && \
	tar -xvf $(fftw_file) && \
	cd $(fftw_dir) && \
	CFLAGS=-fPIC ./configure --enable-float --with-pic && \
	make -j8 && \
	cp fftw/.libs/libfftw.a $(gcc_dir) && \
	cd $(root_dir) && \
	rm -rf $(fftw_file) $(fftw_dir);

core: 
	cd $(gcc_dir) && make -j8 lib

clean:
	rm -f $(gcc_dir)/libfftw.a $(gcc_dir)/libsrw.a && \
	rm -f $(root_dir)/$(fftw_file) && \
	rm -rf $(root_dir)/$(fftw_dir)/

.PHONY: all clean core fftw nofftw
