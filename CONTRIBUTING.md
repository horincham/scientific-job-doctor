# Contributing

- Start with a Gaussian task, a precise symptom, and the scientific decision the diagnosis should support.
- Route the task from `SKILL.md` only if the existing topics cannot handle it. Place domain guidance in the most relevant reference file and cite the Gaussian keyword page, technical note, original paper, or public case it depends on.
- Record the Gaussian revision and method when they affect keyword behavior. For community cases, describe the observed evidence and scope of the recommendation. Label missing inputs or outcomes.
- Contribute synthetic or explicitly redistributable examples. Include the question, observable evidence, expected diagnostic boundary, and one useful next check. Keep unpublished structures, log files with embedded identifiers, checkpoints, credentials, and attachments out of public contributions.
- Run `python -m unittest discover -s tests -v` before submitting. For changes to diagnostic judgments, include a representative prompt and the expected decision in the pull request.
