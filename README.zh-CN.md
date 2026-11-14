# Scientific Job Doctor

面向 Gaussian 计算化学作业的 Codex skill。输入一个计算目录、一份日志或输入文件，再说明你想得到的物理量或目标结构。Skill 会引用作业行号，给出运行状态、数值收敛、结果可用性及下一步排查建议。

[English](README.md) · [技能入口](skills/scientific-job-doctor/SKILL.md) · [官方手册提炼](skills/scientific-job-doctor/references/gaussian-manual.md) · [诊断示例](examples/README.md)

## 安装

下载或克隆仓库，把 [`skills/scientific-job-doctor`](skills/scientific-job-doctor) 整个目录复制到用户的 `~/.agents/skills/`，或某个项目的 `.agents/skills/`。Windows 用户目录为 `%USERPROFILE%\.agents\skills\`。在 Codex 里输入 `$scientific-job-doctor`，再给计算目录和目标。 [Codex 官方文档](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)

```text
$scientific-job-doctor 检查 ./job_042。我要用这个自由基的优化构型和频率做热化学，
请逐段判断哪些计算已经完成，引用具体日志行，并给出最有判别力的下一项检查。
```

## 覆盖范围与资料

支持输入、检查点和 Slurm 诊断，以及 Gaussian 单点、SCF 与波函数、基组/ECP、后 HF、复合方法、优化、扫描、TS/IRC、频率与热化学、溶剂、BSSE、激发态与光谱、CASSCF、ONIOM、性质和动力学等任务。读取本地作业资料，候选修改在诊断回复中展示。

仓库内的[手册提炼](skills/scientific-job-doctor/references/gaussian-manual.md)将关键词规则写成可追溯的判断条目。[来源索引](skills/scientific-job-doctor/references/sources.md)收录 Gaussian 厂商资料、原始方法资料及 16 篇计算化学公社讨论。示例使用合成输入和日志片段。目录结构参考 [AI Computational Chemist](https://github.com/JCLiuGroup/AI-Computational-Chemist)。

本地结构检查可运行 `python -m unittest discover -s tests -v`。贡献方式见 [CONTRIBUTING.md](CONTRIBUTING.md)，项目引用见 [CITATION.cff](CITATION.cff)。
