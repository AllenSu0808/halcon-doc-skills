# crop_contours_xld (Operator)

## Name

`crop_contours_xld` — Crop an XLD contour.

## Signature

`def crop_contours_xld(contours: HObject, row_1: Union[float, int], col_1: Union[float, int], row_2: Union[float, int], col_2: Union[float, int], close_contours: str) -> HObject`

## Description

`crop_contours_xld` crops all XLD contours given in *`contours`*,
i.e., only contour segments contained in the rectangle given by
*`row_1`*, *`col_1`*, *`row_2`* and *`col_2`* are
returned on output. While in [`clip_contours_xld`](clip_contours_xld.md) all contour
segments that intersect a boundary line are omitted, here they
are cropped at the exact intersection point with the cropping rectangle.
If necessary, contours are split and several new contours are produced.
Closed contours can, however, be closed again using the parameter
*`close_contours`*. If it is set to *"true"*, a closed contour is
transformed into one or several contours that are closed via segments
on the cropping rectangle. If it is *"false"*, all
contours end at the points where they leave the cropping rectangle.
The resulting contours are returned in *`cropped_contours`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` HObject

Input contours.

**`cropped_contours`** (output_object)  xld_cont(-array) `→` HObject

Output contours.

**`row_1`** (input_control)  number `→` Union[float, int]

Upper border of the cropping
rectangle.

Default:
0

Suggested values:
0, 500, 1000, 1500, 2000

**`col_1`** (input_control)  number `→` Union[float, int]

Left border of the cropping rectangle.

Default:
0

Suggested values:
0, 500, 1000, 1500, 2000

**`row_2`** (input_control)  number `→` Union[float, int]

Lower border of the cropping rectangle.

Default:
512

Suggested values:
512, 1024, 1536, 2048

**`col_2`** (input_control)  number `→` Union[float, int]

Right border of the cropping rectangle.

Default:
512

Suggested values:
512, 1024, 1536, 2048

**`close_contours`** (input_control)  string `→` str

Should closed contours produce closed output
contours?

Default:
"true"

List of values:
"false", "true"

## Alternatives

`clip_contours_xld`

## See also

`clip_region`,
`crop_part`,
`clip_contours_xld`

## Module

Foundation
