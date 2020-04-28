# Traversing Clang's AST with python
A simple guide on how to use libclang to travers clang's AST via python

## Steps for Linux
Tested On Ubuntu

### Install clang
Make sure the clang is installed. Otherwise, run the command below to install clang
```sh
$ sudo apt-get install clang
```

### Create a link to libclan.so
Clang's python binding library looks for libclang.so

First, make sure that the libclang.so is available, just check where it is located?
```sh
$ whereis libclang.so
```
If nothing is returned, that means libclang.so is not available.

If libclang is not linked properly, an error will be thrown. Something like this:
```sh
clang.cindex.LibclangError: libclang.so: cannot open shared object file: No such file or directory. To provide a path to libclang use Config.set_library_path() or Config.set_library_file().
```
By default, `libclang.so` is located in this directory (or somewhere similar):
```sh
/usr/lib/x86_64-linux-gnu
```
find the `libclang-\<version>.so.1` in this directory, and link it to the `libclang.so` by running the following command
```sh
$ sudo ln -s libclang-10.so.1 libclang.so
```

### Setting up the clang python library
Download the last version of [clang source code](https://releases.llvm.org/download.html).
inside the downloaded file go to the following directory:
```sh
bindings/python/
```

and copy the `clang` folder to the `lib` folder of your python interpreter.
If you are not sure about where python is installed, just run the following python code snippet to find the location of python interpreter.
```sh
import sys
print(sys.executable)
```

That's all.
