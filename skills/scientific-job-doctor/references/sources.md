# Gaussian 诊断来源索引

每次诊断只引用实际使用的资料。软件文档用于核实关键词和版本行为，研究论文与作者资料用于核实方法定义，论坛案例提供排查线索。检查原帖所涉程序、方法和适用条件后再迁移到当前任务。

## 计算化学公社原帖

以下为首版核对过的主题正文及相关回帖。案例记录来自帖子正文，未复跑附件。若 HTTPS 访问超时，可尝试这里列出的公社公开 HTTP 原帖。

| 公社原帖 | 可用于核对的判断 |
| --- | --- |
| [Gaussian 的安装方法及运行时的相关问题](http://bbs.keinsci.com/thread-10814-1-1.html) | 区分程序的资源、环境和 scratch 设置。历史版本的绝对内存限制随平台核实。 |
| [高斯优化木质素磺酸钠出错](http://bbs.keinsci.com/thread-25717-1-1.html) | 旧版 Windows 案例说明必须核对平台、真实错误和实际内存上限。 |
| [谈谈量子化学中基组的选择](http://bbs.keinsci.com/thread-3545-1-1.html) | 根据研究目标选择基组，核对用途、元素覆盖和计算代价。 |
| [求助高斯优化含金属的小分子的问题](http://bbs.keinsci.com/thread-31604-1-1.html) | 含金属输入先查格式、结构近接、基组/ECP 与电荷多重度。 |
| [Gaussian 16 中对 Ti 的计算采用 SDD 基组考虑了相对论效应吗](http://bbs.keinsci.com/thread-27982-1-1.html) | 相对论解释追溯到所用 ECP。报告实际 ECP 类型与所包含的物理效应。 |
| [什么情况下可以用其他方法或基组的 Hessian 和波函数](http://bbs.keinsci.com/thread-30123-1-1.html) | 区分低级别初猜与最终结果，迁移时核对 ECP 核电子数、轨道和几何。 |
| [判断得到的构型是否为自旋极化单重态](http://bbs.keinsci.com/thread-27538-1-1.html) | 比较波函数稳定性、自旋密度与 `⟨S²⟩`，尤其是双自由基和解离。 |
| [简谈 Gaussian 里找过渡态的关键词 Opt=TS 和 QST2/3](http://bbs.keinsci.com/thread-12093-1-1.html) | TS 初猜、QST 端点原子对应、Hessian 和最终的频率/IRC 验收。 |
| [氢自由基攻击 PDMS 分子的过渡态搜索](http://bbs.keinsci.com/thread-54543-1-1.html) | 依据前文确认优化过程中的本征值检查，核对最终实际虚模。 |
| [IRC 产物与反应物结构相同](http://bbs.keinsci.com/thread-1994-1-1.html) | 路径长度按接近极小点的证据判断。区分受限优化、鞍点和端点。 |
| [结构优化收敛、没有虚频但几何变化](http://bbs.keinsci.com/thread-58057-1-1.html) | 优化和频率之外还要核查最终结构、连接性与研究目的。 |
| [复现二硫键及 C–S 键能的讨论](http://bbs.keinsci.com/thread-36267-1-1.html) | 先匹配几何、理论级别、计算设置和结果的定义。 |
| [势能面交叉对激发态优化的影响](http://bbs.keinsci.com/thread-12318-1-1.html) | 有 G16 A.03 算例。比较态的能量顺序与特征，并核对随版本变化的跟踪行为。 |
| [TD(Root=2) 的柔性扫描遇到态排序变化](http://bbs.keinsci.com/thread-48544-1-1.html) | 以相邻结构和态特征解释根排序变化的线索。 |
| [CASSCF 活性轨道选取讨论](http://bbs.keinsci.com/thread-46834-1-1.html) | 活性空间选择涉及轨道性质和研究目标。讨论中的 ORCA 输出格式按原程序处理。 |
| [公社群聊 Q&A 整理](http://bbs.keinsci.com/thread-3954-1-1.html) | 有关于 SCF、虚频和扫描坐标的案例入口。优先核对对应长文和任务证据。 |

## 关键词与运行手册

- Gaussian [关键词总表](https://gaussian.com/keywords/)和 [GaussView 手册](https://gaussian.com/wp-content/uploads/dl/gv6.pdf)。
- 输入与电子结构 [Link 0 命令](https://gaussian.com/link0/)、[Geom](https://gaussian.com/geom/)、[Guess](https://gaussian.com/guess/)、[Gen/GenECP](https://gaussian.com/gen/)、[SCF](https://gaussian.com/scf/)、[Stable](https://gaussian.com/stable/)、[MP 方法](https://gaussian.com/mp/)、[CCD 与 CCSD](https://gaussian.com/cc/)和 [formchk](https://gaussian.com/formchk/)。
- 常用任务 [Opt](https://gaussian.com/opt/)、[Freq](https://gaussian.com/freq/)、[IRC](https://gaussian.com/irc/)、[TD](https://gaussian.com/td/)、[SCRF](https://gaussian.com/scrf/)和 [Counterpoise](https://gaussian.com/counterpoise/)。
- 进阶任务 [CASSCF](https://gaussian.com/cas/)、[ONIOM](https://gaussian.com/oniom/)、[Population](https://gaussian.com/population/)、[NMR](https://gaussian.com/nmr/)、[Force](https://gaussian.com/force/)、[Polar](https://gaussian.com/polar/)、[BOMD](https://gaussian.com/bomd/)、[ADMP](https://gaussian.com/admp/)和 [PBC](https://gaussian.com/pbc/)。
- Gaussian 技术白皮书 [Vibrational Analysis](https://gaussian.com/wp-content/uploads/dl/vib.pdf)和 [Thermochemistry](https://gaussian.com/wp-content/uploads/dl/thermo.pdf)。
- SchedMD [作业状态](https://slurm.schedmd.com/job_state_codes.html)、[退出码](https://slurm.schedmd.com/job_exit_code.html)和 [sacct](https://slurm.schedmd.com/sacct.html)。

## 领域作者资料与原始方法

- 卢天 [SCF 不收敛](https://www.umsyar.com/61)和[几何优化收敛](https://www.umsyar.com/164)。用于区分慢收敛、振荡、初猜与迭代设置。
- 卢天 [优化后 NO 或虚频](https://www.umsyar.com/278)、[小虚频与热化学](https://www.umsyar.com/699)和[计算 IRC 的方法和常见问题](https://www.umsyar.com/400)。用于检查模式性质和路径终点。
- 卢天 [Gaussian TDDFT 激发态及吸收、荧光、磷光](https://www.umsyar.com/314)和[复现计算结果时常见差异](https://www.umsyar.com/678)。
- 卢天 [隐式溶剂模型与自由能](https://www.umsyar.com/327)和[BSSE 及 Gaussian 的处理](https://www.umsyar.com/46)。
- Lu 和 Chen [Shermo](https://www.cambridge.org/engage/chemrxiv/article-details/60c74b4f0f50db2bc7396be2)。用于 RRHO 变体、低频和热化学后处理假设。
- Marenich、Cramer 和 Truhlar [SMD 原始论文](https://doi.org/10.1021/jp810292n)。用于核对溶剂化模型定义和贡献。
- Boys 和 Bernardi [Counterpoise 原始论文](https://doi.org/10.1080/00268977000101561)。用于核对片段共用基组的相互作用能定义。
- MOKIT 开发者 [活性空间说明](https://jeanwsr.gitlab.io/mokit-doc-mdbook/chap3-4.html)和[程序仓库](https://github.com/1234zou/MOKIT)。用于活性空间与轨道转换。
- Dapprich 等 [Gaussian ONIOM 实现论文信息](https://tudoster.unideb.hu/en/publikacio/BIBFORM055539)。用于核对能量、梯度和分层计算定义。
- Tian Lu 和 Feiwu Chen [Multiwfn 论文](https://doi.org/10.1002/jcc.22885)与[项目](https://www.umsyar.com/multiwfn)。用于后处理前确认可读取的波函数数据、电子密度与性质定义。
