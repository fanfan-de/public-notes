---
title: 公开知识笔记
tags:
  - index
---

# 公开知识笔记

记录可以公开分享的知识、阅读、实践和思考。AI 与 Agent 是主要专题，也欢迎其他技术、科学、人文和方法论内容。

这里不记录个人隐私和生活：日记、行程、健康与财务、私人联系方式、私人对话，以及未经允许公开的工作或他人资料，都应放在另一个独立笔记库。

## 从这里开始

| 入口 | 用途 |
| --- | --- |
| [公开选题](00-Inbox/README.md) | 收集已经适合公开的选题和简短想法 |
| [主题目录](10-Topics/README.md) | 按主题积累知识，可随内容增加目录 |
| [AI](10-Topics/AI/README.md) | 模型、检索、推理、评估等主要专题 |
| [Agent](10-Topics/Agents/README.md) | 工具、上下文、记忆、协议与工作流 |
| [实践记录](20-Practice/README.md) | 可以公开复现的实验、操作和结果 |
| [阅读笔记](30-Reading/README.md) | 论文、文章、书籍和公开资料的阅读记录 |
| [笔记模板](90-Templates/README.md) | 概念、实践、阅读三类模板 |
| [附件约定](assets/README.md) | 小图片与轻量附件的使用方式 |

## 写作约定

- 一篇笔记围绕一个主题，用清楚的文件名；不要为了分类提前建立大量空目录。
- 明确区分来源中的事实、自己的判断和有待验证的想法，引用附上原始链接。
- 以 Markdown 为主，内部使用相对 Markdown 链接，方便在 Obsidian 和 GitHub 中阅读；示意图优先用 Mermaid。
- Inbox、模板和标为待完善的内容也会公开。私密草稿从一开始就应放在独立的私人笔记库。
- AI 可以协助整理、检索和编辑，但不要把生成的结论当作自己的亲身经历或已经验证的事实。

## 本机使用

这个目录本身就是 Obsidian 笔记库。首次克隆后，在 Obsidian 中选择“打开本地仓库”，然后选择克隆目录。

`.obsidian/` 保留在本机，不参与 Git 同步，避免把窗口状态、插件配置或本地路径上传。笔记、模板和小附件通过 Git 同步。

首次使用当前克隆时运行：

```bash
python3 scripts/setup.py
```

它会安装带校验的固定版本 Gitleaks，并启用本仓库的提交和推送检查。需要 Python 3、Git 和网络；自动安装支持 Linux 与 macOS。

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
