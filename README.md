# proxy_pool
代理池

## 介绍
此代理池的搭建参考了[崔庆才](https://cuiqingcai.com/)大大的新书<Python3 网络爬虫开发实战>，搭建了一个比较高效的代理池，
代理池的资源来源于[西刺代理](http://www.xicidaili.com/)和[66ip](http://www.66ip.cn/)，后续会添加其它其它免费代理网站，
在此感谢崔大大的教程和各大免费代理网站提供的代理。

## 第三方库
<br> pip install requests </br>
<br> pip install aiohttp </br>
<br> pip install beautifulsoup4 </br>
<br> pip install redis </br>
<br> pip install flask </br>
<br> pip install aiohttp </br>
<br> 本次数据库存储使用非关系型数据库redis，需要下载安装，官网地址：https://redis.io </br>

## 使用介绍
<br>提供了两种调用方式：</br>
<br>1、url调用：导入proxy模块，调用start_pps()方法运行代理池，然后访问"http://127.0.0.1:5000/random"  来调用随机代理</br>
<br>2、数据库调用：导入proxy模块，调用get_proxy_from_db()方法来获取随机代理

## 框架介绍
<br>代理池主要包含五个模块，分别为生成器模块、测试器模块、接口模块、存储模块和调度模块：</br>
<br>生成器模块：从各大免费代理网站获取代理保存到数据库，并初始化每个代理的分数为10</br>
<br>测试器模块：从数据库调出代理进行测试，并对其进行评分；若有效，则分数置为100，若无效，则分数减1，小于0时认为此代理无效，删除此代理</br>
<br>接口模块：使用flask库对存储进行封装，提供可通过url访问的接口</br>
<br>存储模块：对redis数据库的增删查改功能进行封装，提供可供其它模块调用的API</br>
<br>调度模块：对生成器、测试器和接口进行合理调度，使代理池能够协调、高效的运行

## 运行效果
<br> 生成器运行效果： </br>
<br>  </br>
![生成器运行图片加载失败！！！](https://github.com/ZZShi/proxy_pool/blob/master/result/getter.png)
<br>  </br>

<br> 测试器运行效果： </br>
<br>  </br>
![测试器运行图片加载失败！！！](https://github.com/ZZShi/proxy_pool/blob/master/result/tester1.png)
<br>  </br>
![测试器运行图片加载失败！！！](https://github.com/ZZShi/proxy_pool/blob/master/result/tester2.png)
<br>  </br>

<br> 接口运行效果： </br>
<br>  </br>
![接口运行图片加载失败！！！](https://github.com/ZZShi/proxy_pool/blob/master/result/api1.png)
<br>  </br>
![接口运行图片加载失败！！！](https://github.com/ZZShi/proxy_pool/blob/master/result/api2.png)
<br>  </br>

<br> 调度后运行效果： </br>
<br>  </br>
![调度运行图片加载失败！！！](https://github.com/ZZShi/proxy_pool/blob/master/result/pps_running.png)
<br>  </br>
