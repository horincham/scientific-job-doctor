# Synthetic diagnostic examples

These excerpts are constructed for review and can be pasted directly into a Codex prompt with `$scientific-job-doctor`.

## A frequency stage times out

> I need thermochemistry for a radical. `job.log:110` shows `Optimization completed`. Line 160 shows `Normal termination`. At line 162 a new Link1 step begins with a `Freq Geom=AllCheck Guess=Read` route. Line 172 shows `SCF Done` and no frequencies follow. The matching Slurm job step has state `TIMEOUT`.

**Expected diagnosis.** Report the completed optimization and the timed-out frequency stage separately. Look for a complete, matching frequency block in the earlier stage. If needed, verify the checkpoint before proposing a frequency-only continuation.

## An excited state changes character

> An optimization with `TD=(NStates=3,Root=2)` converged. Initially S2 has A→B charge-transfer character. Near the end, S2 is localized on B while nearby S3 has the target A→B character. Can I use this geometry for CT emission?

**Expected diagnosis.** Confirm numerical optimization. The target CT minimum still needs verification. Ask for the root actually used for the gradient and compare NTOs, hole–electron distributions, or state overlaps along the path.

## An imaginary mode points to a different process

> For intermolecular H abstraction, my converged TS has a single frequency of −114 cm⁻¹, mainly methyl torsion. Can I report the barrier?

**Expected diagnosis.** The imaginary-mode count alone is insufficient. Check displacement along the two H-transfer distances. A validated H-abstraction barrier requires a matching reaction mode and appropriate endpoint evidence.

## SCF energy appears together with a convergence warning

> A Fe calculation uses `GenECP Geom=AllCheck Guess=Read`. Its last SCF step prints `SCF Done` and `Convergence criterion not met`. The source checkpoint and ECP definition have not been verified.

**Expected diagnosis.** The observed SCF did not meet its criterion. Verify the matching checkpoint, effective electron count and ECP/basis assignment before selecting an SCF retry.
