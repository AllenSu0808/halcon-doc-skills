# select_lines (Operator)

## Name

`select_lines` — Select lines according to various criteria.

## Warning

**`select_lines` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def select_lines(row_begin_in: Sequence[int], col_begin_in: Sequence[int], row_end_in: Sequence[int], col_end_in: Sequence[int], feature: MaybeSequence[str], operation: str, min: MaybeSequence[Union[int, float, str]], max: MaybeSequence[Union[int, float, str]]) -> Tuple[Sequence[int], Sequence[int], Sequence[int], Sequence[int]]`

## Description

The operator `select_lines` chooses lines according to
various criteria. For every input line the indicated features
(*`feature`*) are calculated. If each
(*`operation`* = *"and"*) or at least one
(*`operation`* = *"or"*) of the calculated features is within
the given limits (*`min`*,*`max`*) the line is
transferred into the output.
The default values *"min"* and *"max"* of the parameters
*`min`* and *`max`* are used to leave bottom and top limits,
respectively, open.

Condition:
$$Min_{i}\le Feature_{i}(Line)\le Max_{i}$$

Possible values for *`feature`*:

- ***"length"*** —

  (Euclidean) length of the line
- ***"row"*** —

  Line index of the center
- ***"column"*** —

  Column index of the center
- ***"phi"*** —

  Orientation of the line
  ($-\frac{\pi}{2} < \varphi \le \frac{\pi}{2}$ ![figure](../assets/a9d6b4537501996b.svg))

## Attention

If only one feature is used the value of *`operation`* is
meaningless. Several features are processed according to the
sequence in which they are passed.

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

**`feature`** (input_control)  string(-array) `→` MaybeSequence[str]

Features to be used for selection.

Default:
"length"

List of values:
"column", "length", "phi", "row"

**`operation`** (input_control)  string `→` str

Desired combination of the features.

Default:
"and"

List of values:
"and", "or"

**`min`** (input_control)  string(-array) `→` MaybeSequence[Union[int, float, str]]

Lower limits of the features or 'min'.

Default:
"min"

**`max`** (input_control)  string(-array) `→` MaybeSequence[Union[int, float, str]]

Upper limits of the features or 'max'.

Default:
"max"

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
