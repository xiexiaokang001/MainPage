# MainPage

一个实用的字符转换工具集，基于 Django 框架开发。

## 📋 项目结构

```
MainPage/
├── MainPage/                 # Django 项目配置目录
│   ├── MainPage/            # 项目核心配置
│   │   ├── __init__.py
│   │   ├── settings.py      # 项目设置
│   │   ├── urls.py          # 根 URL 配置
│   │   └── wsgi.py          # WSGI 入口
│   ├── ascii/               # ASCII 转换应用
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── form.py          # 表单定义
│   │   ├── models.py        # 数据模型
│   │   ├── urls.py          # ASCII 应用路由
│   │   └── views.py         # 视图逻辑
│   ├── index/               # 首页应用
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py         # 首页视图
│   └── templates/           # HTML 模板
│       ├── homepage.html       # 首页
│       ├── ascii_to_char.html # ASCII → 字符串
│       ├── char_to_ascii.html # 字符串 → ASCII
│       └── string_reverse.html # 字符串反转
├── manage.py                # Django 管理脚本
└── README.md                # 项目说明
```

## 🚀 功能特性

1. **ASCII 转字符串**
   - 输入：十六进制 ASCII 码（空格分隔），如 `41 42 43`
   - 输出：对应字符串，如 `ABC`

2. **字符串转 ASCII**
   - 输入：任意字符串，如 `Hello`
   - 输出：十六进制 ASCII 码（空格分隔），如 `48 65 6c 6c 6f`

3. **字符串反转**
   - 输入：任意字符串，如 `Hello`
   - 输出：反转后的字符串，如 `olleH`

4. **智能主题切换**
   - 自动检测时间，7:00-19:00 使用浅色主题
   - 其他时间使用深色主题
   - 响应式设计，适配各种设备

5. **转换结果对比**
   - 实时显示转换前后的数据
   - 方便对比和验证转换结果

##栈

- ** 🛠 技术后端框架**：Django 4.2
- **前端技术**：原生 HTML/CSS/JavaScript
- **视图模式**：Django Class-Based Views (CBV)
- **响应式设计**：CSS Grid + Flexbox
- **主题系统**：CSS Variables + JavaScript 时间检测

## 📦 安装与运行

### 1. 安装依赖
```bash
pip install Django==4.2.*
```

### 2. 启动服务器
```bash
python manage.py runserver
```

### 3. 访问应用
打开浏览器访问：`http://127.0.0.1:8000/`

## 🎯 路由结构

| 路由 | 功能 | 视图类 |
|------|------|--------|
| `/` | 首页 | `index` |
| `/ascii/plus` | ASCII 转字符串 | `AsciiViewPlus` |
| `/ascii/minus` | 字符串转 ASCII | `AsciiViewMinus` |
| `/ascii/reverse` | 字符串反转 | `AsciiViewReverse` |

## 💻 核心代码说明

### 视图层 (views.py)
- 使用 Django `View` 类实现 RESTful 风格的 HTTP 处理
- `GET` 请求：渲染表单页面
- `POST` 请求：处理表单数据并返回结果

### 表单层 (form.py)
- `AsciiFrom`：统一的输入表单，包含一个 `CharField` 字段

### 模板层
- 每个功能页面都包含表单区域和结果对比区域
- 使用 CSS Variables 实现主题切换
- 内联 CSS 保证零外部依赖

## 🎨 界面特性

- **深色/浅色主题自动切换**
- **卡片式布局**
- **响应式设计**（适配移动端和桌面端）
- **转换前后数据对比展示**
- **流畅的动画过渡效果**

## 📝 后续优化方向

1. 添加用户历史记录功能
2. 支持批量文件导入/导出
3. 添加更多字符编码支持（UTF-8、GBK 等）
4. 添加单元测试
5. 支持 API 接口调用

## 📄 许可证

MIT License
