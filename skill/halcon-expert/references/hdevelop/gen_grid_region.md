# gen_grid_region (Operator)

## Name

`gen_grid_region` — Create a region from lines or pixels.

## Signature

`gen_grid_region( : RegionGrid : RowSteps, ColumnSteps, Type, Width, Height : )`

## Description

The operator `gen_grid_region` creates a grid constructed
of lines (*`Type`* = 'lines') or pixels
(*`Type`* = 'points').
In case of 'lines' continuous lines are returned, in case of
'points' only the intersections of the lines.
Starting from the pixel (0,0) to the pixel
(*`Height`*-1,*`Width`*-1) the grid is
built up at stepping width *`RowSteps`* in row
direction and *`ColumnSteps`* in column direction.
The step widths have to be greater than *1*.
Exceptions are in 'lines' mode *`RowSteps`*, where
*`RowSteps`* or *`ColumnSteps`* can be set equal to *0*.
In such a case, only columns, rows respectively, are created.

## Attention

If a very small pattern is chosen
(*`RowSteps`* < 4 or *`ColumnSteps`*
< 4) the created region requires much storage.

In the 'points' mode *`RowSteps`* and
*`ColumnSteps`* must not be set to zero.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`RegionGrid`** (output_object)  region `→` object

Created lines/pixel region.

**`RowSteps`** (input_control)  extent.y `→`  (integer / real)

Step width in line direction or zero.

Default:
10

Suggested values:
0, 2, 3, 4, 5, 7, 10, 15, 20, 30, 50, 100

Value range:
`RowSteps` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`RowSteps > 1 || RowSteps == 0`

**`ColumnSteps`** (input_control)  extent.x `→`  (integer / real)

Step width in column direction or zero.

Default:
10

Suggested values:
0, 2, 3, 4, 5, 7, 10, 15, 20, 30, 50, 100

Value range:
`ColumnSteps` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`ColumnSteps > 1 || ColumnSteps == 0`

**`Type`** (input_control)  string `→`  (string)

Type of created pattern.

Default:
'lines'

List of values:
'lines', 'points'

**`Width`** (input_control)  extent.x `→`  (integer)

Maximum width of pattern.

Default:
512

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
Width` (lin)

Minimum increment:
1

Recommended increment:
10

**`Height`** (input_control)  extent.y `→`  (integer)

Maximum height of pattern.

Default:
512

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
Height` (lin)

Minimum increment:
1

Recommended increment:
10

## Example (HDevelop)

```
read_image(Image,'fabrik')
gen_grid_region(Raster,10,10,'lines',512,512)
reduce_domain(Image,Raster,Mask)
sobel_amp(Mask,GridSobel,'sum_abs',3)
dev_display(GridSobel)
```

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
