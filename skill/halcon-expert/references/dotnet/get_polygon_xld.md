# GetPolygonXld (Operator)

## Name

`GetPolygonXld` — Return an XLD polygon's data.

## Signature

`static void HOperatorSet.GetPolygonXld(HObject polygon, out HTuple row, out HTuple col, out HTuple length, out HTuple phi)`

`void HXLDPoly.GetPolygonXld(out HTuple row, out HTuple col, out HTuple length, out HTuple phi)`

## Description

`GetPolygonXld` returns the following values of the XLD
polygon *`polygon`*:

|  |  |
| --- | --- |
| *`row`* | Row coordinates of the polygons' points |
| *`col`* | Column coordinates of the polygons' points |
| *`length`* | Lengths of the line segments between points i and i+1, respectively |
| *`phi`* | Angles to the normal vectors of the line segments between points i and i+1, respectively |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`polygon`** (input_object)  xld_poly `→` [HXLDPoly](HXLDPoly.md)

Input XLD polygon.

**`row`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the polygons' points.

**`col`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the polygons' points.

**`length`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Lengths of the line segments.

**`phi`** (output_control)  angle.rad-array `→` [HTuple](HTuple.md) (*double*)

Angles to the normal vectors of the line segments.

## Possible Predecessors

`GenPolygonsXld`

## Alternatives

`GetLinesXld`

## Module

Foundation
