# GetParallelsXld (Operator)

## Name

`GetParallelsXld` — Return an XLD parallel's data (as lines).

## Signature

`static void HOperatorSet.GetParallelsXld(HObject parallels, out HTuple row1, out HTuple col1, out HTuple length1, out HTuple phi1, out HTuple row2, out HTuple col2, out HTuple length2, out HTuple phi2)`

`void HXLD.GetParallelsXld(out HTuple row1, out HTuple col1, out HTuple length1, out HTuple phi1, out HTuple row2, out HTuple col2, out HTuple length2, out HTuple phi2)`

## Description

`GetParallelsXld` returns for the first XLD parallel in
*`parallels`* the following values:

|  |  |
| --- | --- |
| *`row1`*: | Row coordinates of the points on polygon P1 |
| *`col1`*: | Column coordinates of the points on polygon P1 |
| *`length1`*: | Lengths of the line segments on polygon P1 |
| *`phi1`*: | Angles to the normal vectors of the line segments on polygon P1 |
| *`row2`*: | Row coordinates of the points on polygon P2 |
| *`col2`*: | Column coordinates of the points on polygon P2 |
| *`length2`*: | Lengths of the line segments on polygon P2 |
| *`phi2`*: | Angles to the normal vectors of the line segments on polygon P2 |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`parallels`** (input_object)  xld `→` [HXLD](HXLD.md)

Input XLD parallels.

**`row1`** (output_control)  polygon.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the points on polygon P1.

**`col1`** (output_control)  polygon.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the points on polygon P1.

**`length1`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Lengths of the line segments on polygon P1.

**`phi1`** (output_control)  angle.rad-array `→` [HTuple](HTuple.md) (*double*)

Angles to the normal vectors of the line segments on polygon P1.

**`row2`** (output_control)  polygon.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the points on polygon P2.

**`col2`** (output_control)  polygon.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the points on polygon P2.

**`length2`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Lengths of the line segments on polygon P2.

**`phi2`** (output_control)  angle.rad-array `→` [HTuple](HTuple.md) (*double*)

Angles to the normal vectors of the line segments on polygon P2.

## Possible Predecessors

`GenParallelsXld`

## See also

`GetPolygonXld`,
`GetLinesXld`

## Module

Foundation
