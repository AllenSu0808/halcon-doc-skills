# gen_region_line (Operator)

## Name

`gen_region_line` — Store input lines as regions.

## Signature

`gen_region_line( : RegionLines : BeginRow, BeginCol, EndRow, EndCol : )`

## Description

The operator `gen_region_line` stores the given lines (with starting
point [*`BeginRow`*,*`BeginCol`*] and ending point
[*`EndRow`*, *`EndCol`*]) as region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`RegionLines`** (output_object)  region(-array) `→` object

Created regions.

**`BeginRow`** (input_control)  line.begin.y(-array) `→`  (integer / real)

Line coordinates of the starting points of the input
lines.

Default:
100

Suggested values:
10, 50, 100, 200, 300, 400

Value range:
`BeginRow` (lin)

Minimum increment:
1

Recommended increment:
1

**`BeginCol`** (input_control)  line.begin.x(-array) `→`  (integer / real)

Column coordinates of the starting points of the input
lines.

Default:
50

Suggested values:
10, 50, 100, 200, 300, 400

Value range:
`BeginCol` (lin)

Minimum increment:
1

Recommended increment:
1

**`EndRow`** (input_control)  line.end.y(-array) `→`  (integer / real)

Line coordinates of the ending points of the input
lines.

Default:
150

Suggested values:
50, 100, 200, 300, 400, 500

Value range:
`EndRow` (lin)

Minimum increment:
1

Recommended increment:
1

**`EndCol`** (input_control)  line.end.x(-array) `→`  (integer / real)

Column coordinates of the ending points of the
input lines.

Default:
250

Suggested values:
50, 100, 200, 300, 400, 500

Value range:
`EndCol` (lin)

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
