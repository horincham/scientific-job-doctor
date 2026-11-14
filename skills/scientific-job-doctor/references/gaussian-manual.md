# Gaussian 官方手册提炼

以下条目按 Gaussian 网页关键词说明和技术白皮书重新表述。每条给出软件行为和它在诊断中的用法。先确认日志里的版本和 revision。Gaussian 09、Gaussian 16 和不同平台的支持范围、默认值和限制可能有差别。

## 输入与检查点

### Link 0 的检查点与资源

`%Chk` 指定当前计算使用的检查点。设置 `%OldChk` 时，程序把旧检查点内容复制到当前工作检查点，供后续关键词读取。在日志与原输入中核对两个路径、源头作业及所需数据，再决定可读取几何、轨道还是力常数。Gaussian 的内存设置与调度器分配分别核对。 [Link 0 Commands](https://gaussian.com/link0/)

### 从检查点读取几何和轨道

`Geom=Checkpoint` 从检查点取结构，输入仍给电荷和多重度。`Geom=AllCheck` 也从检查点取标题、电荷和多重度。`Guess=Read` 涉及轨道初猜。诊断读入失败或电子数异常时，先核实检查点到底包含什么以及本次 route 还要求哪些外部块。 [Geom](https://gaussian.com/geom/) · [Guess](https://gaussian.com/guess/)

### Gen、GenECP 与基组

`Gen` 从输入读取基组定义。`GenECP` 同时读取基组与 ECP，相当于配合赝势读取选项使用 `Gen`。先核对原子或中心标签、分隔以及实际赋给各原子的基组，再检查 ECP 区块、替代的核电子数及相应价基组。 [Gen and GenECP](https://gaussian.com/gen/)

## 单点和波函数

### SCF 收敛

Gaussian 的 `SCF=Conver=N` 对常规 SCF 约束密度矩阵变化的 RMS 和最大值。能量趋势可帮助区分快慢与振荡，判定是否达标仍需查实际收敛信息。`XQC` 在常规 SCF 未收敛时转入 QC 步骤。厂商说明列出 QC 对 restricted open-shell 的限制，推荐前核对参考态、已用算法和版本。 [SCF](https://gaussian.com/scf/)

### Stable 与 Stable=Opt

`Stable` 检查指定单行列式解在可考虑的轨道扰动下的稳定性。`Stable=Opt` 可在检测到不稳定后继续优化波函数。若得到新解，记录对应的能量、占据和自旋，并核对几何、频率或性质是否还对应这个解。 [Stable](https://gaussian.com/stable/)

### MP 与 CCSD(T)

相关方法的参考 SCF、相关能和最终所需能量各有用途。厂商的 CCSD(T) 示例在 CC 振幅收敛与 `E(Corr)` 之后给出单独的 `CCSD(T)=` 总能量。遇到算到一半的日志，应确认请求的相关方法、参考类型与实际完成阶段，再定位最终能量字段。 [MP Methods](https://gaussian.com/mp/) · [CCD and CCSD](https://gaussian.com/cc/)

## 优化、反应路径与振动

### Opt、Restart、约束和 QST

`Opt` 的步数和收敛条件与 SCF 迭代独立。优化续接需要优化历史，单独读取旧几何可以开启新的优化。QST2 提供两个端点，QST3 还要提供 TS 初猜，结构间保持原子顺序一一对应。检查 `ModRedundant` 引用的坐标和约束，并区分 Hessian 初猜、优化期间的本征值检查与最终振动验收。 [Opt](https://gaussian.com/opt/)

### Freq 与 ReadFC

振动频率从力常数和质量得到。`ReadFC` 可以复用检查点中的力常数。诊断时应确认求得或读到的是目标构型、理论级别与电子态的 Hessian。观察实际振动模式，结合频率和收敛判断驻点。 [Freq](https://gaussian.com/freq/) · [Vibrational Analysis](https://gaussian.com/wp-content/uploads/dl/vib.pdf)

### IRC 与 RCFC

`IRC=RCFC` 读取现有笛卡尔力常数。`CalcFC` 请求在起始点计算力常数。选择续算前，核对 Hessian 的来源和起始 TS。`Forward` 和 `Reverse` 控制计算方向，化学端点须根据实际路径、原子映射与构型验收。 [IRC](https://gaussian.com/irc/)

### 热化学的修正与汇总

Gaussian 热化学输出同时给出热修正量和加入电子能后的汇总值。重组不同理论级别时，先明确电子能来源、温压和标准态，再从同一频率段取目标修正。低频模式、柔性构象或特殊体系需另外评估 RRHO 近似。 [Thermochemistry](https://gaussian.com/wp-content/uploads/dl/thermo.pdf)

## 溶剂与电子激发

### SCRF 与溶剂响应

`SCRF` 选择连续介质模型及溶剂。对 SMD 核对有关非静电贡献和所需能量定义。垂直与弛豫的激发过程涉及不同的溶剂响应条件，按具体路由核对所用模型、平衡或非平衡设置以及真实输出。 [SCRF](https://gaussian.com/scrf/)

### Counterpoise 片段计算

`Counterpoise=N` 表示片段数。排查时核对片段赋值、电荷与多重度，及片段在 ghost 基组存在时的子任务。固定几何的相互作用量与相对独立弛豫片段的结合量需要各自的能量定义。 [Counterpoise](https://gaussian.com/counterpoise/)

### TD 的根与目标电子态

`NStates` 控制求解的态数，`Root` 指定关注的根。优化、扫描和性质计算要核对输出里实际参与计算的态、梯度和状态特征。根序号和最终收敛标记无法独立确认电子态沿几何路径的身份。 [TD](https://gaussian.com/td/)

## 进阶关键词

### CASSCF 的活性空间

检查 route 给的活性电子数和活性轨道数。用 `StateAverage` 时核对 `NRoot`、参与平均的各根及权重。确认轨道分区、占据和所求状态，尤其在多几何计算中检查初猜和轨道交换。 [CASSCF](https://gaussian.com/cas/)

### ONIOM 层和性质

核对 model/real 的原子层级、边界原子、所用方法以及电荷多重度。机械或电子嵌入会影响高层与环境的相互作用。用实际层设置和各分项输出解释总能量。 [ONIOM](https://gaussian.com/oniom/)

### Properties 的密度与参照

Population 和部分性质使用计算得到的电子密度或轨道，所用密度随方法和关键词变化。NMR 输出屏蔽张量，化学位移还要注明参照及换算。检查实际密度、物理量单位、参照和张量坐标系。 [Population](https://gaussian.com/population/) · [NMR](https://gaussian.com/nmr/) · [Polar](https://gaussian.com/polar/)

### 分子动力学

BOMD 和 ADMP 的传播方案不同。先根据所用方法核对积分步、实际输出、轨迹完整性、能量分量及电子自由度处理，再判断数值异常或续算条件。 [BOMD](https://gaussian.com/bomd/) · [ADMP](https://gaussian.com/admp/)
