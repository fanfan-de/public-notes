# Public Notes

This is a public personal knowledge vault, published through GitHub. AI and agents are major topics, not a limit on subject matter. Other public knowledge, reading, experiments, and essays belong here too.

## Content boundary

- Treat every tracked file, collection item, template, and commit as public.
- Do not add personal life, diaries, schedules, health or financial details, private conversations, credentials, account exports, local machine paths, or unpublished workplace / third-party information.
- Do not migrate material from another vault or a private conversation without an explicit request identifying content that may be published. New topical notes may summarize public ideas without preserving private chat context.
- Never invent personal experiences, completed experiments, or opinions on the owner's behalf. Distinguish sourced facts, interpretation, and unverified ideas.
- Keep secrets out of Git history. Use obvious placeholders in examples. Do not bypass hooks, disable checks, or force-push to make a failed check disappear.

## Organization and writing

- Start from README.md. All content categories live directly at the vault root: AI/, Agent/, 实践/, 阅读/, 收集/, and 模板/. Add new topics as sibling root directories when real content needs them. Keep ordinary notes at category/note.md; use tags and links for finer organization instead of adding folder levels.
- Notes are primarily Chinese; retain conventional technical terms and names. Keep one main topic per note.
- Add a title and a small number of useful frontmatter tags. Record dates for time-sensitive observations.
- Use standard relative Markdown links so both GitHub and Obsidian can navigate them. Use original sources for factual claims and check current information when needed.
- Prefer Markdown and Mermaid. Put small images under assets/. Each tracked file must be at most 1 MiB; prefer images under 300 KiB. Link to large public material instead of copying it.
- Keep .obsidian/ settings local. Use Obsidian CLI move / rename when changing linked filenames so existing links can be updated. Target vault=public-notes explicitly.

## Bundled skills

- Four official Obsidian skills are committed under `.agents/skills/`: obsidian-cli, obsidian-markdown, obsidian-bases, and json-canvas. Load the relevant SKILL.md and its references when the task needs them.
- Codex discovers these as repository skills when working in this clone. They do not require a user-global installation or machine-specific symlinks.
- The writing conventions in this guide take precedence over generic examples in the bundled skills, including the use of relative Markdown links for GitHub compatibility.
- Keep upstream skill files unchanged. Record the source revision and file hashes in skills-lock.json, preserve the upstream license, and put repository-specific policy in this guide.
- Skills do not install applications. Reading / editing files needs file access; app commands also need Obsidian installed, its official CLI enabled, and the app running.

## Git and validation

- On each clone, run `python3 scripts/setup.py` to enable repository hooks and install Gitleaks.
- Before editing, use `git pull --ff-only` when the worktree is clean. Preserve existing user changes and resolve conflicts deliberately.
- Stage only intended files, inspect `git diff --cached`, and run `python3 scripts/check.py` before committing.
- Use concise commits such as `docs(notes): explain a topic`. Use the owner's GitHub noreply identity for commits made on the owner's behalf.
- After a commit, use `git pull --rebase` and `git push` when GitHub synchronization is requested. Resolve and recheck any conflicts; never force-push as a shortcut.
- Local hooks check before transfer; GitHub Actions is a second check after upload. Checks catch common patterns, not all private content, especially images.
