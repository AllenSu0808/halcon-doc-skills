# get_polygon_xld (Operator)

## Name

`get_polygon_xld` — Return an XLD polygon's data.

## Signature

`def get_polygon_xld(polygon: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

## Description

`get_polygon_xld` returns the following values of the XLD
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

**`polygon`** (input_object)  xld_poly `→` HObject

Input XLD polygon.

**`row`** (output_control)  point.y-array `→` Sequence[float]

Row coordinates of the polygons' points.

**`col`** (output_control)  point.x-array `→` Sequence[float]

Column coordinates of the polygons' points.

**`length`** (output_control)  real-array `→` Sequence[float]

Lengths of the line segments.

**`phi`** (output_control)  angle.rad-array `→` Sequence[float]

Angles to the normal vectors of the line segments.

## Possible Predecessors

`gen_polygons_xld`

## Alternatives

`get_lines_xld`

## Module

Foundation
