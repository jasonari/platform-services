# platform-services

基于 FastAPI 的 Web 后端服务。

## 本地开发

在仓库根目录执行：

```powershell
uv sync --locked
uv run uvicorn main:app --app-dir src --reload
```

- 健康检查：<http://127.0.0.1:8000/health>，返回 `{"status":"ok"}`，仅表示应用可响应请求。
- API 文档：<http://127.0.0.1:8000/docs>。

## 配置

默认配置即可启动。如需调整，将 `.env.example` 复制为仓库根目录下的 `.env`，或设置环境变量。环境变量优先于 `.env`。

| 变量 | 默认值 | 用途 |
| --- | --- | --- |
| `APP_NAME` | `platform-services` | API 文档中的应用名称 |
| `LOG_LEVEL` | `INFO` | 应用日志级别，支持 `DEBUG`、`INFO`、`WARNING`、`ERROR`、`CRITICAL` |

Uvicorn 自身的日志级别通过启动参数 `--log-level` 设置。

## 目录

```text
src/
├── main.py                       # 应用入口、日志初始化及路由注册
└── platform_services/
    ├── config.py                 # 环境配置
    └── api/
        └── health.py             # 健康检查接口
```
