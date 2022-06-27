# ALU

使用 Verilog 编写 32 位 ALU 模块。

## 实验目的

通过编写一个稍复杂的 32 位 ALU（Arithmetic Logic Unit，算术/逻辑单元）模块，熟悉 Verilog 的用法，并熟悉多模块项目的编写。

## 实验指导

在项目中加入文件 `alu.v` 和 `alu_tb.v`，并加入上一次实验中编写的 `adder.v`。其中 `alu.v` 包含一个 ALU 模块，其接口如下：

```verilog
module alu(
    input [31:0] operationCode,
    input [31:0] operand1,
    input [31:0] operand2,
    output [21:0] result,
    output overflow
);
endmodule
```

其中 `operationCode` 参数为运算类型。不同运算类型的说明如下（仅有符号加减法运算设置 `overflow`）：

|`operationCode`|指令名|功能|备注|
|:---:|:-------------:|:--:|:-:|
|`100000`|`ADD`|有符号加法||
|`100001`|`ADDU`|无符号加法|`overflow` 恒为 0|
|`100010`|`SUB`|有符号减法||
|`100011`|`SUBU`|无符号减法|`overflow` 恒为 0|
|`000000`|`SLL`|逻辑左移|`operand1` 的低 5 位为移位位数，`operand2` 为操作数|
|`000010`|`SRL`|逻辑右移|`operand1` 的低 5 位为移位位数，`operand2` 为操作数|
|`000011`|`SRA`|算术右移|`operand1` 的低 5 位为移位位数，`operand2` 为操作数|
|`100100`|`AND`|按位与||
|`100101`|`OR`|按位或||
|`100110`|`XOR`|按位异或||
|`100111`|`NOR`|按位或非|即，将按位或的结果取反|

其中加减法运算请使用前一个实验中的加法器（`adder.v`）来实现，以练习模块调用。其他操作使用 Verilog 内置运算符即可。

另外，请仿照前一个实验中给出的测试文件，自行设计 `alu_tb.v` 进行测试。

## 实验要求

完成 ALU 的实现，并自行设计测试文件，验证 ALU 的正确性。

提交代码（三个文件）和实验报告，实验报告中应包含表明结果正确的波形图截图。
