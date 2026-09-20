# Claude Code subagent definitions — copy to `.claude/agents/`

Remote tooling cannot write into `.claude/`. Owner, once:

```
cd C:\Claude\shinobi-v2
mkdir .claude\agents
copy tools\claude-agents\*.md .claude\agents\
del .claude\agents\README.md
```

Then in Claude Code: `/agents` lists them; "use the systems agent to …" dispatches one. Each file is a thin pointer to `leads/<lead>.md` — edit the brief, not the pointer. Engine sub-lead owns this folder.
