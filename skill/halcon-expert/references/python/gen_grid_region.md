# gen_grid_region (Operator)

## Name

`gen_grid_region` — Create a region from lines or pixels.

## Signature

`def gen_grid_region(row_steps: Union[float, int], column_steps: Union[float, int], type: str, width: int, height: int) -> HObject`

## Description

The operator `gen_grid_region` creates a grid constructed
of lines (*`type`* = 'lines') or pixels
(*`type`* = 'points').
In case of 'lines' continuous lines are returned, in case of
'points' only the intersections of the lines.
Starting from the pixel (0,0) to the pixel
(*`height`*-1,*`width`*-1) the grid is
built up at stepping width *`row_steps`* in row
direction and *`column_steps`* in column direction.
The step widths have to be greater than *1*.
Exceptions are in 'lines' mode *`row_steps`*, where
*`row_steps`* or *`column_steps`* can be set equal to *0*.
In such a case, only columns, rows respectively, are created.

## Attention

If a very small pattern is chosen
(*`row_steps`* < 4 or *`column_steps`*
< 4) the created region requires much storage.

In the 'points' mode *`row_steps`* and
*`column_steps`* must not be set to zero.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region_grid`** (output_object)  region `→` HObject

Created lines/pixel region.

**`row_steps`** (input_control)  extent.y `→` Union[float, int]

Step width in line direction or zero.

Default:
10

Suggested values:
0, 2, 3, 4, 5, 7, 10, 15, 20, 30, 50, 100

Value range:
`row_steps` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`RowSteps > 1 || RowSteps == 0`

**`column_steps`** (input_control)  extent.x `→` Union[float, int]

Step width in column direction or zero.

Default:
10

Suggested values:
0, 2, 3, 4, 5, 7, 10, 15, 20, 30, 50, 100

Value range:
`column_steps` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`ColumnSteps > 1 || ColumnSteps == 0`

**`type`** (input_control)  string `→` str

Type of created pattern.

Default:
"lines"

List of values:
"lines", "points"

**`width`** (input_control)  extent.x `→` int

Maximum width of pattern.

Default:
512

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
width` (lin)

Minimum increment:
1

Recommended increment:
10

**`height`** (input_control)  extent.y `→` int

Maximum height of pattern.

Default:
512

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
height` (lin)

Minimum increment:
1

Recommended increment:
10

## Complexity

The necessary storage (in bytes) for the region is:

O((ImageWidth / ColumnSteps) * (ImageHeight / RowSteps))

## Result

If the parameter values are correct the operator `gen_grid_region`
returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.
The clipping according to the current image format is set via the operator
`set_system('clip_region',<'true'/'false'>)`.

## Possible Successors

`reduce_domain`,
`paint_region`

## Alternatives

`gen_region_line`,
`gen_region_polygon`,
`gen_region_points`,
`gen_region_runs`

## See also

`gen_checker_region`,
`reduce_domain`

## Module

Foundation
