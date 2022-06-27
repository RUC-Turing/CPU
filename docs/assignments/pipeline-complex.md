# 流水线 MIPS 处理器（50 条）

设计并实现流水线 MIPS 处理器，支持所列举的 MIPS 指令。

## 实验指导

### 指令集

需要支持的指令如下：

* R 型指令
    * `ADD` 有符号加法
    * `ADDU` 无符号加法
    * `SUB` 有符号减法
    * `SUBU` 无符号减法
    * `SLL` 逻辑左移
    * `SRL` 逻辑右移
    * `SRA` 算术右移
    * `SLLV` 逻辑左移（移位量在寄存器中）
    * `SRLV` 逻辑右移（移位量在寄存器中）
    * `SRAV` 算术右移（移位量在寄存器中）
    * `AND` 按位与
    * `OR` 按位或
    * `XOR` 按位异或
    * `NOR` 按位或，并按位取反
    * `SLT` 有符号比较
    * `SLTU` 无符号比较
* 立即数指令
    * `ADDI` 有符号加法
    * `ADDIU` 无符号加法
    * `ANDI` 按位与
    * `ORI` 按位或
    * `XORI` 按位异或
    * `SLTI` 有符号比较
    * `SLTIU` 无符号比较
* 加载指令
    * `LUI` 加载立即数到高位
* 乘除法指令
    * `MULT` 有符号乘法
    * `MULTU` 无符号乘法
    * `DIV` 有符号除法
    * `DIVU` 无符号除法
    * `MFHI` 读取 HI 寄存器
    * `MTHI` 写入 HI 寄存器
    * `MFLO` 读取 LO 寄存器
    * `MTLO` 写入 LO 寄存器
* 分支指令
    * `BEQ` 相等时跳转
    * `BNE` 不相等时跳转
    * `BLEZ` 小于零时跳转
    * `BGTZ` 大于零时跳转
    * `BGEZ` 小于或等于零时跳转
    * `BLTZ` 大于或等于零时跳转
* 跳转指令
    * `JR` 跳转到寄存器中的地址
    * `JALR` 跳转到寄存器中的地址，并写入返回地址到寄存器
    * `J` 跳转
    * `JAL` 跳转，并写入返回地址到寄存器
* 访存指令
    * `LB` 非对齐加载（字节）并带符号扩展
    * `LBU` 非对齐加载（字节）并无符号扩展
    * `LH` 非对齐加载（半字）并带符号扩展
    * `LHU` 非对齐加载（半字）并无符号扩展
    * `LW` 对其加载
    * `SB` 非对齐存储（字节）
    * `SH` 非对齐存储（半字）
    * `SW` 对齐存储

同样，为了方便测试，请识别 `syscall` 指令，并在该指令执行完成后使用 `$finish` 语句结束仿真。

在流水线 CPU 中，我们需要处理分支延迟槽（Branch Delay Slot）。在使用 Mars 工具辅助测试时，请确保 Mars 的[延迟分支](/tools/mars.md#延迟分支)选项已**开启**。

### 乘除法

本次实验要求实现对乘除法指令的支持。与普通的算术运算指令由算术逻辑单元（ALU）完成不同，MIPS 中的乘除法指令由乘除法单元（MultiplicationDivisionUnit，MDU）来完成。

在流水线中 MDU 与 ALU 同样处于 EX 级，但 MDU 的运算是非阻塞的。由于乘除法的开销较大，当发起一次乘除法运算时，运算会保持在 MDU 中运行多个周期，不会在当前周期得到结果。运算完成后，MDU 将运算结果写入到两个内部寄存器 HI 和 LO 中。HI 和 LO 不是通用寄存器，只能通过对应的指令来访问。

当需要读取结果（MFLO / MFHI）但结果未计算完成时，MDU 处于忙碌状态，当前的指令执行阻塞在 ID/EX。

以下是乘除法器模块接口的参考设计：

```systemverilog
// 模拟乘除法指令的延迟
`define MUL_DELAY_CYCLES 5  // 乘法需要 5 个周期
`define DIV_DELAY_CYCLES 10 // 除法需要 10 个周期

typedef logic [63:0] _mdu_long_t;
typedef logic [31:0] _mdu_int_t;

// 定义操作类型
typedef enum logic [2:0] {
    MDU_READ_HI,
    MDU_READ_LO,
    MDU_WRITE_HI,
    MDU_WRITE_LO,
    MDU_START_SIGNED_MUL,
    MDU_START_UNSIGNED_MUL,
    MDU_START_SIGNED_DIV,
    MDU_START_UNSIGNED_DIV
} mdu_operation_t;

module MultiplicationDivisionUnit(
    // 重置（Reset）信号，设置时表示将状态恢复为初始状态（全 0）。
    input logic reset,
    // 时钟信号，请接入全局时钟，并在时钟沿时（如，上升沿时）对寄存器变量赋值。
    input logic clock,

    // 乘除法运算的第一个操作数。
    input _mdu_int_t operand1,
    // 乘除法运算的第二个操作数。
    input _mdu_int_t operand2,
    // 要进行的操作类型。
    input mdu_operation_t operation,

    // 当前指令是否开始使用乘除法器。
    input logic start,

    // 输出当前乘除法器是否处于忙碌状态。
    // 当乘除法器处于忙碌状态时，乘除法指令在 ID/EX 级阻塞。
    output logic busy,
    // 由 MFLO / MFHI 指令读取到的结果。
    output _mdu_int_t dataRead
);
```

为了和 Mars 的行为一致，请将乘除法器实现为**在除数为 0 时会保留 HI / LO 的旧值**。

### 测试

与[上个实验](./pipeline-simple.md#测试)要求相同。
