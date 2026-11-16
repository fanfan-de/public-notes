---
title: 公开知识笔记
tags:
  - index
---

# 公开知识笔记

记录可以公开分享的知识、阅读、实践和思考。AI 与 Agent 是主要专题，也欢迎其他技术、科学、人文和方法论内容。

这里不记录个人隐私和生活：日记、行程、健康与财务、私人联系方式、私人对话，以及未经允许公开的工作或他人资料，都应放在另一个独立笔记库。

## 从这里开始

| 分类 | 用途 |
| --- | --- |
| [AI](AI/README.md) | 模型、检索、推理、评估等主要专题 |
| [Agent](Agent/README.md) | 工具、上下文、记忆、协议与工作流 |
| [Anybox](Anybox/README.md) | Anybox 项目的产品、架构、设计决策、实现、部署与验证记录 |
| [实践](实践/README.md) | 可以公开复现的实验、操作和结果 |
| [阅读](阅读/README.md) | 论文、文章、书籍和公开资料的阅读记录 |
| [收集](收集/README.md) | 已经适合公开的选题和简短想法 |
| [模板](模板/README.md) | 概念、实践、阅读三类模板 |
| [附件](assets/README.md) | 小图片与轻量附件的使用方式 |

所有内容分类直接放在根目录。新增主题也直接建立同级目录，普通笔记保持“分类/笔记.md”的结构；细分主题优先使用标签和链接。

## 写作约定

- 一篇笔记围绕一个主题，用清楚的文件名，直接放在根目录下对应的分类中；不要为了分类提前建立大量空目录。
- 明确区分来源中的事实、自己的判断和有待验证的想法，引用附上原始链接。
- 以 Markdown 为主，内部使用相对 Markdown 链接，方便在 Obsidian 和 GitHub 中阅读；示意图优先用 Mermaid。
- 收集、模板和标为待完善的内容也会公开。私密草稿从一开始就应放在独立的私人笔记库。
- AI 可以协助整理、检索和编辑，但不要把生成的结论当作自己的亲身经历或已经验证的事实。

## 本机使用

这个目录本身就是 Obsidian 笔记库。首次克隆后，在 Obsidian 中选择“打开本地仓库”，然后选择克隆目录。

`.obsidian/` 保留在本机，不参与 Git 同步，避免把窗口状态、插件配置或本地路径上传。笔记、模板和小附件通过 Git 同步。

首次使用当前克隆时运行：

```bash
python3 scripts/setup.py
```

它会安装带校验的固定版本 Gitleaks、启用本仓库的提交和推送检查，并注册跨项目使用的 `$save-public-note`。需要 Python 3、Git 和网络；自动安装支持 Linux 与 macOS。

## Agent Skills 随仓库同步

仓库内置四个官方 Skills 和一个自定义保存入口，完整文件保存在 `.agents/skills/`：

| Skill | 用途 |
| --- | --- |
| `save-public-note` | 从任意项目整理指定内容并保存到本笔记库 |
| `obsidian-cli` | 读取、检索、创建和管理笔记，以及控制 Obsidian |
| `obsidian-markdown` | Markdown、属性、链接、提示块等笔记格式 |
| `obsidian-bases` | Bases 数据视图 |
| `json-canvas` | Canvas 画布 |

在另一台电脑克隆仓库后，用 Codex 打开这个仓库目录，就会自动发现项目中的 Skills。按任务需要加载，也可以明确指定 `$obsidian-cli` 等名称。更新不会立即显示时，重启 Codex。其他 agent 的自动发现规则可能不同。

Skills 提供操作知识，不会自动安装应用。新电脑仍需安装 Obsidian，把克隆目录作为笔记库打开；若要控制应用，在 Obsidian 设置中开启并注册官方 CLI，并保持应用运行。只有 Markdown 文件读写时，可以直接使用 agent 的文件工具。

运行 `python3 scripts/setup.py` 后，也可以在其他项目中调用 `$save-public-note`。脚本在本机用户 Skills 目录创建指向仓库内保存入口的软链接；入口通过自身真实位置找到笔记库，不依赖当前项目，也不把本机路径写进 Git。仓库内的 Skill 文件本身是实际文件，可随 Git 同步。

例如，在任意项目中说：

> 使用 $save-public-note，把这次讨论中适合公开的知识整理成一篇笔记。

> 使用 $save-public-note，总结这篇文章并保存到阅读分类，然后同步到 GitHub。

默认调用只保存本地笔记；用户要求提交、同步或发布时，再检查并执行相应 Git 操作。换电脑后运行同一个 setup 命令即可注册全局入口；移动或删除克隆目录后，需在保留的克隆中重新运行 setup 修复入口。

项目内 Skills 的自动发现不依赖 setup。只需提交检查、不需全局入口时，可运行 `python3 scripts/setup.py --checks-only`。来源和版本见 [Skills 说明](.agents/skills/README.md) 及 [skills-lock.json](skills-lock.json)。

## 通过 GitHub 同步

远程仓库：[fanfan-de/public-notes](https://github.com/fanfan-de/public-notes)。

开始编辑前先同步：

```bash
git pull --ff-only
```

编辑完成后，明确选择本次要发布的文件，检查内容再提交：

```bash
git status --short
git add 具体文件或目录
git diff --cached
python3 scripts/check.py
git commit -m "docs(notes): add a public knowledge note"
git pull --rebase
git push
```

另一个电脑首次使用：

```bash
git clone https://github.com/fanfan-de/public-notes.git
cd public-notes
python3 scripts/setup.py
```

建议 Git 提交身份使用 GitHub 的 noreply 邮箱。若同步出现冲突，先解决并复查，不使用强制推送覆盖另一台电脑的修改。

## 公开内容与文件检查

- 本地提交检查整个暂存区，拒绝常见私密文件路径、密钥文件、日志、压缩包和不支持的二进制附件。
- 所有单个文件上限为 **1 MiB**；图片建议控制在 **300 KiB** 内，较大的图、PDF 和音视频使用公开来源链接。
- Gitleaks 检查常见密钥，并增加邮箱、本机用户目录、带标签手机号和身份证号的规则；示例邮箱使用 `example.com`。
- 推送前扫描本地 Git 历史；GitHub Actions 在推送和 PR 后再次执行检查。云端检查发生在上传之后，不能替代本地检查。
- 自动检查无法识别截图和自然语言里的所有隐私，发布前仍需查看差异；忽略规则也不会移除已经提交的内容。

本仓库使用手动检查后提交和推送的方式。可以让 agent 执行这些步骤，暂不配置后台自动提交或推送。
