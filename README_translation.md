# 药品注册管理办法 - Weblate 翻译指南

## 📋 项目说明

本项目用于翻译《药品注册管理办法》全文，使用 Weblate 进行协作翻译管理。

## 📁 文件结构

```
.
├── 药品注册管理办法.md          # 原始中文文档
├── drug_registration.pot         # 翻译模板文件（自动生成）
├── drug_registration_en.po       # 英文翻译文件
├── drug_registration_zh_CN.po    # 简体中文源文件（可选）
├── convert_md_to_po.py          # Markdown 转 PO 格式的转换脚本
└── README_translation.md         # 本说明文件
```

## 🚀 快速开始

### 方法一：使用转换脚本（推荐）

1. **运行转换脚本**
   ```bash
   python3 convert_md_to_po.py
   ```
   这会自动将 `药品注册管理办法.md` 转换为 PO 格式的翻译文件。

2. **初始化 Git 仓库**
   ```bash
   git init
   git add drug_registration.pot drug_registration_en.po
   git commit -m "Add drug registration translation files"
   ```

### 方法二：手动创建翻译条目

如果文档很长，建议按章节分割成多个 PO 文件，便于管理。

## 🔧 Weblate 配置步骤

### 1. 创建项目
- 登录 Weblate
- 点击 **"Add new project"**
- 填写：
  - 项目名称：`药品注册管理办法`
  - 项目标识符：`drug-registration`
  - 项目网站：（可选）

### 2. 添加组件
- 在项目中点击 **"Add new translation component"**
- 配置如下：

**基本信息：**
- 组件名称：`药品注册管理办法全文`
- 标识符：`full-text`

**版本控制：**
- 版本控制系统：`Git`
- 源代码仓库：填入你的 Git 仓库地址
- 仓库分支：`main` 或 `master`

**文件设置：**
- 文件格式：`Gettext PO file`
- 文件掩码：`drug_registration_*.po`
- 模板文件：`drug_registration.pot`
- 新翻译模板：`drug_registration.pot`
- 基础文件路径：留空或填 `/`

**语言设置：**
- 源语言：`Chinese (Simplified)` (zh_CN)
- 翻译语言：添加 `English` (en)、`Japanese` (ja) 等

### 3. 开始翻译

配置完成后：
1. Weblate 会自动扫描并加载所有翻译条目
2. 点击目标语言（如 English）
3. 逐条翻译每个段落
4. 使用 Weblate 的功能：
   - 💡 **翻译建议**：查看机器翻译和翻译记忆
   - 📝 **术语表**：添加专业术语（如"药品注册"、"临床试验"等）
   - ✅ **质量检查**：自动检测翻译问题
   - 💬 **评论功能**：与团队讨论翻译细节

## 📝 翻译注意事项

### 专业术语一致性
建议在 Weblate 中创建术语表，包含：

| 中文 | English |
|------|---------|
| 药品注册 | Drug Registration |
| 药品监督管理部门 | Drug Regulatory Authority |
| 临床试验 | Clinical Trial |
| 上市许可 | Marketing Authorization |
| 申请人 | Applicant |
| 有效性 | Efficacy |
| 安全性 | Safety |
| 质量可控 | Quality Control |

### 法律文本翻译原则
1. **准确性优先**：法律条文必须准确传达原意
2. **保持格式**：保留条款编号和结构
3. **术语统一**：使用标准的法律和医药术语
4. **避免意译**：尽量直译，保持法律严谨性

## 🔄 工作流程

```
原始文档 (MD) 
    ↓
转换脚本 (Python)
    ↓
PO 翻译文件
    ↓
Git 仓库
    ↓
Weblate 平台
    ↓
协作翻译
    ↓
自动提交到 Git
    ↓
导出翻译结果
```

## 📤 导出翻译结果

翻译完成后，可以：

1. **从 Weblate 下载**
   - 在组件页面点击 **"Files"** → **"Download translation"**

2. **从 Git 仓库获取**
   ```bash
   git pull origin main
   ```

3. **转换回 Markdown**（可选）
   - 编写脚本将 PO 文件转换回 Markdown 格式
   - 或使用 `po2txt` 等工具

## 🛠️ 常用命令

```bash
# 检查 PO 文件语法
msgfmt -c drug_registration_en.po

# 更新 PO 文件（当模板更新时）
msgmerge -U drug_registration_en.po drug_registration.pot

# 统计翻译进度
msgfmt --statistics drug_registration_en.po
```

## 💡 提示

- 对于超长文档，建议按章节拆分成多个 PO 文件
- 定期备份翻译进度
- 使用 Weblate 的自动建议功能提高效率
- 建立审校流程确保翻译质量

## 📞 支持

如有问题，请联系项目管理员或查阅 [Weblate 官方文档](https://docs.weblate.org/)。
