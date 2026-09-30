# GenStructElements (Operator)

## Name

`GenStructElements` — Generate standard structuring elements.

## Warning

**`GenStructElements` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.GenStructElements(out HObject structElements, HTuple type, HTuple row, HTuple column)`

`void HRegion.GenStructElements(string type, int row, int column)`

## Description

`GenStructElements` serves to generate eight structuring
elements normally used in the operator [`Fitting`](fitting.md). The
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

**`structElements`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Generated structuring elements.

**`type`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of structuring element to generate.

Default:
"noise"

List of values:
"noise"

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Row coordinate of the reference point.

Default:
1

Suggested values:
0, 1, 10, 50, 100, 200, 300, 400

Value range:
`row` (lin)

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

Column coordinate of the reference point.

Default:
1

Suggested values:
0, 1, 10, 50, 100, 200, 300, 400

Value range:
`column` (lin)

## Result

`GenStructElements` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
Otherwise, an exception is raised.

## Possible Successors

`Fitting`,
`HitOrMiss`,
`Opening`,
`Closing`,
`Erosion2`,
`Dilation2`

## See also

`GolayElements`

## Module

Foundation
