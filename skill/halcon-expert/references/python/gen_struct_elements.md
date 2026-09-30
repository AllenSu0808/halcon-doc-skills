# gen_struct_elements (Operator)

## Name

`gen_struct_elements` — Generate standard structuring elements.

## Warning

**`gen_struct_elements` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def gen_struct_elements(type: str, row: int, column: int) -> HObject`

## Description

`gen_struct_elements` serves to generate eight structuring
elements normally used in the operator [`fitting`](fitting.md). The
default value *"noise"* of the parameter *`type`*
generates elements especially suited for the elimination of noise.
o o o o * o o o * * o o o o o o o o o * o o * o
* * * o * o o * o o * o * * o o * * * * o o * *
o o o o * o * o o o o * o * o o * o o o o o o o
M1 M2 M3 M4 M5 M6 M7 M8

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`struct_elements`** (output_object)  region(-array) `→` HObject

Generated structuring elements.

**`type`** (input_control)  string `→` str

Type of structuring element to generate.

Default:
"noise"

List of values:
"noise"

**`row`** (input_control)  point.y `→` int

Row coordinate of the reference point.

Default:
1

Suggested values:
0, 1, 10, 50, 100, 200, 300, 400

Value range:
`row` (lin)

**`column`** (input_control)  point.x `→` int

Column coordinate of the reference point.

Default:
1

Suggested values:
0, 1, 10, 50, 100, 200, 300, 400

Value range:
`column` (lin)

## Result

`gen_struct_elements` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
Otherwise, an exception is raised.

## Possible Successors

`fitting`,
`hit_or_miss`,
`opening`,
`closing`,
`erosion2`,
`dilation2`

## See also

`golay_elements`

## Module

Foundation
