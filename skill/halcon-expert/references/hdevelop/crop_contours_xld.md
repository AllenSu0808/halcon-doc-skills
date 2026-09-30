# crop_contours_xld (Operator)

## Name

`crop_contours_xld` — Crop an XLD contour.

## Signature

`crop_contours_xld(Contours : CroppedContours : Row1, Col1, Row2, Col2, CloseContours : )`

## Description

`crop_contours_xld` crops all XLD contours given in *`Contours`*,
i.e., only contour segments contained in the rectangle given by
*`Row1`*, *`Col1`*, *`Row2`* and *`Col2`* are
returned on output. While in [`clip_contours_xld`](clip_contours_xld.md) all contour
segments that intersect a boundary line are omitted, here they
are cropped at the exact intersection point with the cropping rectangle.
If necessary, contours are split and several new contours are produced.
Closed contours can, however, be closed again using the parameter
*`CloseContours`*. If it is set to *'true'*, a closed contour is
transformed into one or several contours that are closed via segments
on the cropping rectangle. If it is *'false'*, all
contours end at the points where they leave the cropping rectangle.
The resulting contours are returned in *`CroppedContours`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Contours`** (input_object)  xld_cont(-array) `→` object

Input contours.

**`CroppedContours`** (output_object)  xld_cont(-array) `→` object

Output contours.

**`Row1`** (input_control)  number `→`  (real / integer)

Upper border of the cropping
rectangle.

Default:
0

Suggested values:
0, 500, 1000, 1500, 2000

**`Col1`** (input_control)  number `→`  (real / integer)

Left border of the cropping rectangle.

Default:
0

Suggested values:
0, 500, 1000, 1500, 2000

**`Row2`** (input_control)  number `→`  (real / integer)

Lower border of the cropping rectangle.

Default:
512

Suggested values:
512, 1024, 1536, 2048

**`Col2`** (input_control)  number `→`  (real / integer)

Right border of the cropping rectangle.

Default:
512

Suggested values:
512, 1024, 1536, 2048

**`CloseContours`** (input_control)  string `→`  (string)

Should closed contours produce closed output
contours?

Default:
'true'

List of values:
'false', 'true'

## Alternatives

`clip_contours_xld`

## See also

`clip_region`,
`crop_part`,
`clip_contours_xld`

## Module

Foundation
