# line_orientation (Operator)

## Name

`line_orientation` — Calculate the orientation of lines.

## Signature

`line_orientation( : : RowBegin, ColBegin, RowEnd, ColEnd : Phi)`

## Description

The operator `line_orientation` returns the orientation
(-pi/2 < *`Phi`* <= pi/2) of the given lines. If more
than one line is to be treated the line and column indices can be
passed as tuples. In this case *`Phi`* is, of course, also
a tuple and contains the corresponding orientations.

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

**`Phi`** (output_control)  angle.rad(-array) `→`  (real)

Orientation of the input lines.

## Result

`line_orientation` always returns the value 2 (
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

`line_position`

## See also

`line_position`,
`detect_edge_segments`

## Module

Foundation
