# partition_lines (Operator)

## Name

`partition_lines` — Partition lines according to various criteria.

## Warning

**`partition_lines` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def partition_lines(row_begin_in: Sequence[int], col_begin_in: Sequence[int], row_end_in: Sequence[int], col_end_in: Sequence[int], feature: MaybeSequence[str], operation: str, min: MaybeSequence[Union[int, float, str]], max: MaybeSequence[Union[int, float, str]]) -> Tuple[Sequence[int], Sequence[int], Sequence[int], Sequence[int], Sequence[int], Sequence[int], Sequence[int], Sequence[int]]`

## Description

The operator `partition_lines` divides lines into two sets
according to various criteria. For each input line the indicated
features (*`feature`*) are calculated. If each
(*`operation`* = *"and"*) or at least one
(*`operation`* = *"or"*) of the calculated features is within
the given limits (*`min`*,*`max`*) the line is
transferred into the first set (parameters *`row_begin_out`* to
*`col_end_out`*), otherwise into the second set (parameters
*`fail_row_bout`* to *`fail_col_eout`*).
The default values *"min"* and *"max"* of the parameters
*`min`* and *`max`* are used to leave bottom and top limit,
respectively, open.
$$\text{Condition:}Min_{i}\le Feature_{i}(Line)\le Max_{i}$$
Possible values for *`feature`*:

- **'length'** —

  (Euclidean) length of the line
- **'row'** —

  Line index of the center
- **'column'** —

  Column index of the center
- **'phi'** —

  Orientation of the line $\left(-\frac{\pi}{2} < \varphi \le \frac{\pi}{2}\right)$ ![figure](../assets/9c19d9d0a0968c31.svg)

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

List of values:
"column", "length", "phi", "row"

**`operation`** (input_control)  string `→` str

Desired combination of the features.

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
lines fulfilling the conditions.

**`col_begin_out`** (output_control)  line.begin.x-array `→` Sequence[int]

Column coordinates of the starting points of the
lines fulfilling the conditions.

**`row_end_out`** (output_control)  line.end.y-array `→` Sequence[int]

Row coordinates of the ending points of the
lines fulfilling the conditions.

**`col_end_out`** (output_control)  line.begin.x-array `→` Sequence[int]

Column coordinates of the ending points of the
lines fulfilling the conditions.

**`fail_row_bout`** (output_control)  line.begin.y-array `→` Sequence[int]

Row coordinates of the starting points of the
lines not fulfilling the conditions.

**`fail_col_bout`** (output_control)  line.begin.x-array `→` Sequence[int]

Column coordinates of the starting points of the
lines not fulfilling the conditions.

**`fail_row_eout`** (output_control)  line.end.y-array `→` Sequence[int]

Row coordinates of the ending points of the
lines not fulfilling the conditions.

**`fail_col_eout`** (output_control)  line.end.x-array `→` Sequence[int]

Column coordinates of the ending points of the
lines not fulfilling the conditions.

## Result

The operator `partition_lines` returns the value 2 (
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
`select_lines`,
`select_lines_longest`

## See also

`select_lines`,
`select_lines_longest`,
`detect_edge_segments`,
`select_shape`

## Module

Foundation
