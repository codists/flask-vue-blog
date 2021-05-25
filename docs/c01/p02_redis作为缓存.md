# redis作为缓存
## 问题

- 为什么要缓存（why）
  - 减少页面加载时间，大概减少 20-50 ms

- 存什么(how)
  - 将请求和请求的结果作为键值对进行存储。

- 哪些页面应该进行缓存/哪些页面不应该缓存
  - 实时数据不应该缓存：如商品数量

- 用 Redis 的哪种数据类型进行存储
  - 使用字符串进行存储，SETEX 命令。

- 缓存失效时间

  - 5分钟

- 如果不能缓存怎么办？

  设置回调函数。

## 原生 Redis 实现

## 中间件/插件
1、Flask-Caching



## 参考资料

[1] Flask-Caching: https://flask-caching.readthedocs.io/en/latest/

