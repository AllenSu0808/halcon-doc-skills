# select_lines_longest (Operator)

## Name

`select_lines_longest` — Select the longest input lines.

## Warning

**`select_lines_longest` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`select_lines_longest( : : RowBeginIn, ColBeginIn, RowEndIn, ColEndIn, Num : RowBeginOut, ColBeginOut, RowEndOut, ColEndOut)`

## Description

The operator `select_lines_longest` selects the
*`Num`* longest input lines from the input lines described by
the tuples *`RowBeginIn`*, *`ColBeginIn`*,
*`RowEndIn`* and *`ColEndIn`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`RowBeginIn`** (input_control)  line.begin.y-array `→`  (integer)

Row coordinates of the starting points of the
input lines.

**`ColBeginIn`** (input_control)  line.begin.x-array `→`  (integer)

Column coordinates of the starting points of the
input lines.

**`RowEndIn`** (input_control)  line.end.y-array `→`  (integer)

Row coordinates of the ending points of the
input lines.

**`ColEndIn`** (input_control)  line.end.x-array `→`  (integer)

Column coordinates of the ending points of the
input lines.

**`Num`** (input_control)  integer `→`  (integer)

(Maximum) desired number of output lines.

Default:
10

**`RowBeginOut`** (output_control)  line.begin.y-array `→`  (integer)

Row coordinates of the starting points of the
output lines.

**`ColBeginOut`** (output_control)  line.begin.x-array `→`  (integer)

Column coordinates of the starting points of the
output lines.

**`RowEndOut`** (output_control)  line.end.y-array `→`  (integer)

Row coordinates of the ending points of the
output lines.

**`ColEndOut`** (output_control)  line.end.x-array `→`  (integer)

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
