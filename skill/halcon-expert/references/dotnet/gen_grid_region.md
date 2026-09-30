# GenGridRegion (Operator)

## Name

`GenGridRegion` — Create a region from lines or pixels.

## Signature

`static void HOperatorSet.GenGridRegion(out HObject regionGrid, HTuple rowSteps, HTuple columnSteps, HTuple type, HTuple width, HTuple height)`

`void HRegion.GenGridRegion(HTuple rowSteps, HTuple columnSteps, string type, int width, int height)`

`void HRegion.GenGridRegion(int rowSteps, int columnSteps, string type, int width, int height)`

## Description

The operator `GenGridRegion` creates a grid constructed
of lines (*`type`* = 'lines') or pixels
(*`type`* = 'points').
In case of 'lines' continuous lines are returned, in case of
'points' only the intersections of the lines.
Starting from the pixel (0,0) to the pixel
(*`height`*-1,*`width`*-1) the grid is
built up at stepping width *`rowSteps`* in row
direction and *`columnSteps`* in column direction.
The step widths have to be greater than *1*.
Exceptions are in 'lines' mode *`rowSteps`*, where
*`rowSteps`* or *`columnSteps`* can be set equal to *0*.
In such a case, only columns, rows respectively, are created.

## Attention

If a very small pattern is chosen
(*`rowSteps`* < 4 or *`columnSteps`*
< 4) the created region requires much storage.

In the 'points' mode *`rowSteps`* and
*`columnSteps`* must not be set to zero.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regionGrid`** (output_object)  region `→` [HRegion](HRegion.md)

Created lines/pixel region.

**`rowSteps`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long / double)

Step width in line direction or zero.

Default:
10

Suggested values:
0, 2, 3, 4, 5, 7, 10, 15, 20, 30, 50, 100

Value range:
`rowSteps` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`RowSteps > 1 || RowSteps == 0`

**`columnSteps`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long / double)

Step width in column direction or zero.

Default:
10

Suggested values:
0, 2, 3, 4, 5, 7, 10, 15, 20, 30, 50, 100

Value range:
`columnSteps` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`ColumnSteps > 1 || ColumnSteps == 0`

**`type`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of created pattern.

Default:
"lines"

List of values:
"lines", "points"

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

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

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

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

If the parameter values are correct the operator `GenGridRegion`
returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.
The clipping according to the current image format is set via the operator
`set_system('clip_region',<'true'/'false'>)`.

## Possible Successors

`ReduceDomain`,
`PaintRegion`

## Alternatives

`GenRegionLine`,
`GenRegionPolygon`,
`GenRegionPoints`,
`GenRegionRuns`

## See also

`GenCheckerRegion`,
`ReduceDomain`

## Module

Foundation
