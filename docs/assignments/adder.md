# 加法器

使用 Verilog 编写 32 位加法器。

## 实验目的

通过编写一个简单的 32 位加法器模块，熟悉 Verilog 的基本语法。

## 实验指导

在项目中加入文件 `adder.v` 和 `adder_tb.v`（`tb` 意为「Test Bench」）。其中 `adder.v` 包含一个加法器模块，其接口如下：

```verilog
module adder(
    input [31:0] operand1,
    input [31:0] operand2,
    output [31:0] result
);

endmodule
```

实现加法器时可以使用**行波进位**或者**超前进位**两种方式，前者可以使用 `generate` 或者 `always @ (*)` / `always_comb` 语句块来简化代码，后者可以编写代码生成器来生成代码（请不要直接使用 `+`）。

!!! info "提示"
    **行波进位**加法器将若干个一位全加器级联，其中每一位的进位输出将作为下一位的一个输入。优点是结构简单，电路开销较小；缺点是组合逻辑传播层数较多，延迟较高。
    **超前进位**加法器并行计算每一位的结果，计算每一位的结果时统一考虑之前所有位的结果是否造成对这一位的进位。优点是并行度高，延迟低；缺点是电路较为复杂，且复杂度随着位数提高而急剧提升。

    本次作业仅为一个例子，一般在编写 Verilog 代码时不需要单独编写加法器，更不需要考虑使用哪种加法器，直接使用 `+` 加法运算即可。

编写加法器后，编写测试文件 `adder_tb.v`，用于测试加法器的正确性。我们可以生成随机数据，将加法器的输出与 Verilog 内置加法运算 `+` 的结果进行对比，如果一致则说明加法器实现正确。

```verilog
module adder_tb();
    // 调用 VCS 仿真工具的功能，将变量导出到文件中，以便观测波形
    // 如果不需要波形图，则可以去掉这一行以减小开销
    initial $fsdbDumpvars();

    // a 和 b 为寄存器，将被随时间赋值
    reg [31:0] a, b;
    // result 为纯组合逻辑值
    wire [31:0] result;

    // 实例化全加器
    adder adder_inst(
      .operand1(a),
      .operand2(b),
      .result(result)
    );

    // 使用加法运算计算正确结果
    wire [31:0] answer;
    assign answer = a + b;

    // 判断结果是否相等
    wire equal;
    assign equal = result == answer;

    // 时序逻辑部分，执行多组测试
    // 注意：initial 语句不是电路的一部分，而是仿真程序的一部分，仅应在测试时使用
    integer i;
    initial begin
        for (i = 0; i < 256; i = i + 1)
        begin
            // 使用随机数对 a 和 b 进行赋值
            a <= $urandom();
            b <= $urandom();

            // 延迟 10 个单位时间，以便在波形图中观测结果
            #10;
        end

        // 循环结束后结束运行，推出仿真
        $finish;
    end
endmodule
```

## 实验要求

成功编译并仿真，并通过波形图来检验加法器工作正确。

提交代码和实验报告，实验报告中应包含表明结果正确的波形图截图。
