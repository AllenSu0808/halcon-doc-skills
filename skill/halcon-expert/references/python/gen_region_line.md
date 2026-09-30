# gen_region_line (Operator)

## Name

`gen_region_line` — Store input lines as regions.

## Signature

`def gen_region_line(begin_row: MaybeSequence[Union[int, float]], begin_col: MaybeSequence[Union[int, float]], end_row: MaybeSequence[Union[int, float]], end_col: MaybeSequence[Union[int, float]]) -> HObject`

## Description

The operator `gen_region_line` stores the given lines (with starting
point [*`begin_row`*,*`begin_col`*] and ending point
[*`end_row`*, *`end_col`*]) as region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region_lines`** (output_object)  region(-array) `→` HObject

Created regions.

**`begin_row`** (input_control)  line.begin.y(-array) `→` MaybeSequence[Union[int, float]]

Line coordinates of the starting points of the input
lines.

Default:
100

Suggested values:
10, 50, 100, 200, 300, 400

Value range:
`begin_row` (lin)

Minimum increment:
1

Recommended increment:
1

**`begin_col`** (input_control)  line.begin.x(-array) `→` MaybeSequence[Union[int, float]]

Column coordinates of the starting points of the input
lines.

Default:
50

Suggested values:
10, 50, 100, 200, 300, 400

Value range:
`begin_col` (lin)

Minimum increment:
1

Recommended increment:
1

**`end_row`** (input_control)  line.end.y(-array) `→` MaybeSequence[Union[int, float]]

Line coordinates of the ending points of the input
lines.

Default:
150

Suggested values:
50, 100, 200, 300, 400, 500

Value range:
`end_row` (lin)

Minimum increment:
1

Recommended increment:
1

**`end_col`** (input_control)  line.end.x(-array) `→` MaybeSequence[Union[int, float]]

Column coordinates of the ending points of the
input lines.

Default:
250

Suggested values:
50, 100, 200, 300, 400, 500

Value range:
`end_col` (lin)

Minimum increment:
1

Recommended increment:
1

## Result

The operator `gen_region_line` always returns the value 2 (
H_MSG_TRUE)
.
The clipping according to the current image format is determined by the
operator `set_system('clip_region',<'true'/'false'>)`.

## Possible Predecessors

`split_skeleton_lines`

## Alternatives

`gen_region_hline`

## Module

Foundation
