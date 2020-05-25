# 百度电话面试笔记

### 抽象类与接口的区别

1. 定义上, 抽象类是一个类,是没有描述完整的类,含有抽象的方法.接口是一个抽象类型,是一个抽象方法的集合
2. 内容上,抽象类可以包含属性和方法,可以有已经实现的方法,但是接口只有方法,且是抽象方法
3. 使用上, 都不能实例化. 类只能单继承,子类可以实现其抽象方法. 接口可以多继承, 子类必须实现所有抽象方法. 接口认为是类为了实现多继承而设计

### require_once 与 include_once 的区别

+ include_once 是包含,如果出错,会警告

+ require_once是必须,如果出错,是致命错误

### 操作系统的进程通信方式

+ 管道

+ 信号

  ```python
  # python 使用demo
  import signal
  # Define signal handler function
  def myHandler(signum, frame):
      print("Now, it's the time")
      exit()
  
  # register signal.SIGALRM's handler 
  signal.signal(signal.SIGALRM, myHandler)
  signal.alarm(5)
  while True:
      print('not yet')
  ```

+ 套接字

+ 消息队列

+ 共享内存

+ 信号量

  ### nginx 与php通信的套接字区别

+ tcp 套接字, 因特网,效率相对低,但是可以多个机器
+ unix套接字, 文件系统,地址是文件名.大并发长缓存可能会报错

###  nginx反向代理与负载均衡

+ 负载均衡upstream

  ```nginx
  http {
      upstream myServer {
          server 127.0.0.1:8081;
          server 127.0.0.1:8082;
      }
      server {
          listen 80;
          location / {
              proxy_pass http://myServer;
          }
      }
  }
  ```

+ 反向代理proxy_pass

  ```nginx
     location /b {
              rewrite ^/b(.*) /$1 break;
              proxy_pass http://127.0.0.1:8081
          }
  
          # 反向代理
          location /c {
              rewrite ^/c(.*) /$1 break;
              proxy_pass http://127.0.0.1:8082
          }
         }
  ```



### 操作系统死锁避免

1. 死锁产生的条件
   + 互斥, 不可使用其他进程占用的资源
   + 占有且等待, 等待其他进程的时候,继续占用资源不释放
   + 不可抢占
   + 循环等待
2. 避免
   + 允许抢占式
   + 资源分配, 按照银行家算法分配资源,保证处于安全状态

### php实现301 跳转

header( "HTTP/1.1 301 Moved Permanently" ) ;

header("Location:url")

### http协议理解

+ 无状态, 为了保持简单的特点,不会对发送或者接受的消息进行持久化处理, 采用cookie
+ 无连接, 每次连接只处理一个请求, 后来有了keep-alive
+ 灵活,各种数据类型,通过content-type
+ 简单,只用传输请求方法与url 

### http 304 状态码

表示未修改, 当有缓存的界面重新请求的时候会带上Etag字段,对比服务器生成的新的资源,如果Etag没有变化,则只返回消息头.减少了带宽与资源消耗

### tcp 3次握手4次挥手

问题一, 为什么要三次握手?

答:确定客户端和服务器端的发送, 接受能力是否正常.以及同步双方的序列号和确认号

> SYN, ACK,Seq,AckNumber 
>
> SYN(synchronous建立联机) ACK(acknowledgement 确认) PSH(push传送) FIN(finish结束) RST(reset重置) URG(urgent紧急)Sequence number(顺序号码) Acknowledge number(确认号码)
>
> 所以Syn=1 表示建立连接的标志. ack=1 是确认, 非第一次请求的对话基本都有一个确认.每一个seq=x都有一个确认的ackNumber=x+1

1. 第一次握手, 客户端发送一条消息到服务端. 服务器端知道了客户端发送能力ok, 服务器接受能力ok

   发送syn=1, seq=x

2. 第二次握手,客户端知道了自己发送能力ok,服务器接受和发送都ok

   发送syn=1, ack=1,ackNumber=x+1, seq=y

3. 第三次握手, 服务器段知道了自己发送能力ok,以及客户端接受能力ok

   发送ackNumber=y+1,ack=1

   经历了上面的三次握手过程，客户端和服务端都确认了自己的接收、发送能力是正常的。之后就可以正常通信了。

问题二,  四次挥手?(任意一方可以开始)

1. 客户端发送FIN=1, Seq=x到服务器, 表示客户端关闭了发送
2. 服务器发送ack=1,ackNumber=x+1.表示知道客户端关闭发送了.但是接受未关闭
3. 服务器发送FIN=1,Seq=y确定关闭服务器端发送功能
4. 客户端确认关闭, 发送ack=1, ackNumber=y+1

问题三, 为什么多一次挥手?

挥手的时候, 因为可能存在服务器端依然在发送数据,所以分为先发送ack确认,然后等在数据传输完毕之后再次发送fin表示自己关闭了发送.

### mysql建立索引的准则

1. 常用作查询的字段建立索引
2. 常用来排序分组的字段建立索引
3. 合理使用前缀索引
4. 最左前缀匹配原则, 遇到范围查询停止
5. 尽量选择区分度高的列作为索引

### ip查找城市设计

1. 根据ip段分组
2. 二分查找