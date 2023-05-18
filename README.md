
<div style="text-align: center">
<h1>python-microservice-framework</h1>
</div>


**中文** | [English](./README.en-US.md)

## 简介

python的微服务框架，我会完善它，但我并不确定这是否是正确的想法，采用`fastapi`,`consul`,`pyjwt`等主流技术搭建。

## 特性

- **微服务架构**: fastapi、consul、pyjwt、nginx、docker、restful
- **服务调用**: 基于rest接口封装服务调用工具
- **接口约束**: 应遵循项目严格的接口约束，方便使用和管理
- **接口认证**: 使用pyjwt生成token，Depends嵌入路由实现全局认证(待完善，token存数据库)
- **异常处理**: `预留`
- **规范的数据库操作**: 任何crud操作应基于CRUD_BASE实现

## 准备

- [Python3.x](https://www.python.org/downloads/) 和 [git](https://git-scm.com/) 开发环境
- [FastApi](https://fastapi.tiangolo.com/zh/) - 熟悉相关路由编写
- [Pyjwt](https://pyjwt.readthedocs.io/en/stable/) - 熟悉相关api
- [Mongodb](https://www.mongodb.com/docs/) - 熟悉mongodb数据库的基本操作
- [Consul](https://yushuai-w.gitbook.io/consul/) - 了解即可

## 安装使用

- 获取项目代码

```bash
git clone https://github.com/longyi-xw/python-microservice-framework.git
```

- 安装依赖

```bash
make preinstall

make install
```
或者
```bash
pip install -r requirements.txt
```

- 运行服务

到service下面的某个服务 main.py 执行它

## 项目结构

```
python-microservice-framework/
├── _types                                  # 类型文件
│   ├── service.py                          
│   └── __init__.py
├── config                                  # 配置目录
│   ├── settings.py                         # 项目配置
├── core                                    
│   ├── security.py                         # 安全认证
│   ├── consul.py                           # 服务注册中心
│   ├── algorithm_library                   # 算法库
│   └── __init__.py
├── db
│   ├── mongo.py                            # 数据库配置
│   ├── crud_base.py                        # crud基础封装
│   └── __init__.py
├── decorator
│   ├── singleton.py                        # 单例装饰器
│   └── __init__.py
├── enums                                   # 公共枚举
│   ├── service_verify.py
│   ├── service_api.py                      # 服务接口约束，新增接口前应该先考虑它
│   ├── service.py                          # 服务配置，服务的地址，端口等
├── services
│   ├── data_analysis                       # 数据服务
│   │   ├── models                          # 模型类
│       ├── crud                            # 模型的crud单独封装
│   │   ├── main.py                         # 服务启动入口
│   │   ├── api                             # 接口
│   └── business
│       ├── models
│       ├── main.py
│       ├── crud
│       ├── api
├── tests                                   # 测试
│   └── test_main.http
├── utils                                   # 工具库
│   ├── service_invoke.py
├── requirements.txt                        # 依赖文件
├── setup.py                                # 可能的启动脚本
├── README.md                               
├── README.en-US.md
├── Makefile                                # 编译步骤
└── Dockerfile                              # 部署文件
```

## 部署