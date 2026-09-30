# PolarTransContourXld (Operator)

## Name

`PolarTransContourXld` — Transform a contour in an annular arc to polar coordinates.

## Signature

`static void HOperatorSet.PolarTransContourXld(HObject contour, out HObject polarTransContour, HTuple row, HTuple column, HTuple angleStart, HTuple angleEnd, HTuple radiusStart, HTuple radiusEnd, HTuple width, HTuple height)`

`HXLDCont HXLDCont.PolarTransContourXld(HTuple row, HTuple column, double angleStart, double angleEnd, HTuple radiusStart, HTuple radiusEnd, int width, int height)`

`HXLDCont HXLDCont.PolarTransContourXld(double row, double column, double angleStart, double angleEnd, double radiusStart, double radiusEnd, int width, int height)`

## Description

`PolarTransContourXld` transforms the *`contour`* in
the annular arc specified by the center point (*`row`*,
*`column`*), the radii *`radiusStart`* and
*`radiusEnd`* and the angles *`angleStart`* and
*`angleEnd`* to its polar coordinate version
*`polarTransContour`* in the virtual image of the dimensions
*`width`* x *`height`*. The output contour
is cropped at the borders of this virtual image.

The coordinate (0,0) in the output contour always corresponds to the
contour point specified by *`radiusStart`* and
*`angleStart`*. Analogously, the coordinate
(*`height`*-1,*`width`*-1) in the output contour
always corresponds to the point in the contour that is specified by
*`radiusEnd`* and *`angleEnd`*, even if the contour does
not contain these points. In the usual mode (*`angleStart`*
< *`angleEnd`* and *`radiusStart`* <
*`radiusEnd`*), the polar transformation is performed in the
mathematically positive orientation (counterclockwise).
Furthermore, contour points with smaller radii lie in the upper part
of the output contour. By suitably exchanging the values of these
parameters (e.g., *`angleStart`* > *`angleEnd`* or
*`radiusStart`* > *`radiusEnd`*), any desired
orientation of the output contour *`polarTransContour`* can be
achieved.

The angles can be chosen from all real numbers. Center point and
radii can be real as well.

Note that *`polarTransContour`* can consist of more than one
contour because *`contour`* may be split at
*`angleStart`* respectively *`angleEnd`* or the size of
the angle interval [*`angleStart`*,*`angleEnd`*] may be
greater than one 2pi period.

If more than one contour is passed in *`contour`*, their polar
transformations are computed individually and stored as a tuple in
*`polarTransContour`*. However, since one contour may be
transformed into several contours, there is no relation between the
indices of the contours in the input tuple *`contour`* and the
indices in the output tuple *`polarTransContour`*.

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Attention

Only the contour points are transformed. As the polar transformation
is not affine, `PolarTransContourXld` only produces
reliable results if the spacing of the contour points is
small. Existing attributes are not transformed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`contour`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Input contour.

**`polarTransContour`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Output contour.

**`row`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 240, 256, 480, 512

**`column`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 256, 320, 512, 640

**`angleStart`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Angle of the ray to be mapped to the column coordinate
*0* of *`polarTransContour`*.

Default:
0.0

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853, 12.566370616

Value range:
`-6.2831853
≤
angleStart
≤
6.2831853`

**`angleEnd`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Angle of the ray to be mapped to the column coordinate
*`width`*-1 of *`polarTransContour`* to.

Default:
6.2831853

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853, 12.566370616

Value range:
`-6.2831853
≤
angleEnd
≤
6.2831853`

**`radiusStart`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of the circle to be mapped to the row coordinate
*0* of *`polarTransContour`*.

Default:
0

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
radiusStart
≤
32767`

**`radiusEnd`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of the circle to be mapped to the row coordinate
*`height`*-1 of *`polarTransContour`*.

Default:
100

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
radiusEnd
≤
32767`

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the virtual output image.

Default:
512

Suggested values:
256, 320, 512, 640, 800, 1024

Value range:
`0
≤
width
≤
32767`

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the virtual output image.

Default:
512

Suggested values:
240, 256, 480, 512, 600, 1024

Value range:
`0
≤
height
≤
32767`

## See also

`PolarTransImageExt`,
`PolarTransImageInv`,
`PolarTransRegion`,
`PolarTransRegionInv`,
`PolarTransContourXldInv`

## Module

Foundation
