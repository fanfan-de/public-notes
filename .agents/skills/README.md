# 随仓库分发的 Agent Skills

这些 Skills 原样来自 [Obsidian 官方仓库](https://github.com/obsidianmd/obsidian-skills)，固定到提交 `398127736bd4ba42d767b1419fee1a927508370b`。上游文件保持原样，附带完整参考资料；本仓库约定在根目录的 [AGENTS.md](../../AGENTS.md) 中维护。

| Skill | 用途 |
| --- | --- |
| [obsidian-cli](obsidian-cli/SKILL.md) | 通过官方 CLI 操作笔记库 |
| [obsidian-markdown](obsidian-markdown/SKILL.md) | 编写 Obsidian Markdown、属性、引用与链接 |
| [obsidian-bases](obsidian-bases/SKILL.md) | 编写 Bases 数据视图 |
| [json-canvas](json-canvas/SKILL.md) | 编写 Canvas 画布 |

来源、版本和逐文件 SHA-256 保存在 [skills-lock.json](../../skills-lock.json) 中。更新时一并更新内容、锁定记录和许可证，重新运行仓库检查。

这四个上游 Skills 的许可见 [LICENSE](LICENSE)。该许可证仅覆盖这些第三方文件，不替本仓库的原创笔记指定许可。

Codex 在当前仓库中自动发现 `.agents/skills/`。Skills 文件会随 Git 克隆和拉取同步；运行所需的 Obsidian 应用、CLI、Python 和 Git 仍需在新电脑上安装或启用。
