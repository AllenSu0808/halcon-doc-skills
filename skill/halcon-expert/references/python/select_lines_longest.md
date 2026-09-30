# select_lines_longest (Operator)

## Name

`select_lines_longest` — Select the longest input lines.

## Warning

**`select_lines_longest` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def select_lines_longest(row_begin_in: Sequence[int], col_begin_in: Sequence[int], row_end_in: Sequence[int], col_end_in: Sequence[int], num: int) -> Tuple[Sequence[int], Sequence[int], Sequence[int], Sequence[int]]`

## Description

The operator `select_lines_longest` selects the
*`num`* longest input lines from the input lines described by
the tuples *`row_begin_in`*, *`col_begin_in`*,
*`row_end_in`* and *`col_end_in`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`row_begin_in`** (input_control)  line.begin.y-array `→` Sequence[int]

Row coordinates of the starting points of the
input lines.

**`col_begin_in`** (input_control)  line.begin.x-array `→` Sequence[int]

Column coordinates of the starting points of the
input lines.

**`row_end_in`** (input_control)  line.end.y-array `→` Sequence[int]

Row coordinates of the ending points of the
input lines.

**`col_end_in`** (input_control)  line.end.x-array `→` Sequence[int]

Column coordinates of the ending points of the
input lines.

**`num`** (input_control)  integer `→` int

(Maximum) desired number of output lines.

Default:
10

**`row_begin_out`** (output_control)  line.begin.y-array `→` Sequence[int]

Row coordinates of the starting points of the
output lines.

**`col_begin_out`** (output_control)  line.begin.x-array `→` Sequence[int]

Column coordinates of the starting points of the
output lines.

**`row_end_out`** (output_control)  line.end.y-array `→` Sequence[int]

Row coordinates of the ending points of the
output lines.

**`col_end_out`** (output_control)  line.end.x-array `→` Sequence[int]

Column coordinates of the ending points of the
output lines.

## Result

The operator `select_lines_longest` returns the value 2 (
H_MSG_TRUE)
if the parameter values are correct. Otherwise an exception is
raised.

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

`line_orientation`,
`line_position`,
`select_lines`,
`partition_lines`

## See also

`select_lines`,
`partition_lines`,
`detect_edge_segments`,
`select_shape`

## Module

Foundation
