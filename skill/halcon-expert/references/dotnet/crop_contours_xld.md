# CropContoursXld (Operator)

## Name

`CropContoursXld` — Crop an XLD contour.

## Signature

`static void HOperatorSet.CropContoursXld(HObject contours, out HObject croppedContours, HTuple row1, HTuple col1, HTuple row2, HTuple col2, HTuple closeContours)`

`HXLDCont HXLDCont.CropContoursXld(HTuple row1, HTuple col1, HTuple row2, HTuple col2, string closeContours)`

`HXLDCont HXLDCont.CropContoursXld(double row1, double col1, double row2, double col2, string closeContours)`

## Description

`CropContoursXld` crops all XLD contours given in *`contours`*,
i.e., only contour segments contained in the rectangle given by
*`row1`*, *`col1`*, *`row2`* and *`col2`* are
returned on output. While in [`ClipContoursXld`](clip_contours_xld.md) all contour
segments that intersect a boundary line are omitted, here they
are cropped at the exact intersection point with the cropping rectangle.
If necessary, contours are split and several new contours are produced.
Closed contours can, however, be closed again using the parameter
*`closeContours`*. If it is set to *"true"*, a closed contour is
transformed into one or several contours that are closed via segments
on the cropping rectangle. If it is *"false"*, all
contours end at the points where they leave the cropping rectangle.
The resulting contours are returned in *`croppedContours`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Input contours.

**`croppedContours`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Output contours.

**`row1`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Upper border of the cropping
rectangle.

Default:
0

Suggested values:
0, 500, 1000, 1500, 2000

**`col1`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Left border of the cropping rectangle.

Default:
0

Suggested values:
0, 500, 1000, 1500, 2000

**`row2`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Lower border of the cropping rectangle.

Default:
512

Suggested values:
512, 1024, 1536, 2048

**`col2`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Right border of the cropping rectangle.

Default:
512

Suggested values:
512, 1024, 1536, 2048

**`closeContours`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Should closed contours produce closed output
contours?

Default:
"true"

List of values:
"false", "true"

## Alternatives

`ClipContoursXld`

## See also

`ClipRegion`,
`CropPart`,
`ClipContoursXld`

## Module

Foundation
