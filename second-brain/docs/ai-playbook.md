# AI playbook — operating the second brain with Claude, ChatGPT & NotebookLM

## Which brain for which question

| Question shape | Use | Why |
|---|---|---|
| "What did I read/save about X?" | **claude.ai** + Readwise/Recall connectors | Live search over highlights and cards, no sync lag |
| "What do I *think* about X?" | **Claude Code on this repo** (or claude.ai reading GitHub) | Your evergreen notes are the answer, and they live here |
| "Turn my knowledge into a post / brief / playbook" | **Claude Code on this repo** | Drafts from `notes/` + prompts library, in-place, git-tracked |
| Librarian chores (triage, distill, tag hygiene) | **Claude Code on this repo** | Needs file write access + the rules in `CLAUDE.md` |
| Deep synthesis across 10–50 specific sources, with citations | **NotebookLM** | Grounded strictly in uploaded sources; audio overview for drives |
| Broad/current web research, second opinion on a draft | **ChatGPT** (deep research) | Different model, different blind spots — useful disagreement |
| "Where does project X stand?" | **Notion** (or its connector from either AI) | Operational truth lives there |

## Claude (primary)

**1. claude.ai connectors** — Readwise, Recall, and Notion are already
connected. Retrieval etiquette: name the tool in the ask ("search my Readwise
highlights for…", "check my Recall cards on…") — it routes better than "search
my stuff".

**2. Claude Code on this repo** — the vault's hands. It loads `CLAUDE.md`
automatically and knows the conventions. The standing jobs:

- *"Run the weekly review"* → follows `resources/prompts/weekly-review.md`
- *"Process the inbox"* → triages `inbox/` to zero, shows what went where
- *"Distill <source> into notes"* → 1–3 seed evergreen notes, linked into MOCs
- *"Draft a LinkedIn post from <note>"* → `resources/prompts/note-to-linkedin-post.md`
- *"Sync my Readwise"* → runs the script (needs `READWISE_TOKEN` in env)

Works from the terminal, claude.ai/code, or the mobile app — same repo, same
rules, so sessions are interchangeable.

**3. Claude Projects** <a id="claude-projects"></a> — for stable contexts that
shouldn't re-derive the basics every chat. Create one project per ongoing
context, seed its knowledge with vault files, refresh monthly:

- **"Actionable AI — content"**: `notes/mocs/moc-content-engine.md`, your top
  content notes, voice/style notes.
- **"AI for small law firms"**: `notes/mocs/moc-ai-for-small-law-firms.md` +
  the evergreen notes it links.

## ChatGPT (second opinion)

**Setup (one-time):** ChatGPT → Settings → Connectors → **GitHub** → authorize
→ select `gyates45/curated`. Deep research and chat can then read the vault
directly. (The repo is public, so pasting a file's GitHub URL into any chat
also works with zero setup.)

**No Readwise/Recall connectors exist for ChatGPT — the vault *is* the
bridge.** Whatever matters got distilled into `notes/`, which ChatGPT can
read. This is a feature: ChatGPT sees your conclusions, not 34k raw
highlights.

**Custom GPT (optional):** build "Greg's Second Brain" with the instructions
in [`resources/prompts/chatgpt-second-brain-gpt.md`](../resources/prompts/chatgpt-second-brain-gpt.md);
point it at the GitHub connector or upload the `second-brain/` folder as
knowledge (refresh quarterly).

**Best uses:** deep research runs to *feed* the vault (output lands in
`inbox/` for triage — it enters `notes/` only after distillation); red-teaming
a draft ("argue against this post"); second opinion on a playbook outline.

## NotebookLM (per-project research workbench)

Use when one question deserves many sources: workshop prep, a playbook
chapter, a market-state question. Not a permanent store — notebooks are
scaffolding.

1. Create a notebook named for the question, not the topic
   (*"What actually blocks AI adoption in <50-lawyer firms?"*).
2. Load sources: PDFs, article URLs, YouTube links, plus relevant vault notes
   (paste or upload the `.md` files — they're small on purpose).
3. Interrogate: contradictions between sources, strongest counter-evidence,
   what's missing. Generate the audio overview for drive-time.
4. **Distill back or it didn't happen:** conclusions → evergreen notes via
   [`resources/prompts/notebooklm-project-kit.md`](../resources/prompts/notebooklm-project-kit.md).
   Then the notebook can die; the knowledge survived.

## Etiquette (all AIs)

- AI drafts, Greg decides. Nothing publishes, and no note reaches
  `status: evergreen`, without human eyes.
- Ask AIs to **cite vault paths** in anything they draft from your notes —
  provenance stays visible and checkable.
- When two AIs disagree, that's signal: capture the disagreement in `inbox/`;
  it's usually a post idea.
