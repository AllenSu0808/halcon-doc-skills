# get_lines_xld (Operator)

## Name

`get_lines_xld` — Return an XLD polygon's data (as lines).

## Signature

`def get_lines_xld(polygon: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

## Description

`get_lines_xld` returns the XLD polygon *`polygon`*
as a set of lines. The following values are returned:

|  |  |
| --- | --- |
| *`begin_row`*: | Rows coordinates of the lines' start points |
| *`begin_col`*: | Columns coordinates of the lines' start points |
| *`end_row`*: | Row coordinates of the lines' end points |
| *`end_col`*: | Column coordinates of the lines' end points |
| *`length`*: | Lengths of the line segments |
| *`phi`*: | Angles to the normal vectors of the line segments |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`polygon`** (input_object)  xld_poly(-array) `→` HObject

Input XLD polygons.

**`begin_row`** (output_control)  line.begin.y-array `→` Sequence[float]

Row coordinates of the lines' start points.

**`begin_col`** (output_control)  line.begin.x-array `→` Sequence[float]

Column coordinates of the lines' start points.

**`end_row`** (output_control)  line.end.y-array `→` Sequence[float]

Column coordinates of the lines' end points.

**`end_col`** (output_control)  line.end.x-array `→` Sequence[float]

Column coordinates of the lines' end points.

**`length`** (output_control)  real-array `→` Sequence[float]

Lengths of the line segments.

**`phi`** (output_control)  angle.rad-array `→` Sequence[float]

Angles to the normal vectors of the line segments.

## Possible Predecessors

`gen_polygons_xld`

## Alternatives

`get_polygon_xld`

## Module

Foundation
