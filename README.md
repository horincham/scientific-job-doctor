# Scientific Job Doctor

A Codex skill for diagnosing Gaussian quantum chemistry jobs and checking whether the results support the intended calculation.

[中文说明](README.zh-CN.md) · [Skill](skills/scientific-job-doctor/SKILL.md) · [Gaussian manual notes](skills/scientific-job-doctor/references/gaussian-manual.md) · [Examples](examples/README.md)

## What it does

Give Codex a Gaussian input, log, or calculation directory and state the scientific objective. The skill identifies the relevant job and calculation stage, explains what the available evidence supports, and suggests the next check or a candidate restart. It cites the job files and the corresponding technical references. The workflow reads local artifacts and presents proposed changes for review.

The reference library covers input and checkpoint handling, SCF and wavefunction stability, correlation and composite methods, basis sets and ECPs, optimizations, scans, TS and IRC, thermochemistry, solvation and BSSE, excited states and spectroscopy, CASSCF, ONIOM, properties, and dynamics. Slurm output can help distinguish a scheduler interruption from a Gaussian failure.

## Install for Codex

Copy [`skills/scientific-job-doctor`](skills/scientific-job-doctor) into `~/.agents/skills/` for personal use, or into `.agents/skills/` inside a project. On Windows, the personal path starts at `%USERPROFILE%\.agents\skills\`. Keep `SKILL.md` and the `references/` directory together. The skill has no Python dependency. [Codex installation locations](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)

In Codex, invoke the skill and provide a path and a goal.

```text
$scientific-job-doctor Diagnose the Gaussian job in ./job_042.
I need the thermochemistry of the optimized radical. Cite the decisive
log lines, check which calculation stages finished, and suggest the next check.
```

## Sources and validation

The [manual notes](skills/scientific-job-doctor/references/gaussian-manual.md) paraphrase Gaussian keyword documentation and tie each behavior to a diagnostic decision. The [source index](skills/scientific-job-doctor/references/sources.md) links first-party documentation, original research, and 16 Computational Chemistry Commune discussions. Forum cases are used within their stated context. [AI Computational Chemist](https://github.com/JCLiuGroup/AI-Computational-Chemist) informed the repository organization.

The repository includes synthetic [diagnostic examples](examples/README.md) and a structural check that runs locally with `python -m unittest discover -s tests -v`. Case review is qualitative and depends on the supplied evidence. Gaussian revision-specific behavior should be checked against the installed revision and its documentation.

## Contributing and citing

See [CONTRIBUTING.md](CONTRIBUTING.md) for source and example requirements and [CITATION.cff](CITATION.cff) for citation metadata. Original repository content is available under the [MIT License](LICENSE). Linked third-party materials retain their own terms.
