Linux系统下源码编译安装MySQL（Ubuntu）
---

# 安装前准备

- 查看 MySQL是否以安装

# 源码安装 MySQL 的步骤

- 下载源码
- 解压
- 安装

# 演示

## 下载源码

- 下载方式1

  根据 MySQL 参考手册 [2.1.3 How to Get MySQL](https://dev.mysql.com/doc/refman/8.0/en/getting-mysql.html) 的提示：

  - 点击 [MySQL下载地址](https://dev.mysql.com/downloads/)
  - 点击 [MySQL 社区版](https://dev.mysql.com/downloads/mysql/)
  - 选择合适的版本，如 **Linux - Generic (glibc 2.12) (x86, 64-bit), Compressed TAR Archive**，然后点击 `Download`。
  - 点击 `Download` 后会提示登陆注册，直接看到最下面，点击 **[No thanks, just start my download](https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.23-linux-glibc2.12-x86_64.tar)** 进行下载。

- 下载方式2

  如果我们是在命令行操作，那么可以使用 wget 工具进行下载。

  ```
  wget https://cdn.mysql.com//Downloads/MySQL-8.0/mysql-8.0.23-linux-glibc2.12-x86_64.tar.xz
  ```

## 解压

- 进入到源码所在的目录，根据 [MySQL 参考手册2.9.4](https://dev.mysql.com/doc/refman/8.0/en/installing-source-distribution.html) 的指导使用 `tar` 命令进行进行解压。

```
$ tar -xJvf mysql-8.0.23-linux-glibc2.12-i686.tar.xz
```

说明：

（1）x：extract 解压。

（2）J：我们可以看到压缩包的后缀是 xz ，说明文件是使用 xz 的支持压缩的。J 指定使用使用 xz 的支持进行解压。

（3）v：--verbose，详细地列出处理文件。

（4）f ：--file，指定要解压的文件。

## 编译

### make

### cmake

我们将 MySQL 文件解压后得到的是 **源码**。Linux 系统真正识别的 **可执行文件** 是 **二进制程序**，所以需要将源码转为二进制程序。将源码转为二进制程序的过程称为**编译(compile)**。先编译这个还是先编译哪个，称为**构建(build)**。而 Linux 系统下构建最常用的工具是 [Make](https://en.wikipedia.org/wiki/Make_%28software%29)。关于Make的详细介绍，见 [Make 命令教程](https://www.ruanyifeng.com/blog/2015/02/make.html)。下面使用 Make 命令进行编译。

* 生成makefile

  需要指定boost。需要指定目录。

# 参考资料

[1] MySQL 参考手册：

[2] Make 命令教程：https://www.ruanyifeng.com/blog/2015/02/make.html



