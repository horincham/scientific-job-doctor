# 输入与运行环境

## 输入结构、模型和续算

| 线索 | 取证与处理 |
| --- | --- |
| `QPErr`、`Unrecognized ...`、`End of file in ZSymb`、读取段落时报错 | 查看 route 回显和光标位置，以及源文件对应行。识别 Link 0、route、标题、电荷/多重度、坐标和关键词要求的附加区块。核对空行、ASCII 标点、括号、关键词版本、外部文件和 Link1 边界。回到原文件核对实际字符。 |
| 电荷、多重度不匹配 | 计算显式电子数 `N = Σ Zᵢ − Σ Ncore,ECP − q`，去除 ghost 等无电子中心。一般自旋定义下，`Nα = (N + M − 1)/2`、`Nβ = (N − M + 1)/2` 都应为非负整数。比较日志电子数，并核对质子化、自由基、氧化态和用户目标。ONIOM、Counterpoise、片段初猜应逐层或逐片段解释。 |
| `Gen`、`GenECP`、`Pseudo=Read`、内置混合基组 | 将输入每个中心映射到实际输出的基组和 ECP，检查遗漏、重复、中心编号、shell 角动量约定、分隔符 `****` 与区块顺序。确认 ECP 版本、替代的核电子数和对应的价基组。对重元素或混合代码检查原始定义及 Gaussian 中实际展开。 |
| `Geom=Check` 或 `Geom=AllCheck` | `Check` 从检查点取结构并保留输入中所需标题与电荷多重度。 `AllCheck` 同时读取结构、标题、电荷与多重度，仍需按 route 提供外部基组等附加数据。遇到多片段、约束、ONIOM 或其他专门几何格式，查具体任务输入规则。 |
| `Guess=Read`、`Opt=Restart`、`Freq=ReadFC`、`IRC=RCFC` | 先明确要复用轨道、优化状态、频率所用力常数还是 IRC 初始 Hessian。核对最后成功写入、Gaussian 版本、几何和原子次序、态、基组与理论级别。续接优化历史与使用上次几何开启新优化有不同语义。使用旧 Hessian 作优化初猜可以是近似策略，目标理论级别的频率与 IRC 仍要匹配各自用途。 |

对于检查点读取失败，区分文件路径错误、计算节点不可见、权限、文件不完整、格式或内容不符。先检查文件位置和关联作业，再决定是否能用提供的 `.fchk` 或另存的几何重建。目录有几个时间接近的 `.chk` 时，依据输入和运行记录配对。

续算方案中，`%OldChk=prior.chk` 表明要读取的原检查点，`%Chk=retry.chk` 指定本次的新检查点。核对两个路径和所需内容，避免把失败尝试写回唯一的检查点。需要跨版本或跨平台读取时，按 Gaussian 工具说明确认兼容格式。

## Slurm、进程、I/O

| 线索 | 取证与处理 |
| --- | --- |
| `TIMEOUT`、`CANCELLED`、`PREEMPTED`、`NODE_FAIL` | 先按作业 ID 和 step 配对 `sacct` 或 stdout/stderr，再把时间与最后的 Gaussian 操作对齐。确认具体状态和信号。若日志末尾只停在 SCF、Hessian 或积分阶段，该阶段表示中断位置。 |
| `OUT_OF_MEMORY`、allocation error、`Killed` | 同时查 Gaussian 错误、调度器或 cgroup OOM 和配置。区分单任务 `MaxRSS`、作业申请内存与节点或 step 上限。检查 `--mem` 与 `--mem-per-cpu` 的单位和作用域、Gaussian `%Mem`、进程与线程数并预留开销。仅有 `Killed` 时优先取调度器记录。 |
| `Erroneous write`、`No space left on device`、`FileIO`、文件无法打开 | 核对文件路径和失败动作，检查 `GAUSS_SCRDIR`、工作目录、节点可见性、磁盘配额、容量、inode 和权限。后 HF、数值频率与大基组任务尤其需要审计 scratch 峰值。保留需要续算的检查点和输入。 |
| 空日志、调度成功、Gaussian 结果缺失 | 检查启动命令、模块环境、输入/输出重定向、子进程退出值、作业和 step。批处理脚本可能在 Gaussian 失败后用另一条命令的成功状态退出。 |
| `segmentation violation`、`Error termination via Lnk1e` 或尾部执行文件编号 | 这些信息可定位异常类型或模块。查前文第一条具体错误、计算阶段、调度信息和输入，才可推断故障原因。输入与资源证据都不足时，记录可复现条件并检查相同任务的最小算例。 |

若用户只提供了输入和 log，先做本地诊断。需要时请用户提供带表头的调度表或对应标准错误，字段可包含 JobID、State、ExitCode、Elapsed、Timelimit、ReqMem、AllocCPUS 和 MaxRSS。

资料依据见[来源索引](sources.md)的 Gaussian 输入、Slurm、基组选择和资源案例。
