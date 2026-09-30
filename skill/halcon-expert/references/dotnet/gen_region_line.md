# GenRegionLine (Operator)

## Name

`GenRegionLine` — Store input lines as regions.

## Signature

`static void HOperatorSet.GenRegionLine(out HObject regionLines, HTuple beginRow, HTuple beginCol, HTuple endRow, HTuple endCol)`

`void HRegion.GenRegionLine(HTuple beginRow, HTuple beginCol, HTuple endRow, HTuple endCol)`

`void HRegion.GenRegionLine(int beginRow, int beginCol, int endRow, int endCol)`

## Description

The operator `GenRegionLine` stores the given lines (with starting
point [*`beginRow`*,*`beginCol`*] and ending point
[*`endRow`*, *`endCol`*]) as region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regionLines`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Created regions.

**`beginRow`** (input_control)  line.begin.y(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Line coordinates of the starting points of the input
lines.

Default:
100

Suggested values:
10, 50, 100, 200, 300, 400

Value range:
`beginRow` (lin)

Minimum increment:
1

Recommended increment:
1

**`beginCol`** (input_control)  line.begin.x(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Column coordinates of the starting points of the input
lines.

Default:
50

Suggested values:
10, 50, 100, 200, 300, 400

Value range:
`beginCol` (lin)

Minimum increment:
1

Recommended increment:
1

**`endRow`** (input_control)  line.end.y(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Line coordinates of the ending points of the input
lines.

Default:
150

Suggested values:
50, 100, 200, 300, 400, 500

Value range:
`endRow` (lin)

Minimum increment:
1

Recommended increment:
1

**`endCol`** (input_control)  line.end.x(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Column coordinates of the ending points of the
input lines.

Default:
250

Suggested values:
50, 100, 200, 300, 400, 500

Value range:
`endCol` (lin)

Minimum increment:
1

Recommended increment:
1

## Result

The operator `GenRegionLine` always returns the value 2 (
H_MSG_TRUE)
.
The clipping according to the current image format is determined by the
operator `set_system('clip_region',<'true'/'false'>)`.

## Possible Predecessors

`SplitSkeletonLines`

## Alternatives

`GenRegionHline`

## Module

Foundation
