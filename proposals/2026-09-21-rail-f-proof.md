# Rail F proof — deliberate failure, do not merge

This branch exists to make rail F fail in real CI. The commit adding this file is
authored to the owner while the pull request is opened by the machine account, which
is exactly the condition rail F refuses.

A passing check only proves the workflow ran. If this pull request goes green, rail F
is not enforcing anything — most likely `GITHUB_EVENT_PATH` was not readable and
`pr_author()` returned `None`, which returns 0 and looks identical to success.

Closed and deleted once observed.
