# clip_contours_xld (Operator)

## Name

`clip_contours_xld` — Clip an XLD contour.

## Signature

`clip_contours_xld(Contours : ClippedContours : Row1, Column1, Row2, Column2 : )`

## Description

`clip_contours_xld` clips all XLD contours given in
*`Contours`*, i.e., only contour points contained in the
rectangle given by *`Row1`*, *`Column1`*, *`Row2`*,
and *`Column2`* are returned on output. Note, that the rectangle
behaves like a region, i.e., the rectangle encloses the pixels completely.
If necessary, contours
are split, and several new contours are produced. The resulting
contours are returned in *`ClippedContours`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (input_object)  xld_cont(-array) `→` object

Contours to be clipped.

**`ClippedContours`** (output_object)  xld_cont(-array) `→` object

Clipped contours.

**`Row1`** (input_control)  rectangle.origin.y `→`  (integer)

Row coordinate of the upper left corner of the clip
rectangle.

Default:
0

Suggested values:
0, 500, 1000, 1500, 2000

**`Column1`** (input_control)  rectangle.origin.x `→`  (integer)

Column coordinate of the upper left corner of the clip
rectangle.

Default:
0

Suggested values:
0, 500, 1000, 1500, 2000

**`Row2`** (input_control)  rectangle.corner.y `→`  (integer)

Row coordinate of the lower right corner of the clip
rectangle.

Default:
512

Suggested values:
512, 1024, 1536, 2048

**`Column2`** (input_control)  rectangle.corner.x `→`  (integer)

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
