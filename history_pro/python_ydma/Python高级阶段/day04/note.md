## Linux常用命令

---

### 对文件操作命令

建立空文件

touch    test1.py     

touch     a.txt  

ls -l 

修改时间

touch  -t   201706181919  a.txt 

ls  -l 



删除文件（目录）

mkdir   -p   aa/bb/cc

rm  -rf    aa      -r  删除目录    -f  强制 

rm   -rf   a.txt     删除文件

查看文件内容命令

cat   install.log   查看文件内容

cat  -n  install.log   查看文件内容包括行号      适合查看文件内容较少



more  install.log    分页显示文件内容   空格  向下翻页   b  向上翻页  退出  q



head     install.log    默认显示文件前10行

head   -n  20  install.log     -n 显示行

head  -20  install.log  



tail    install.log     默认显示文件后10行

tail   -n  20   install.log    -n  行数

tail   -20  install.log   

快捷键  

​		清屏   clear   =  ctrl  + l 

​	         强制终止   ctrl  +   c   

​	         补全      Tab     命令补全   文件/目录补全

链接 （快捷方式）

ln    -s   test1.py     t1.py     同一目录下建立链接文件

​             源文件       链接文件

ln    -s   /root/test1.py    /tmp/t3.py    跨目录建立链接文件    绝对路径

ls   -l   /tmp

### 对文件和目录都能操作的命令

复制  cp

同一目录下复制文件  

cp   test1.py    tt.py 

ls 

跨目录复制文件

cp   test1.py   /tmp/

ls   /tmp

复制目录 

cp   -r   /tmp   /root     复制目录 /tmp  到 /root下     -r  复制目录     -a  = -pdr

ls  /root/



剪切和改名

mv   tt.py   02.py    改名 

mv  02.py  tmp   剪切到目录tmp下 

mkdir  txt

mv  tmp  txt    剪切目录到txt目录下

ls  txt

### 权限管理

ls   -l   

-rw-r--r--  644       root      root               test1.py      普通文件   

权限位          属主      属组              文件名 

第一位   文件类型  -  普通文件     d   dir 目录        l  link   链接文件

第二三四位    属主权限 u   user       rw-       4+2+0   6

第五六七位    属组权限 g    group     r--                     4

第八九十位     其它人    o    other      r--                     4



r    read 可读       w   write   可写      x  exe  可执行      -   无权限

4                          2                           1                           0

drwxr-xr-x    755     root      root      txt   (目录) 

lrwxrwxrwx   777   root     root     t1.py -> test1.py   (链接文件)

系统默认建立的普通文件权限  644   

系统默认建立的目录权限    755

系统默认建立的链接文件权限  777

系统最大权限  777     系统最小权限 000



修改权限

chmod   u+x   test1.py   添加属主执行权限

ls -l  test1.py   

chmod  u-x  test1.py   去除属主执行权限

ls  -l    test1.py

chmod  u=rwx  test1.py   对属主权限赋值rwx

ls  -l   test1.py

chmod  u-x,g+w,o+w  test1.py

ls -l  

chmod  a+x   test1.py     a  所有   全加上执行权限

chmod    +x   test1.py     添加所有执行权限

chmod     -x    test1.py      去除所有执行权限

ls   -l   test1.py

chmod   a+w   test1.py     添加所有写权限       



chmod   777  test1.py    

chmod   644  test1.py 

chmod   000  test1.py   



添加用户   

useradd   python

passwd  python   设置密码

修改属主/属组命令

chown    python   test1.py    修改属主

ls -l  test1.py

chown   :python   test1.py    修改属组 

ls -l   test1.py  

chown   python:python   txt    同时修改属主/属组

ls  -l

纳米编辑器

nano   hello.py  

### 帮助命令

man   ls

man   rm           空格 向下      q  退出

帮助选项   --help

ls   --help

### 查找命令 

whereis    ls    查找文件命令所在的位置

find     查找命令 

按照文件名查找

find    /root    -name  hello.py      

find   /root  -name   test1.py

find   /root   -name   index.html

find   /    -name   index.html                              -iname   不区分大小写

 按照用户名查找    -user

find   /root   -user   root

find   /   -user   python

按照组名查找   -group

find  /root   -group   root

find   /   -group   python

按照nouser查找

find  /    -nouser   

按照文件类型查找  -type       普通文件  f    目录文件  d    链接文件  l

find  /  -type     f

find  /  -type    d

find  /   -type     l

按照文件权限查找  -perm      644     755     777    000

find   /   -perm     644

find  /   -perm    755

find   /  -perm     777

find   /  -perm   000

按照文件大小查找  -size      +5k       -5k      5k      M     G

find    /    -size   +5k

find   /   -size   -5k

find   /    -size    +10M

find   /   -size   +10M   -a  -size   -20M

find    /   -size   +10M  -a  -size   -20M    -exec   ls   -l    {}  \;

find    /   -size   +10M  -a  -size   -20M    -exec  rm   -rf  {}  \;     -exec    不提示

find    /   -size   +10M  -a  -size   -20M    -ok  rm   -rf  {}  \;      -ok    提醒



查找文件内容   grep 

grep   "root"    install.log    查找含有root 的行

grep  -n  "root"   install.log    显示行号

grep  -i   "ROOT"   install.log    忽略大小写

grep   -v  "root"  install.log    反向查找

grep  -v   "i686"   install.log   



管道符     |     （连接命令）

ls   -l   /etc/    |   more      

cat  -n  install.log   |   grep  "zip"

### 压缩与解压缩

.tar.gz    

tar  -zcvf       p1.tar.gz     test1.py  install.log    压缩文件

ls

tar   -zxvf     p1.tar.gz    解压缩  

ls

tar  -ztvf    p1.tar.gz  查看不解压

tar   -zxvf   p1.tar.gz   -C   txt     定向解压缩

ls   txt



.tar.bz2

tar  -jcvf      txt.tar.bz2    txt    压缩目录

ls

tar  -jxvf    txt.tar.bz2   解压缩

tar  -jtvf    txt.tar.bz2    查看不解压

tar   -jxvf    txt.tar.bz2   -C   /tmp    定向解压缩

### 关机和重启命令

shutdown  -h  now     现在关机 

init  0  关机



shutdown   -r   now    重启系统 

reboot   重启系统 

init  6  重启

挂载命令        /mnt    /media  

挂载光盘 

1. 物理连接    2.手动挂载


   mount     光驱设备名   （/dev/sr0    /dev/cdrom）     挂载点  /media   /mnt  (手动建立挂载点      mkdir  /mnt/cdrom)

   ​

   mount   /dev/sr0    /media

   cd  /media/

   ls   

2. 卸载    umount 

   umount  /dev/sr0   

   umount  /media

### 网络命令

ping     测试网络连通性

ping   -c   5   192.168.2.222  



ifconfig     查看网络设备    Linux  

ipconfig        windows  

ipconfig   /all



### 作业

写两遍   一遍 html文档   一遍 课堂笔记

练习至少三遍       记忆（背）

完成练习



#### 1.Linux常用命令练习

```
1.root用户的命令提示符
[root@localhost ~]#

2.普通用户命令提示符
[user@localhost ~]$

3.重启和马上关机
重启：shutdown -r now 、 init 6
马上关机：shutdown -h now  、init 0
 
4.帮助命令
man 、 --help

5.查看当前工作目录
pwd

6.切换工作目录到/etc
cd /etc

7.切换到宿主目录（家目录）
cd 、cd~ 、cd ../../root 、 cd /root 、cd /home

8.显示/etc下所有的目录内容，包括隐藏文件
ls -a /etc

9.以长格式显示/etc下的内容
ls -al /etc

10.以长格式显示/etc目录本身的内容
ls -dl /etc

11.创建/etc/test目录 
mkdir /etc/test

12.创建/etc/test/file的空文件
touch /etc/test/file

13.拷贝文件file01.txt为file02.txt
cp file01.txt file02.txt

14.拷贝目录/tmp为/var/tmp
cp -r /tmp /var/tmp

15.删除文件file.txt
rm -r file.txt -->Y

16.删除目录/test
rm -r /test -->Y
rmdir test

17.强制删除/test目录
rm -rf /test

18.将文件file01.txt重命名为file02.txt
mv file01.txt file02.txt

19.将/etc/file.txt移动到/tmp下
mv /etc/file.txt /tmp

20.将/etc/file.txt移动到/tmp下并重命名为new.txt
mv /etc/file.txt /tmp/new.txt

21.查找/etc下名为file.txt的文件
find /etc -name file.txt

22.分页显示file.txt的内容
more file.txt

23.将a.php和b.html两个文件打包并压缩成new.tar.gz
tar -zcnf new.tar.gz a.php b.html

24.将a.php和b.html两个文件打包并压缩成new.tar.bz2
tar -jcnf new.tar.bz2 a.php b.html

25.使用ping来测试网络的连通性，并指定发包数为5次
ping -c 5 192.168.2.199

26.临时设置网卡的ip为192.168.10.250


27.写出系统默认建立的文件和目录的权限位
默认文件权限：644
默认目录权限：755

28.显示系统命令ls所在的目录
whereis ls

29.显示文件file.txt中含有#号的行
grep -n '#' file.txt

30.显示文件file.txt中没有#号开头的行
grep -v '#' file.txt

31.赋予文件/test/file所属组写权限
chmod g=w /test/file

32.修改目录/dir所有用户具有的全部权限
chmod 777 /dir

33.改变文件/test/file的所有者为phper
chown phper /test/file

34.改变文件/test/file的所属组为 lampbrother
chown :lampbrother /test/file

35.挂载光盘镜像文件步骤
1、物理连接 2、手动挂载 3、识别设备
```





​                                                                     