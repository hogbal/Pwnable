FROM ubuntu:20.04
MAINTAINER hogbal31@gmail.com

ARG user=hogbal
ARG user_passwd=hogbal

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install sudo -y && \
    apt-get install net-tools -y && \  
	apt-get install openssh-server -y && \
	apt-get install vim -y && \
	apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential -y && \
	apt-get install ruby -y && \
	apt-get install zsh -y && \
	apt-get install fonts-powerline -y && \
	apt-get install language-pack-en -y && \
	apt-get install gdb -y && \
	apt-get install tmux -y && \
	pip3 install ropgadget && \
	update-locale

RUN useradd -m ${user} -s /bin/zsh && \
    adduser ${user} sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER ${user}

#install vim
COPY vimrc /home/${user}/.vimrc

#install pwntools
WORKDIR /home/${user}
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade pwntools

#install peda
WORKDIR /home/${user}
RUN git clone https://github.com/longld/peda.git /home/${user}/peda

#install Pwngdb
RUN git clone https://github.com/scwuaptx/Pwngdb.git && \
    cp /home/${user}/Pwngdb/.gdbinit /home/${user}/


#install one_gadget
WORKDIR /home/${user}
RUN git clone https://github.com/david942j/one_gadget.git /home/${user}/one_gadget
WORKDIR /home/${user}/one_gadget
RUN sudo gem install one_gadget

#install oh my zsh
WORKDIR /home/${user}
RUN sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)" && \
	sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="agnoster"/' /home/${user}/.zshrc && \
	git clone https://github.com/zsh-users/zsh-syntax-highlighting.git /home/${user}/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting && \
	git clone https://github.com/zsh-users/zsh-autosuggestions  /home/${user}/.oh-my-zsh/custom/plugins/zsh-autosuggestions&& \
	sed -i 's/plugins=(git)/plugins=(git zsh-syntax-highlighting zsh-autosuggestions)/' /home/${user}/.zshrc

#git clone pwnable
RUN git clone https://github.com/${user}/pwnable.git /home/${user}/pwnable

USER root

#ssh config
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

#set password
RUN echo 'root:root' | chpasswd
RUN echo ${user}:${user_passwd} | chpasswd

EXPOSE 22

RUN service ssh start
CMD ["/usr/sbin/sshd", "-D"]
