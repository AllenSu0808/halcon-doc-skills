# get_polygon_xld (Operator)

## Name

`get_polygon_xld` — Return an XLD polygon's data.

## Signature

`get_polygon_xld(Polygon : : : Row, Col, Length, Phi)`

## Description

`get_polygon_xld` returns the following values of the XLD
polygon *`Polygon`*:

|  |  |
| --- | --- |
| *`Row`* | Row coordinates of the polygons' points |
| *`Col`* | Column coordinates of the polygons' points |
| *`Length`* | Lengths of the line segments between points i and i+1, respectively |
| *`Phi`* | Angles to the normal vectors of the line segments between points i and i+1, respectively |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Polygon`** (input_object)  xld_poly `→` object

Input XLD polygon.

**`Row`** (output_control)  point.y-array `→`  (real)

Row coordinates of the polygons' points.

**`Col`** (output_control)  point.x-array `→`  (real)

Column coordinates of the polygons' points.

**`Length`** (output_control)  real-array `→`  (real)

Lengths of the line segments.

**`Phi`** (output_control)  angle.rad-array `→`  (real)

Angles to the normal vectors of the line segments.

## Possible Predecessors

`gen_polygons_xld`

## Alternatives

`get_lines_xld`

## Module

Foundation
