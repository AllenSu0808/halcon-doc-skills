# get_parallels_xld (Operator)

## Name

`get_parallels_xld` — Return an XLD parallel's data (as lines).

## Signature

`def get_parallels_xld(parallels: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

## Description

`get_parallels_xld` returns for the first XLD parallel in
*`parallels`* the following values:

|  |  |
| --- | --- |
| *`row_1`*: | Row coordinates of the points on polygon P1 |
| *`col_1`*: | Column coordinates of the points on polygon P1 |
| *`length_1`*: | Lengths of the line segments on polygon P1 |
| *`phi_1`*: | Angles to the normal vectors of the line segments on polygon P1 |
| *`row_2`*: | Row coordinates of the points on polygon P2 |
| *`col_2`*: | Column coordinates of the points on polygon P2 |
| *`length_2`*: | Lengths of the line segments on polygon P2 |
| *`phi_2`*: | Angles to the normal vectors of the line segments on polygon P2 |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`parallels`** (input_object)  xld `→` HObject

Input XLD parallels.

**`row_1`** (output_control)  polygon.y-array `→` Sequence[float]

Row coordinates of the points on polygon P1.

**`col_1`** (output_control)  polygon.x-array `→` Sequence[float]

Column coordinates of the points on polygon P1.

**`length_1`** (output_control)  real-array `→` Sequence[float]

Lengths of the line segments on polygon P1.

**`phi_1`** (output_control)  angle.rad-array `→` Sequence[float]

Angles to the normal vectors of the line segments on polygon P1.

**`row_2`** (output_control)  polygon.y-array `→` Sequence[float]

Row coordinates of the points on polygon P2.

**`col_2`** (output_control)  polygon.x-array `→` Sequence[float]

Column coordinates of the points on polygon P2.

**`length_2`** (output_control)  real-array `→` Sequence[float]

Lengths of the line segments on polygon P2.

**`phi_2`** (output_control)  angle.rad-array `→` Sequence[float]

Angles to the normal vectors of the line segments on polygon P2.

## Possible Predecessors

`gen_parallels_xld`

## See also

`get_polygon_xld`,
`get_lines_xld`

## Module

Foundation
