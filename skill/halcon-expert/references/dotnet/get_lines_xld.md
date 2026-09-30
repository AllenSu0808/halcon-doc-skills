# GetLinesXld (Operator)

## Name

`GetLinesXld` — Return an XLD polygon's data (as lines).

## Signature

`static void HOperatorSet.GetLinesXld(HObject polygon, out HTuple beginRow, out HTuple beginCol, out HTuple endRow, out HTuple endCol, out HTuple length, out HTuple phi)`

`void HXLDPoly.GetLinesXld(out HTuple beginRow, out HTuple beginCol, out HTuple endRow, out HTuple endCol, out HTuple length, out HTuple phi)`

## Description

`GetLinesXld` returns the XLD polygon *`polygon`*
as a set of lines. The following values are returned:

|  |  |
| --- | --- |
| *`beginRow`*: | Rows coordinates of the lines' start points |
| *`beginCol`*: | Columns coordinates of the lines' start points |
| *`endRow`*: | Row coordinates of the lines' end points |
| *`endCol`*: | Column coordinates of the lines' end points |
| *`length`*: | Lengths of the line segments |
| *`phi`*: | Angles to the normal vectors of the line segments |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`polygon`** (input_object)  xld_poly(-array) `→` [HXLDPoly](HXLDPoly.md)

Input XLD polygons.

**`beginRow`** (output_control)  line.begin.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the lines' start points.

**`beginCol`** (output_control)  line.begin.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the lines' start points.

**`endRow`** (output_control)  line.end.y-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the lines' end points.

**`endCol`** (output_control)  line.end.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the lines' end points.

**`length`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Lengths of the line segments.

**`phi`** (output_control)  angle.rad-array `→` [HTuple](HTuple.md) (*double*)

Angles to the normal vectors of the line segments.

## Possible Predecessors

`GenPolygonsXld`

## Alternatives

`GetPolygonXld`

## Module

Foundation
