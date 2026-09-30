# ClipContoursXld (Operator)

## Name

`ClipContoursXld` — Clip an XLD contour.

## Signature

`static void HOperatorSet.ClipContoursXld(HObject contours, out HObject clippedContours, HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`HXLDCont HXLDCont.ClipContoursXld(int row1, int column1, int row2, int column2)`

## Description

`ClipContoursXld` clips all XLD contours given in
*`contours`*, i.e., only contour points contained in the
rectangle given by *`row1`*, *`column1`*, *`row2`*,
and *`column2`* are returned on output. Note, that the rectangle
behaves like a region, i.e., the rectangle encloses the pixels completely.
If necessary, contours
are split, and several new contours are produced. The resulting
contours are returned in *`clippedContours`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Contours to be clipped.

**`clippedContours`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Clipped contours.

**`row1`** (input_control)  rectangle.origin.y `→` [HTuple](HTuple.md) (*int* / long)

Row coordinate of the upper left corner of the clip
rectangle.

Default:
0

Suggested values:
0, 500, 1000, 1500, 2000

**`column1`** (input_control)  rectangle.origin.x `→` [HTuple](HTuple.md) (*int* / long)

Column coordinate of the upper left corner of the clip
rectangle.

Default:
0

Suggested values:
0, 500, 1000, 1500, 2000

**`row2`** (input_control)  rectangle.corner.y `→` [HTuple](HTuple.md) (*int* / long)

Row coordinate of the lower right corner of the clip
rectangle.

Default:
512

Suggested values:
512, 1024, 1536, 2048

**`column2`** (input_control)  rectangle.corner.x `→` [HTuple](HTuple.md) (*int* / long)

Column coordinate of the lower right corner of the clip
rectangle.

Default:
512

Suggested values:
512, 1024, 1536, 2048

## Possible Predecessors

`GenContoursSkeletonXld`,
`LinesGauss`,
`LinesFacet`,
`EdgesSubPix`

## Possible Successors

`GenPolygonsXld`

## Alternatives

`CropContoursXld`

## See also

`ClipRegion`,
`CropPart`,
`CropContoursXld`

## Module

Foundation
