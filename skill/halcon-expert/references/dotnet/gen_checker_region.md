# GenCheckerRegion (Operator)

## Name

`GenCheckerRegion` — Create a checkered region.

## Signature

`static void HOperatorSet.GenCheckerRegion(out HObject regionChecker, HTuple widthRegion, HTuple heightRegion, HTuple widthPattern, HTuple heightPattern)`

`void HRegion.GenCheckerRegion(int widthRegion, int heightRegion, int widthPattern, int heightPattern)`

## Description

The operator `GenCheckerRegion` returns a checkered region.
Every black field of the checkerboard belongs to the region.
The horizontal and vertical expansion of the region is limited by
*`widthRegion`*, *`heightRegion`* respectively,
the size of the fields of the checkerboard by
*`widthPattern`* * *`heightPattern`*.

## Attention

If a very small pattern is chosen
(*`widthPattern`* < 4) the created region requires much storage.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regionChecker`** (output_object)  region `→` [HRegion](HRegion.md)

Created checkerboard region.

**`widthRegion`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Largest occurring x value of the region.

Default:
511

Suggested values:
10, 20, 31, 63, 127, 255, 300, 400, 511

Value range:
`1
≤
widthRegion` (lin)

Minimum increment:
1

Recommended increment:
10

**`heightRegion`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Largest occurring y value of the region.

Default:
511

Suggested values:
10, 20, 31, 63, 127, 255, 300, 400, 511

Value range:
`1
≤
heightRegion` (lin)

Minimum increment:
1

Recommended increment:
10

**`widthPattern`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of a field of the checkerboard.

Default:
64

Suggested values:
1, 2, 4, 8, 16, 20, 32, 64, 100, 128, 200, 300, 500

Value range:
`1
≤
widthPattern` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`WidthPattern < WidthRegion`

**`heightPattern`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of a field of the checkerboard.

Default:
64

Suggested values:
1, 2, 4, 8, 16, 20, 32, 64, 100, 128, 200, 300, 500

Value range:
`1
≤
heightPattern` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`HeightPattern < HeightRegion`

## Example (HDevelop)

```
gen_checker_region(Checker,512,512,32,64)
dev_set_draw('fill')
dev_display (Checker)
```

## Complexity

The required storage (in bytes) for the region is:

O((*`widthRegion`* * *`heightRegion`*) /
*`widthPattern`*)

## Result

The operator `GenCheckerRegion` returns the value 2 (
H_MSG_TRUE)
if the parameter values are correct.
Otherwise an exception is raised.
The clipping according to the current image format is set via the operator
`set_system('clip_region',<'true'/'false'>)`.

## Possible Successors

`PaintRegion`

## Alternatives

`GenGridRegion`,
`GenRegionPolygonFilled`,
`GenRegionPoints`,
`GenRegionRuns`,
`GenRectangle1`,
`ConcatObj`,
`GenRandomRegion`,
`GenRandomRegions`

## See also

`ReduceDomain`

## Module

Foundation
