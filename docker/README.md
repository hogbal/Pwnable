# pwnable docker

pwnable을 위한 환경 셋팅이 되어있는 docker image입니다.

image를 pull하고싶으면 [docker hub](https://hub.docker.com/repository/docker/hogbal/pwnable)를 참고하세요.

## installed 
* vim
* pwntools
* gdb-peda
* Pwngdb
* ropgadget
* one gadget
* oh my zsh
* ssh
* tmux

## docker run
user와 user_passwd가 ARG로 설정되어 있습니다.

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

