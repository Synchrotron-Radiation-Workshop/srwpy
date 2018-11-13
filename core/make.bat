@echo on

msbuild vc\\SRWLIB.vcxproj /maxcpucount:%NUMBER_OF_PROCESSORS% -property:Configuration="Release";Platform="x64"

