# line_position (Operator)

## Name

`line_position` — Calculate the center of gravity, length, and orientation of a line.

## Signature

`line_position( : : RowBegin, ColBegin, RowEnd, ColEnd : RowCenter, ColCenter, Length, Phi)`

## Description

The operator `line_position` returns the center
(*`RowCenter`*, *`ColCenter`*), the (Euclidean) length
(*`Length`*) and the orientation (-pi/2 < *`Phi`* <=
pi/2)
of the given lines. If more than one line is to be treated the line
and column indices can be passed as tuples. In this case the output
parameters, of course, are also tuples.

The routine is applied, for example, to model lines in order to
determine search regions for the edge detection
([`detect_edge_segments`](detect_edge_segments.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`RowBegin`** (input_control)  line.begin.y(-array) `→`  (real / integer)

Row coordinates of the starting points of the
input lines.

**`ColBegin`** (input_control)  line.begin.x(-array) `→`  (real / integer)

Column coordinates of the starting points of the
input lines.

**`RowEnd`** (input_control)  line.end.y(-array) `→`  (real / integer)

Row coordinates of the ending points of the
input lines.

**`ColEnd`** (input_control)  line.end.x(-array) `→`  (real / integer)

Column coordinates of the ending points of the
input lines.

**`RowCenter`** (output_control)  point.y(-array) `→`  (real)

Row coordinates of the centers of gravity of the
input lines.

**`ColCenter`** (output_control)  point.x(-array) `→`  (real)

Column coordinates of the centers of gravity of the
input lines.

**`Length`** (output_control)  real(-array) `→`  (real)

Euclidean length of the input lines.

**`Phi`** (output_control)  angle.rad(-array) `→`  (real)

Orientation of the input lines.

## Result

`line_position` always returns the value 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`sobel_amp`,
`edges_image`,
`threshold`,
`hysteresis_threshold`,
`split_skeleton_region`,
`split_skeleton_lines`

## Possible Successors

`set_line_width`,
`disp_line`

## Alternatives

`line_orientation`

## See also

`line_orientation`,
`detect_edge_segments`

## Module

Foundation
