# pwnable docker

This docker image is an image with environment settings for studying pwnable.

Pull image from [docker hub](https://hub.docker.com/repository/docker/hogbal/pwnable).

## installed 
* vim
* pwntools
* gdb-peda
* Pwngdb
* ropgadget
* one gadget
* oh my zsh
* ssh

## docker run
set user and user_passwd as ARG in Dockerfile.

### No ARG setting
```
docker run -it -p [host port]:22 hogbal/pwnable:[Tag]
```

### ARG setting
```
docker run -it -p [host port]:22 hogbal/pwnable:[Tag] user=[username] userpasswd=[userpasswd]
```

## Dockerfile table
|Tag|summary|Dockerfile|
|:---:|:---:|:------:|
|ubuntu20.04|using ubuntu:20.04 image|[ubuntu20.04 Dockerfile](https://github.com/hogbal/pwnable/blob/master/docker/ubuntu20.04/Dockerfile)|
|ubuntu18.04|using ubuntu:18.04 image|[ubuntu18.04 Dockerfile](https://github.com/hogbal/pwnable/blob/master/docker/ubuntu18.04/Dockerfile)|
|ubuntu16.04|using ubuntu:16.04 image|[ubuntu16.04 Dockerfile](https://github.com/hogbal/pwnable/blob/master/docker/ubuntu18.04/Dockerfile)|

