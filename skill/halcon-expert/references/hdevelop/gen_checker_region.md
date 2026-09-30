# gen_checker_region (Operator)

## Name

`gen_checker_region` — Create a checkered region.

## Signature

`gen_checker_region( : RegionChecker : WidthRegion, HeightRegion, WidthPattern, HeightPattern : )`

## Description

The operator `gen_checker_region` returns a checkered region.
Every black field of the checkerboard belongs to the region.
The horizontal and vertical expansion of the region is limited by
*`WidthRegion`*, *`HeightRegion`* respectively,
the size of the fields of the checkerboard by
*`WidthPattern`* * *`HeightPattern`*.

## Attention

If a very small pattern is chosen
(*`WidthPattern`* < 4) the created region requires much storage.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`RegionChecker`** (output_object)  region `→` object

Created checkerboard region.

**`WidthRegion`** (input_control)  extent.x `→`  (integer)

Largest occurring x value of the region.

Default:
511

Suggested values:
10, 20, 31, 63, 127, 255, 300, 400, 511

Value range:
`1
≤
WidthRegion` (lin)

Minimum increment:
1

Recommended increment:
10

**`HeightRegion`** (input_control)  extent.y `→`  (integer)

Largest occurring y value of the region.

Default:
511

Suggested values:
10, 20, 31, 63, 127, 255, 300, 400, 511

Value range:
`1
≤
HeightRegion` (lin)

Minimum increment:
1

Recommended increment:
10

**`WidthPattern`** (input_control)  extent.x `→`  (integer)

Width of a field of the checkerboard.

Default:
64

Suggested values:
1, 2, 4, 8, 16, 20, 32, 64, 100, 128, 200, 300, 500

Value range:
`1
≤
WidthPattern` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`WidthPattern < WidthRegion`

**`HeightPattern`** (input_control)  extent.y `→`  (integer)

Height of a field of the checkerboard.

Default:
64

Suggested values:
1, 2, 4, 8, 16, 20, 32, 64, 100, 128, 200, 300, 500

Value range:
`1
≤
HeightPattern` (lin)

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

O((*`WidthRegion`* * *`HeightRegion`*) /
*`WidthPattern`*)

## Result

The operator `gen_checker_region` returns the value 2 (
H_MSG_TRUE)
if the parameter values are correct.
Otherwise an exception is raised.
The clipping according to the current image format is set via the operator
`set_system('clip_region',<'true'/'false'>)`.

## Possible Successors

`paint_region`

## Alternatives

`gen_grid_region`,
`gen_region_polygon_filled`,
`gen_region_points`,
`gen_region_runs`,
`gen_rectangle1`,
`concat_obj`,
`gen_random_region`,
`gen_random_regions`

## See also

`reduce_domain`

## Module

Foundation
