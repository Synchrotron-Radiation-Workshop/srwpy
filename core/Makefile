# This Makefile is to compile SRW with optional compilation of FFTW-2.1.5.

root_dir = $(realpath .)
gcc_dir = $(root_dir)/gcc
fftw_version = fftw-2.1.5
fftw_dir = $(fftw_version)

nofftw: core

all: clean fftw core

fftw:
	git clone https://github.com/PaNOSC-ViNYL/FFTW.git $(fftw_dir) && \
	cd $(fftw_dir) && \
	CFLAGS=-fPIC ./configure --enable-float --with-pic && \
	make -j8 && \
	cp fftw/.libs/libfftw.a $(gcc_dir) && \
	cd $(root_dir) && \
	rm -rf $(fftw_dir);

core:
	cd $(gcc_dir) && make -j8 lib

clean:
	rm -f $(gcc_dir)/libfftw.a $(gcc_dir)/libsrw.a && \
	rm -rf $(root_dir)/$(fftw_dir)/

.PHONY: all clean core fftw nofftw
