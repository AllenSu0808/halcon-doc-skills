# select_lines (Operator)

## Name

`select_lines` — Select lines according to various criteria.

## Warning

**`select_lines` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`select_lines( : : RowBeginIn, ColBeginIn, RowEndIn, ColEndIn, Feature, Operation, Min, Max : RowBeginOut, ColBeginOut, RowEndOut, ColEndOut)`

## Description

The operator `select_lines` chooses lines according to
various criteria. For every input line the indicated features
(*`Feature`*) are calculated. If each
(*`Operation`* = *'and'*) or at least one
(*`Operation`* = *'or'*) of the calculated features is within
the given limits (*`Min`*,*`Max`*) the line is
transferred into the output.
The default values *'min'* and *'max'* of the parameters
*`Min`* and *`Max`* are used to leave bottom and top limits,
respectively, open.

Condition:
$$Min_{i}\le Feature_{i}(Line)\le Max_{i}$$

Possible values for *`Feature`*:

- ***'length'*** —

  (Euclidean) length of the line
- ***'row'*** —

  Line index of the center
- ***'column'*** —

  Column index of the center
- ***'phi'*** —

  Orientation of the line
  ($-\frac{\pi}{2} < \varphi \le \frac{\pi}{2}$ ![figure](../assets/a9d6b4537501996b.svg))

## Attention

If only one feature is used the value of *`Operation`* is
meaningless. Several features are processed according to the
sequence in which they are passed.

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

**`Feature`** (input_control)  string(-array) `→`  (string)

Features to be used for selection.

Default:
'length'

List of values:
'column', 'length', 'phi', 'row'

**`Operation`** (input_control)  string `→`  (string)

Desired combination of the features.

Default:
'and'

List of values:
'and', 'or'

**`Min`** (input_control)  string(-array) `→`  (string / integer / real)

Lower limits of the features or 'min'.

Default:
'min'

**`Max`** (input_control)  string(-array) `→`  (string / integer / real)

Upper limits of the features or 'max'.

Default:
'max'

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

The operator `select_lines` returns the value 2 (
H_MSG_TRUE)
if the
parameter values are correct. Otherwise an exception is raised.

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
`partition_lines`

## See also

`partition_lines`,
`select_lines_longest`,
`detect_edge_segments`,
`select_shape`

## Module

Foundation
