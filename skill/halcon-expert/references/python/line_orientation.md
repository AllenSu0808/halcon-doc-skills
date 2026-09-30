# line_orientation (Operator)

## Name

`line_orientation` — Calculate the orientation of lines.

## Signature

`def line_orientation(row_begin: MaybeSequence[Union[int, float]], col_begin: MaybeSequence[Union[int, float]], row_end: MaybeSequence[Union[int, float]], col_end: MaybeSequence[Union[int, float]]) -> Sequence[float]`

`def line_orientation_s(row_begin: MaybeSequence[Union[int, float]], col_begin: MaybeSequence[Union[int, float]], row_end: MaybeSequence[Union[int, float]], col_end: MaybeSequence[Union[int, float]]) -> float`

## Description

The operator `line_orientation` returns the orientation
(-pi/2 < *`phi`* <= pi/2) of the given lines. If more
than one line is to be treated the line and column indices can be
passed as tuples. In this case *`phi`* is, of course, also
a tuple and contains the corresponding orientations.

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

**`phi`** (output_control)  angle.rad(-array) `→` Sequence[float]

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
