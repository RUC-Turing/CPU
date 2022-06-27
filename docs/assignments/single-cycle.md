# 单周期 MIPS 处理器

设计并实现单周期 MIPS 处理器，支持所列举的少部分 MIPS 指令。

## 实验指导

### 指令集

需要支持的指令如下：

* `ADDU` 寄存器加法
* `SUBU` 寄存器减法
* `ORI` 立即数或
* `LW` 对齐加载
* `SW` 对齐存储
* `BEQ` 相等时跳转
* `LUI` 加载立即数到高位
* `JAL` 函数调用
* `JR` 寄存器跳转

另外，为了方便测试，请识别 `syscall` 指令，并在该指令执行完成后使用 `$finish` 语句结束仿真。

在单周期 CPU 中，我们不处理分支延迟槽（Branch Delay Slot），即与 x86 / ARM / RISC-V 类似，条件跳转指令会在执行后立即生效。在使用 Mars 工具辅助测试时，请确保 Mars 的[延迟分支](/tools/mars.md#延迟分支)选项已**关闭**。

### 数据通路

推荐将每个独立的模块写在单独的文件中，并在顶层实例化各个模块：

* `DataMemory` 读取/写入数据存储器
    * 大小为 4 KiB，即 1024 字
    * 初始化为全零
* `InstructionMemory` 读取指令存储器
    * 大小为 4 KiB，即 1024 字
    * 指令存储为只读，使用 `initial` 指令在仿真启动时初始化，见下文讲解
* `ProgramCounter` 维护 PC 寄存器的值
    * 功能与上次实验中所要求的一致
    * PC 寄存器的初始值为 `0x00003000`，被自动截断后指向指令存储器的 0 位置
* `ControllerUnit` 对指令进行解码并输出控制信号
    * 输出控制信号的逻辑较为复杂，建议使用 `always` / `always_comb` 组合逻辑块实现硬布线
    * 建议学习进阶的 SystemVerilog 语法，以便使用 `struct` 将控制信号组合在结构体中
* `GeneralPurposeRegisters` 维护通用寄存器值
    * 寄存器与数据存储器相同，使用 `reg` 数组实现，在 `reset` 信号时清零，有两个读取端和一个写入端
    * 输入：要读取的寄存器编号 1、编号 2 以及要写入的寄存器编号
    * 输入：是否开启写入、需要写入的值
    * 输出：读取到的值
    * 初始化为全零
* `ArithmeticLogicUnit` 进行算术/逻辑运算
    * 与之前的实验中的要求类似，可以不使用之前的代码，而是在控制信号中自行定义各种运算的操作码并重新实现

请在顶层根据控制信号将数据通路连接，并处理跳转指令。顶层模块接受测试文件提供的 `clock` 和 `reset` 两个输入信号，没有输出。

### 测试

使用以下测试文件进行测试：

```verilog
module mips_tb();
    initial $fsdbDumpvars();

    reg reset, clock;

    // 将此处被实例化的模块名 TopLevel 改为你的顶层模块名
    TopLevel topLevel(.reset(reset), .clock(clock));

    integer k;
    initial begin
        // 按住 Reset 键，保持一个周期以上并松开
        reset = 1;
        clock = 0; #1;
        clock = 1; #1;
        clock = 0; #1;
        reset = 0; #1;
        
        #1;
        for (k = 0; k < 5000; k = k + 1) begin // 运行 5000 个周期
            clock = 1; #5;
            clock = 0; #5;
        end

        // 请在遇到 syscall 指令并执行完成后停止
        // 停止在此处说明运行错误或者周期数不够
        $finish;
    end
    
endmodule
```

## 实验要求

请提交项目中的所有代码文件，助教将在实验课上现场检查你的代码与运行结果。
