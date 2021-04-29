FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install net-tools -y
RUN apt-get install openssh-server -y
RUN apt-get install fonts-powerline -y
RUN apt-get install zsh -y
RUN apt-get install language-pack-en -y
RUN update-locale

RUN useradd -m hogbal -s /bin/zsh

#install vim
RUN apt-get install vim -y
COPY vimrc /home/hogbal/.vimrc

#install pwntools
WORKDIR /home/hogbal
RUN apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential -y
RUN wget https://bootstrap.pypa.io/pip/3.5/get-pip.py 
RUN python3 get-pip.py
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade pwntools

#install gdb-peda
WORKDIR /home/hogbal
RUN git clone https://github.com/longld/peda.git /home/hogbal/peda
RUN git clone https://github.com/scwuaptx/Pwngdb.git
RUN cp /home/hogbal/Pwngdb/.gdbinit /home/hogbal/

#install ropgadget
RUN pip3 install ropgadget

#install one_gadget
WORKDIR /home/hogbal
RUN apt -y install software-properties-common
RUN apt-add-repository ppa:brightbox/ruby-ng
RUN apt update
RUN apt install ruby2.4 -y
RUN git clone https://github.com/david942j/one_gadget.git /home/hogbal/one_gadget
WORKDIR /home/hogbal/one_gadget
RUN gem install one_gadget

USER hogbal

#install oh my zsh
WORKDIR /home/hogbal
RUN sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
COPY zshrc /home/hogbal/.zshrc
USER root

#git clone
RUN git clone https://github.com/hogbal/pwnable.git /home/hogbal/pwnable

#ssh config
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

#set password
RUN echo 'root:root' | chpasswd
RUN echo 'hogbal:1234' | chpasswd

EXPOSE 22

RUN service ssh start
CMD ["/usr/sbin/sshd", "-D"]
