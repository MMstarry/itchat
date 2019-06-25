# itchat
微信机器人 土味情话

# 部署在服务器上

我们先检查一下云主机目前的python版本，使用命令：
python --version
，查看：


提醒大家千万不要将python2删除，因为有些系统功能依赖python2，所以我们只要添加python3就可以。

我们来用putty远程链接我们的云主机，然后执行下面的安装命令
首先安装依赖包，centos里面是-devel，如果在ubuntu下安装则要改成-dev，依赖包缺一不可，一步一步复制到终端执行就可以！

sudo yum -y groupinstall "Development tools" sudo yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel

然后下载python3.7的安装包(目前更新到了python3.7.3)

wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz

解压下载包

tar -xvJf  Python-3.7.3.tar.xz

编译安装

cd Python-3.7.3 ./configure --prefix=/usr/local/bin/python3 sudo make sudo make install

创建软连接

ln -s /usr/local/bin/python3/bin/python3 /usr/bin/python3 ln -s /usr/local/bin/python3/bin/pip3 /usr/bin/pip3

最后输入命令 python3 --version 检查一下是否安装成功

项目自行上传到服务器，路径自选
下载项目必须库
pip3 install 库名


再cd 进入项目路径

cd 项目路径

安装screen

yum install -y screen

运行的命令

screen python3 要运行py文件

ctrl+A 然后按D，screen会关闭

.查看正在运行的程序

screen -ls

现在关闭终端，在screen中的程序会继续后台运行

结束
[root@localhost ~]# screen -ls
There are screens on:
9975.pts-0.localhost (Detached)
4588.pts-3.localhost (Detached)
2 Sockets in /var/run/screen/S-root.
 
[root@localhost ~]# screen -X -S 4588 quit
[root@localhost ~]# screen -ls
