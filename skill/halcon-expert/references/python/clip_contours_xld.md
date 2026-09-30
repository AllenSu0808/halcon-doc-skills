# clip_contours_xld (Operator)

## Name

`clip_contours_xld` — Clip an XLD contour.

## Signature

`def clip_contours_xld(contours: HObject, row_1: int, column_1: int, row_2: int, column_2: int) -> HObject`

## Description

`clip_contours_xld` clips all XLD contours given in
*`contours`*, i.e., only contour points contained in the
rectangle given by *`row_1`*, *`column_1`*, *`row_2`*,
and *`column_2`* are returned on output. Note, that the rectangle
behaves like a region, i.e., the rectangle encloses the pixels completely.
If necessary, contours
are split, and several new contours are produced. The resulting
contours are returned in *`clipped_contours`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` HObject

Contours to be clipped.

**`clipped_contours`** (output_object)  xld_cont(-array) `→` HObject

Clipped contours.

**`row_1`** (input_control)  rectangle.origin.y `→` int

Row coordinate of the upper left corner of the clip
rectangle.

Default:
0

Suggested values:
0, 500, 1000, 1500, 2000

**`column_1`** (input_control)  rectangle.origin.x `→` int

Column coordinate of the upper left corner of the clip
rectangle.

Default:
0

Suggested values:
0, 500, 1000, 1500, 2000

**`row_2`** (input_control)  rectangle.corner.y `→` int

Row coordinate of the lower right corner of the clip
rectangle.

Default:
512

Suggested values:
512, 1024, 1536, 2048

**`column_2`** (input_control)  rectangle.corner.x `→` int

Column coordinate of the lower right corner of the clip
rectangle.

Default:
512

Suggested values:
512, 1024, 1536, 2048

## Possible Predecessors

`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`

## Possible Successors

`gen_polygons_xld`

## Alternatives

`crop_contours_xld`

## See also

`clip_region`,
`crop_part`,
`crop_contours_xld`

## Module

Foundation
