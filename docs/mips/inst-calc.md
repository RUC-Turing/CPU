# 运算类指令

## 算术运算

### `ADD` 有符号加法

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_100000`
* **编码**
    * `op = 000000`
    * `func = 100000`
    * `rs` 源寄存器：加数 1
    * `rt` 源寄存器：加数 2
    * `rd` 目标寄存器

对两个寄存器中的整数执行加法，结果保存到目标寄存器中。

当发生有符号运算溢出时，产生一个异常。

### `ADDU` 无符号加法

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_100001`
* **编码**
    * `op = 000000`
    * `func = 100001`
    * `rs` 源寄存器：加数 1
    * `rt` 源寄存器：加数 2
    * `rd` 目标寄存器

对两个寄存器中的整数执行加法，结果保存到目标寄存器中。

### `SUB` 有符号减法

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_100010`
* **编码**
    * `op = 000000`
    * `func = 100010`
    * `rs` 源寄存器：被减数
    * `rt` 源寄存器：减数
    * `rd` 目标寄存器

对两个寄存器中的整数执行减法，结果保存到目标寄存器中。

当发生有符号运算溢出时，产生一个异常。

### `SUBU` 无符号减法

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_100011`
* **编码**
    * `op = 000000`
    * `func = 100011`
    * `rs` 源寄存器：被减数
    * `rt` 源寄存器：减数
    * `rd` 目标寄存器

对两个寄存器中的整数执行减法，结果保存到目标寄存器中。

## 按位运算

### `AND` 按位与

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_100100`
* **编码**
    * `op = 000000`
    * `func = 100100`
    * `rs` 源寄存器：操作数 1
    * `rt` 源寄存器：操作数 2
    * `rd` 目标寄存器

对两个寄存器中的整数执行按位与，结果保存到目标寄存器中。

### `OR` 按位或

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_100101`
* **编码**
    * `op = 000000`
    * `func = 100101`
    * `rs` 源寄存器：操作数 1
    * `rt` 源寄存器：操作数 2
    * `rd` 目标寄存器

对两个寄存器中的整数执行按位或，结果保存到目标寄存器中。

### `XOR` 按位异或

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_100110`
* **编码**
    * `op = 000000`
    * `func = 100110`
    * `rs` 源寄存器：操作数 1
    * `rt` 源寄存器：操作数 2
    * `rd` 目标寄存器

对两个寄存器中的整数执行按位异或，结果保存到目标寄存器中。

### `NOR` 按位或非

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_100111`
* **编码**
    * `op = 000000`
    * `func = 100111`
    * `rs` 源寄存器：操作数 1
    * `rt` 源寄存器：操作数 2
    * `rd` 目标寄存器

对两个寄存器中的整数执行按位或非（先按位或，再对结果取非），结果保存到目标寄存器中。

**注：**这个指令看起来很奇怪，它一般被用于对一个寄存器进行取反（另一个寄存器填 `$0`），但有时相邻的位运算也可能能够被编译器优化到这一个指令中。

## 移位运算

### `SLL` 左移

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_000000`
* **编码**
    * `op = 000000`
    * `func = 000000`
    * `rs` 源寄存器：被移位数
    * `shamt` 移位量
    * `rd` 目标寄存器

将寄存器中的整数进行按位左移，结果保存到目标寄存器中。

全 0 的一条指令是一条良构的 SLL 指令（将 `$0` 左移 0 位存到 `$0` 中），且不做任何操作。这是一条常用的 NOP（no-op）指令。

### `SRL` 逻辑右移

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_000010`
* **编码**
    * `op = 000000`
    * `func = 000010`
    * `rs` 源寄存器：被移位数
    * `shamt` 移位量
    * `rd` 目标寄存器

将寄存器中的整数进行按位逻辑右移（高位补 0），结果保存到目标寄存器中。

### `SRA` 算术右移

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_000011`
* **编码**
    * `op = 000000`
    * `func = 000011`
    * `rs` 源寄存器：被移位数
    * `shamt` 移位量
    * `rd` 目标寄存器

将寄存器中的整数进行按位算术右移（高位按原最高位补 0 或 1，即保留补码意义下的符号），结果保存到目标寄存器中。

### `SLLV` 左移（可变移位量）

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_000100`
* **编码**
    * `op = 000000`
    * `func = 000100`
    * `rs` 源寄存器：被移位数
    * `rd` 源寄存器：移位量（取低 5 位，即移位量最多为 31 位）
    * `rd` 目标寄存器

将寄存器中的整数进行按位左移，从另一个寄存器中获取移位量，结果保存到目标寄存器中。

全 0 的一条指令是一条良构的 SLL 指令（将 `$0` 左移 0 位存到 `$0` 中），且不做任何操作。这是一条常用的 NOP（no-op）指令。

### `SRLV` 逻辑右移（可变移位量）

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_000110`
* **编码**
    * `op = 000000`
    * `func = 000110`
    * `rs` 源寄存器：被移位数
    * `rd` 源寄存器：移位量（取低 5 位，即移位量最多为 31 位）
    * `rd` 目标寄存器

将寄存器中的整数进行按位逻辑右移（高位补 0），从另一个寄存器中获取移位量，结果保存到目标寄存器中。

### `SRAV` 算术右移（可变移位量）

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_000111`
* **编码**
    * `op = 000000`
    * `func = 000111`
    * `rs` 源寄存器：被移位数
    * `rd` 源寄存器：移位量（取低 5 位，即移位量最多为 31 位）
    * `rd` 目标寄存器

将寄存器中的整数进行按位算术右移（高位按原最高位补 0 或 1，即保留补码意义下的符号），从另一个寄存器中获取移位量，结果保存到目标寄存器中。

## 比较运算

### `SLT` 判断小于（有符号）

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_101010`
* **编码**
    * `op = 000000`
    * `func = 101010`
    * `rs` 源寄存器：左操作数
    * `rt` 源寄存器：右操作数
    * `rd` 目标寄存器

对两个寄存器中的整数进行有符号比较，判断是否满足 `左操作数 < 右操作数`，如果成立结果则为 1，否则为 0，结果保存到目标寄存器中。

### `SLTU` 判断小于（无符号）

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_101011`
* **编码**
    * `op = 000000`
    * `func = 101011`
    * `rs` 源寄存器：左操作数
    * `rt` 源寄存器：右操作数
    * `rd` 目标寄存器

对两个寄存器中的整数进行无符号比较，判断是否满足 `左操作数 < 右操作数`，如果成立结果则为 1，否则为 0，结果保存到目标寄存器中。

## 乘除法运算

乘除法运算指令涉及到乘除法器。乘除法器中的乘除法运算往往需要多个周期完成，在等待前一次运算结果时，新的乘除法器指令将被阻塞。

### `MULT` 有符号乘法

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_011000`
* **编码**
    * `op = 000000`
    * `func = 011000`
    * `rs` 源寄存器：乘数 1
    * `rt` 源寄存器：乘数 2

启动乘除法器，对两个寄存器中的整数进行有符号乘法运算。当运算需要多个周期完成时，此指令不等待运算结束，而是在当前周期立即返回，乘法操作将在乘除法器中后台进行，阻塞之后调用乘除法器的指令。

乘法结果的低 32 位保存在内部寄存器 `LO` 中，高 32 位保存在内部寄存器 `HI` 中。

### `MULTU` 无符号乘法

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_011001`
* **编码**
    * `op = 000000`
    * `func = 011001`
    * `rs` 源寄存器：乘数 1
    * `rt` 源寄存器：乘数 2

启动乘除法器，对两个寄存器中的整数进行无符号乘法运算。当运算需要多个周期完成时，此指令不等待运算结束，而是在当前周期立即返回，乘法操作将在乘除法器中后台进行，阻塞之后调用乘除法器的指令。

乘法结果的低 32 位保存在内部寄存器 `LO` 中，高 32 位保存在内部寄存器 `HI` 中。

### `DIV` 有符号除法

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_011010`
* **编码**
    * `op = 000000`
    * `func = 011010`
    * `rs` 源寄存器：被除数
    * `rt` 源寄存器：除数

启动乘除法器，对两个寄存器中的整数进行有符号除法运算。当运算需要多个周期完成时，此指令不等待运算结束，而是在当前周期立即返回，除法操作将在乘除法器中后台进行，阻塞之后调用乘除法器的指令。

除法结果的商保存在内部寄存器 `LO` 中，余数保存在内部寄存器 `HI` 中。

### `DIVU` 无符号除法

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_011011`
* **编码**
    * `op = 000000`
    * `func = 011011`
    * `rs` 源寄存器：被除数
    * `rt` 源寄存器：除数

启动乘除法器，对两个寄存器中的整数进行无符号除法运算。当运算需要多个周期完成时，此指令不等待运算结束，而是在当前周期立即返回，除法操作将在乘除法器中后台进行，阻塞之后调用乘除法器的指令。

除法结果的商保存在内部寄存器 `LO` 中，余数保存在内部寄存器 `HI` 中。

### `MFHI` 读取 HI 寄存器

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_010000`
* **编码**
    * `op = 000000`
    * `func = 010000`
    * `rd` 目标寄存器

读取乘除法器中的内部寄存器 `HI` 的值，保存在目标寄存器中。

### `MFLO` 读取 LO 寄存器

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_010010`
* **编码**
    * `op = 000000`
    * `func = 010010`
    * `rd` 目标寄存器

读取乘除法器中的内部寄存器 `LO` 的值，保存在目标寄存器中。

### `MTHI` 写入 HI 寄存器

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_010001`
* **编码**
    * `op = 000000`
    * `func = 010001`
    * `rs` 源寄存器

将一个寄存器的值写入到乘除法器中的内部寄存器 `HI` 中。

### `MTLO` 写入 LO 寄存器

* **类型** R 型
* **Verilog 表达式** `32'b000000_????????????????????_010011`
* **编码**
    * `op = 000000`
    * `func = 010011`
    * `rs` 源寄存器

将一个寄存器的值写入到乘除法器中的内部寄存器 `LO` 中。

## 立即数运算

涉及立即数的算术/按位/比较运算与原本只涉及寄存器（**注：**在 MIPS 编码中，常数的移位量不是立即数）的同语义指令不同，这些指令是 I 型指令，故单独列出。

这些指令中，与运算语义是否有符号无关，所有算术运算指令（包括比较指令）的立即数扩展方式为**带符号扩展**，而除此之外，所有按位运算指令的立即数扩展方式为**无符号扩展**。

### `ADDI` 立即数有符号加法

* **类型** I 型
* **Verilog 表达式** `32'b001000_????????????????????_??????`
* **编码**
    * `op = 001000`
    * `rs` 源寄存器：加数 1
    * `imme` 立即数：加数 2
    * `rd` 目标寄存器

对一个寄存器中的整数和一个立即数（**带符号扩展**到 32 位）执行加法，结果保存到目标寄存器中。

当发生有符号运算溢出时，产生一个异常。

### `ADDIU` 立即数无符号加法

* **类型** I 型
* **Verilog 表达式** `32'b001001_????????????????????_??????`
* **编码**
    * `op = 001001`
    * `rs` 源寄存器：加数 1
    * `imme` 立即数：加数 2
    * `rd` 目标寄存器

对一个寄存器中的整数和一个立即数（**带符号扩展**到 32 位）执行加法，结果保存到目标寄存器中。

**注：**与 `ADDI` 相同，`ADDIU` 的立即数扩展方式同样是**带符号扩展**。

### `ANDI` 立即数按位与

* **类型** I 型
* **Verilog 表达式** `32'b001100_????????????????????_??????`
* **编码**
    * `op = 001100`
    * `rs` 源寄存器：操作数 1
    * `imme` 立即数：操作数 2
    * `rd` 目标寄存器

对一个寄存器中的整数和一个立即数（**无符号扩展**到 32 位）执行按位与，结果保存到目标寄存器中。

**注：**与 `ADDI` 和 `ADDIU` 不同，`ANDI` 的立即数扩展方式是**无符号扩展**。另外两条立即数按位运算指令同为**无符号扩展**。

### `ORI` 立即数按位或

* **类型** I 型
* **Verilog 表达式** `32'b001101_????????????????????_??????`
* **编码**
    * `op = 001101`
    * `rs` 源寄存器：操作数 1
    * `imme` 立即数：操作数 2
    * `rd` 目标寄存器

对一个寄存器中的整数和一个立即数（**无符号扩展**到 32 位）执行按位或，结果保存到目标寄存器中。

### `XORI` 立即数按位异或

* **类型** I 型
* **Verilog 表达式** `32'b001110_????????????????????_??????`
* **编码**
    * `op = 001110`
    * `rs` 源寄存器：操作数 1
    * `imme` 立即数：操作数 2
    * `rd` 目标寄存器

对一个寄存器中的整数和一个立即数（**无符号扩展**到 32 位）执行按位异或，结果保存到目标寄存器中。

### `SLTI` 立即数判断小于（有符号）

* **类型** I 型
* **Verilog 表达式** `32'b001010_????????????????????_??????`
* **编码**
    * `op = 001010`
    * `rs` 源寄存器：操作数 1
    * `imme` 立即数：操作数 2
    * `rd` 目标寄存器

对一个寄存器中的整数和一个立即数（**带符号扩展**到 32 位）进行有符号比较，判断是否满足 `左操作数 < 右操作数`，如果成立结果则为 1，否则为 0，结果保存到目标寄存器中。

### `SLTIU` 立即数判断小于（无符号）

* **类型** I 型
* **Verilog 表达式** `32'b001011_????????????????????_??????`
* **编码**
    * `op = 001011`
    * `rs` 源寄存器：操作数 1
    * `imme` 立即数：操作数 2
    * `rd` 目标寄存器

对一个寄存器中的整数和一个立即数（**带符号扩展**到 32 位）进行无符号比较，判断是否满足 `左操作数 < 右操作数`，如果成立结果则为 1，否则为 0，结果保存到目标寄存器中。

### `LUI` 加载到高位

* **类型** I 型
* **Verilog 表达式** `32'b001111_????????????????????_??????`
* **编码**
    * `op = 001111`
    * `imme` 立即数
    * `rd` 目标寄存器

将一个立即数（16 位）加载到一个寄存器的高 16 位，并将低 16 位置零。
