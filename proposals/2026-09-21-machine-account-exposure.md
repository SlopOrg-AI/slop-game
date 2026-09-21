# Machine account exposure — three findings, deferred by the owner

**Status:** PROPOSED · raised by `builder-260921-c`, 2026-09-21. Owner: *"i think we can
address later. priority right now is merging #8."* Recorded here rather than in `queue/`
because none of it blocks work today — `D260921.2-P`: non-blocking questions are proposals.

Nothing here is urgent. All three are cheap to fix and get more expensive to discover late.

## 1. The machine account's real email is in public history, permanently

`a6d5625`, the merge commit for PR #7, is authored to **`sloporg.ai@gmail.com`** — the
account's actual Gmail, not its no-reply address.

Cause, with evidence rather than inference: the owner's merge commits carry
`51842005+chris-egan@users.noreply.github.com`, so **he** has *"Keep my email addresses
private"* enabled and `sloporgAI` does not. GitHub falls back to an account's primary
address for merge commits made through the API.

**Why it is worth more than a shrug.** That mailbox is the account-recovery path for
`sloporgAI`. Every constraint on that identity is downstream of who controls its mail — a
password reset from that inbox takes the account regardless of token scopes, `CODEOWNERS`,
or the ruleset. Publishing the address in a public repo hands anyone looking the exact
target.

**It cannot be undone.** Removing it means rewriting `main`, which `PROTOCOL.md` §3 forbids
and which would break every clone. The address is public; only the recurrence is fixable.

**Fix (owner, 2 min):** as `sloporgAI`, <https://github.com/settings/emails> → *Keep my email
addresses private*, and *Block command line pushes that expose my email*. Future merge
commits then use the no-reply form that agent commits already use.

## 2. Neither account has two-factor authentication

Observed as org admin: `orgs/SlopOrg-AI/members?filter=2fa_disabled` returns
`["chris-egan", "sloporgAI"]`. The org's own `two_factor_requirement_enabled` is `false`.

On its own, ordinary. Combined with finding 1 it is not: a published recovery address **and**
no second factor is weaker than either alone, and `chris-egan` is org admin — the account
that can delete ruleset `23775959`.

**Fix (owner):** 2FA on both, `chris-egan` first. Requiring it org-wide is a further step and
would want checking against the free plan before relying on it.

## 3. The merge classifier is not a control, and should not be described as one

Claude Code's own guard rail refused `gh pr merge` **twice** today and allowed it **four**
times. No approving review existed in any of the four it allowed — including PR #8, which
merged with `reviews: NONE`.

An earlier working hypothesis, that a genuine approving review is what clears it, is
therefore **not supported**: unreviewed merges pass anyway. The behaviour is inconsistent on
inputs this session could not distinguish.

**Consequence.** Enforcement cannot rest on the harness. The only real gate is GitHub's
`required_approving_review_count`, which is `0` today — so **review is currently a
convention, not a control**, and the framework should say so plainly until that changes.
`D260921.4-P` (a) called for exactly this: fall back and state it plainly if the loop is not
smooth. Setting it to `1` is now safe, since `D260921.5-P` means the owner authors no pull
requests.

## Recommendation

Do 1 and 2 when convenient; they are minutes each. Do 3 — set
`required_approving_review_count: 1` — before making any claim, in `PROTOCOL.md` or
elsewhere, that independent review is enforced here. Right now it is not.
