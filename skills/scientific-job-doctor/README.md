# Scientific Job Doctor · Gaussian

在 Codex 中审查 Gaussian 输入、诊断运行或收敛失败、检查计算结果，以及拟定续算或验证方案。参考资料可本地按需读取。

## 安装

解压 ZIP 后，把完整的 `scientific-job-doctor` 目录放入对应的 skill 目录。

| 使用范围 | 位置 |
| --- | --- |
| Windows 当前用户的所有项目 | `%USERPROFILE%\.agents\skills\scientific-job-doctor\` |
| 某个项目 | `<项目目录>\.agents\skills\scientific-job-doctor\` |
| macOS / Linux 当前用户 | `~/.agents/skills/scientific-job-doctor/` |

确认 `SKILL.md` 与 `references/` 位于该目录下。在 Codex 中用 `$scientific-job-doctor` 调用。如果选择器中暂未显示，重启 Codex 后再看。Skill 本身可在有本地文件读权限的 Codex 会话中工作。查看二进制检查点内容可能需要相应 Gaussian 工具或已导出的 `.fchk`。 [Codex Skill 官方文档](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)

## 用法

> $scientific-job-doctor 诊断这个 Gaussian 作业目录。目标是确认这个自由基的溶液相热化学数据是否可用。请定位失败阶段，引用日志行，并给出最省计算时间的验证方案。

> $scientific-job-doctor 审查当前 TDDFT 优化结果。目标是 A→B 电荷转移态的发射波长。请核对优化过程中态的身份、末端几何和溶剂响应。

可提供 `.gjf/.com`、`.log/.out`、提交脚本、stdout/stderr、已有 Slurm 摘要或 `.fchk`，以及所求物理量或目标结构。单份日志可以开始排查。运行按本地只读方式进行，候选修改在回复中展示。

## 覆盖

输入与运行、基组和赝势、SCF 和电子结构、各种优化与反应路径、振动与热化学、溶剂与结合、激发态和光谱，以及多参考、ONIOM、波函数分析、分子性质和动力学。少见或版本特定的关键词按官方资料逐项核实。 [诊断流程](SKILL.md) · [来源索引](references/sources.md)
