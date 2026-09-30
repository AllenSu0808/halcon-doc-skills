# get_lines_xld (Operator)

## Name

`get_lines_xld` — Return an XLD polygon's data (as lines).

## Signature

`get_lines_xld(Polygon : : : BeginRow, BeginCol, EndRow, EndCol, Length, Phi)`

## Description

`get_lines_xld` returns the XLD polygon *`Polygon`*
as a set of lines. The following values are returned:

|  |  |
| --- | --- |
| *`BeginRow`*: | Rows coordinates of the lines' start points |
| *`BeginCol`*: | Columns coordinates of the lines' start points |
| *`EndRow`*: | Row coordinates of the lines' end points |
| *`EndCol`*: | Column coordinates of the lines' end points |
| *`Length`*: | Lengths of the line segments |
| *`Phi`*: | Angles to the normal vectors of the line segments |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Polygon`** (input_object)  xld_poly(-array) `→` object

Input XLD polygons.

**`BeginRow`** (output_control)  line.begin.y-array `→`  (real)

Row coordinates of the lines' start points.

**`BeginCol`** (output_control)  line.begin.x-array `→`  (real)

Column coordinates of the lines' start points.

**`EndRow`** (output_control)  line.end.y-array `→`  (real)

Column coordinates of the lines' end points.

**`EndCol`** (output_control)  line.end.x-array `→`  (real)

Column coordinates of the lines' end points.

**`Length`** (output_control)  real-array `→`  (real)

Lengths of the line segments.

**`Phi`** (output_control)  angle.rad-array `→`  (real)

Angles to the normal vectors of the line segments.

## Possible Predecessors

`gen_polygons_xld`

## Alternatives

`get_polygon_xld`

## Module

Foundation
