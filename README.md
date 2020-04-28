# TraversingClangASTpython
A simple guide on how to use libclang to travers clang's AST via python

## Steps for Linux
Tested On Ubuntu

### Install clang
Make sure the clang is installed. Otherwise, run the command below to install clang
```sh
$ sudo apt-get install clang
```

### Create a link to libclan.so.1
Clan's python binding looks for libclang.so.1.
If libclang is not linked properly, and error will be thrown. Something like this:
```sh
Loading libclang failed, completion won't be available. Consider setting g:clang_library_path
```
