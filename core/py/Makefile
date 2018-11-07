.PHONY: python clean

python: srwlpy.so

srwlpy.so:
	python setup.py build_ext --build-lib='../gcc'
	rm -rf build

clean:
	rm -rf build
	rm -f ../gcc/srwlpy*.so
