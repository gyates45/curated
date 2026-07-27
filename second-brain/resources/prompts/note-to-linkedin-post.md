# Evergreen note → LinkedIn post

**Run in:** Claude Code on this repo (it can read the note and the MOC context).
The `linkedin-post-drafter` skill handles voice and hook mechanics — this
prompt feeds it the right raw material.

---

Draft a LinkedIn post from this evergreen note: `<path to note>`.

Before drafting:
1. Read the note, its `sources:`, and the MOC(s) that link it — pull one
   supporting detail or example from a related note if it strengthens the post.
2. Audience: small law firm partners and solo attorneys (practical,
   skeptical of hype, time-poor). Angle the claim at a decision they face.

Then run the standard drafting flow (hooks → I pick → full draft). Constraints:
- The post argues the note's claim — don't water it down to a listicle.
- Include the note's "so what" as the payoff.
- No client names or engagement specifics, ever.
- End by telling me which vault notes you drew on (paths), so provenance is
  on record.

If the note is too thin to carry a post, say so and tell me what's missing —
that gap goes back into the note.
