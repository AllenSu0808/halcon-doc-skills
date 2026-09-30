# line_position (Operator)

## Name

`line_position` — Calculate the center of gravity, length, and orientation of a line.

## Signature

`def line_position(row_begin: MaybeSequence[Union[int, float]], col_begin: MaybeSequence[Union[int, float]], row_end: MaybeSequence[Union[int, float]], col_end: MaybeSequence[Union[int, float]]) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def line_position_s(row_begin: MaybeSequence[Union[int, float]], col_begin: MaybeSequence[Union[int, float]], row_end: MaybeSequence[Union[int, float]], col_end: MaybeSequence[Union[int, float]]) -> Tuple[float, float, float, float]`

## Description

The operator `line_position` returns the center
(*`row_center`*, *`col_center`*), the (Euclidean) length
(*`length`*) and the orientation (-pi/2 < *`phi`* <=
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

**`row_begin`** (input_control)  line.begin.y(-array) `→` MaybeSequence[Union[int, float]]

Row coordinates of the starting points of the
input lines.

**`col_begin`** (input_control)  line.begin.x(-array) `→` MaybeSequence[Union[int, float]]

Column coordinates of the starting points of the
input lines.

**`row_end`** (input_control)  line.end.y(-array) `→` MaybeSequence[Union[int, float]]

Row coordinates of the ending points of the
input lines.

**`col_end`** (input_control)  line.end.x(-array) `→` MaybeSequence[Union[int, float]]

Column coordinates of the ending points of the
input lines.

**`row_center`** (output_control)  point.y(-array) `→` Sequence[float]

Row coordinates of the centers of gravity of the
input lines.

**`col_center`** (output_control)  point.x(-array) `→` Sequence[float]

Column coordinates of the centers of gravity of the
input lines.

**`length`** (output_control)  real(-array) `→` Sequence[float]

Euclidean length of the input lines.

**`phi`** (output_control)  angle.rad(-array) `→` Sequence[float]

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
