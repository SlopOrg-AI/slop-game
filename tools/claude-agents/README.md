# Claude Code subagent definitions — copy to `.claude/agents/`

Remote tooling cannot write into `.claude/`. Owner, once:

```
cd C:\Claude\shinobi-v2
mkdir .claude\agents
copy tools\claude-agents\*.md .claude\agents\
del .claude\agents\README.md
```

Claude Code is the **tech** lead in this repo (D5.29): the work, the repo, git, housekeeping. Name another lead ("act as systems") to switch. There is no `admin` pointer — that role retired into Chief of Staff (Cowork, no Claude Code pointer by design) and Tech.

```
```

Then in Claude Code: `/agents` lists them; "use the systems agent to …" dispatches one. Each file is a thin pointer to `leads/<lead>.md` — edit the brief, not the pointer. Tech sub-lead owns this folder.
