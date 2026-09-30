# get_parallels_xld (Operator)

## Name

`get_parallels_xld` — Return an XLD parallel's data (as lines).

## Signature

`get_parallels_xld(Parallels : : : Row1, Col1, Length1, Phi1, Row2, Col2, Length2, Phi2)`

## Description

`get_parallels_xld` returns for the first XLD parallel in
*`Parallels`* the following values:

|  |  |
| --- | --- |
| *`Row1`*: | Row coordinates of the points on polygon P1 |
| *`Col1`*: | Column coordinates of the points on polygon P1 |
| *`Length1`*: | Lengths of the line segments on polygon P1 |
| *`Phi1`*: | Angles to the normal vectors of the line segments on polygon P1 |
| *`Row2`*: | Row coordinates of the points on polygon P2 |
| *`Col2`*: | Column coordinates of the points on polygon P2 |
| *`Length2`*: | Lengths of the line segments on polygon P2 |
| *`Phi2`*: | Angles to the normal vectors of the line segments on polygon P2 |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Parallels`** (input_object)  xld `→` object

Input XLD parallels.

**`Row1`** (output_control)  polygon.y-array `→`  (real)

Row coordinates of the points on polygon P1.

**`Col1`** (output_control)  polygon.x-array `→`  (real)

Column coordinates of the points on polygon P1.

**`Length1`** (output_control)  real-array `→`  (real)

Lengths of the line segments on polygon P1.

**`Phi1`** (output_control)  angle.rad-array `→`  (real)

Angles to the normal vectors of the line segments on polygon P1.

**`Row2`** (output_control)  polygon.y-array `→`  (real)

Row coordinates of the points on polygon P2.

**`Col2`** (output_control)  polygon.x-array `→`  (real)

Column coordinates of the points on polygon P2.

**`Length2`** (output_control)  real-array `→`  (real)

Lengths of the line segments on polygon P2.

**`Phi2`** (output_control)  angle.rad-array `→`  (real)

Angles to the normal vectors of the line segments on polygon P2.

## Possible Predecessors

`gen_parallels_xld`

## See also

`get_polygon_xld`,
`get_lines_xld`

## Module

Foundation
