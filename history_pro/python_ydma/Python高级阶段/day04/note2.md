linux 常用命令
    对文件操作命令
    对文件和目录都能操作命令
    权限管理

    ls -l

    -rw-r--r--      root    root    test1.py
    权限位           属主    属组      文件名

    第一位 文件类型 - 普通文件 d dir 目录    | link 连接文件

    第二三四位   属主权限    u   user    rw-

    第五六七位   数组权限    g   group   r--

    第七八九十位  其他人     o   other   r--

    r read可读    w   write 可写 x exe 可执行 - 无权限

    4            2              1           0


    drwx-xr-x   root    root    txt（目录）

    lrwxrwxrwx  root    root    t1.py->test1.py(链接文件）

    系统默认建立的普通文件权限       644
    系统默认建立的目录权限          755
    系统默认建立的链接文件权限       777
    系统最大权限  777 系统最小权限 000

    所以说在linux系统中，不会有病毒，病毒没有权限