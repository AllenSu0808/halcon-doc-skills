# PolarTransContourXldInv (Operator)

## Name

`PolarTransContourXldInv` — Transform a contour in polar coordinates back to Cartesian coordinates

## Signature

`static void HOperatorSet.PolarTransContourXldInv(HObject polarContour, out HObject XYTransContour, HTuple row, HTuple column, HTuple angleStart, HTuple angleEnd, HTuple radiusStart, HTuple radiusEnd, HTuple widthIn, HTuple heightIn, HTuple width, HTuple height)`

`HXLDCont HXLDCont.PolarTransContourXldInv(HTuple row, HTuple column, double angleStart, double angleEnd, HTuple radiusStart, HTuple radiusEnd, int widthIn, int heightIn, int width, int height)`

`HXLDCont HXLDCont.PolarTransContourXldInv(double row, double column, double angleStart, double angleEnd, double radiusStart, double radiusEnd, int widthIn, int heightIn, int width, int height)`

## Description

`PolarTransContourXldInv` transforms the polar coordinate
representation of a contour, stored in *`polarContour`*, back
onto an annular arc in Cartesian coordinates, described by the radii
*`radiusStart`* and *`radiusEnd`* and the angles
*`angleStart`* and *`angleEnd`* with the center point
located at (*`row`*, *`column`*). All of these values can
be chosen as real numbers. In addition, the dimensions of the
virtual image containing the contour *`polarContour`* must be
given in *`widthIn`* and
*`heightIn`*. *`widthIn`*-1 is the column coordinate
corresponding to *`angleEnd`* and *`heightIn`*-1 is the
row coordinate corresponding to
*`radiusEnd`*. *`angleStart`* and *`radiusStart`*
correspond to column and row coordinate *0*. Furthermore, the
dimensions *`width`* and *`height`* of the virtual output
image containing the transformed contour *`XYTransContour`* are
required. The output contour is cropped at the borders of this
virtual output image.

`PolarTransContourXldInv` is the inverse function of
[`PolarTransContourXld`](polar_trans_contour_xld.md).

The call sequence:

|  |
| --- |
| `polar_trans_contour_xld(Contour, PolarContour, Row, Column, rad(360), 0, 0, Radius, Width, Height)` |
| `polar_trans_contour_xld_inv(PolarContour, XYTransContour, Row, Column, rad(360), 0, 0, Radius, Width, Height, WidthOut, HeightOut)` |

returns the contour `contour`, restricted to the circle
around (`row`, `column`) with radius `radius`,
as its output contour *`XYTransContour`*.

Note that *`XYTransContour`* can consist of more than one
contour because *`polarContour`* may be cropped at the borders
of the virtual output image given by *`width`* and
*`height`*.

If more than one contour is passed in *`polarContour`*, their
transformations are computed individually and stored as a tuple in
*`XYTransContour`*. However, since one contour may be
transformed into several contours, there is no relation between the
indices of the contours in the input tuple *`polarContour`* and
the indices in the output tuple *`XYTransContour`*.

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Attention

Only the contour points are transformed. As the polar transformation
is not affine, `PolarTransContourXldInv` only produces
reliable results if the spacing of the contour points is
small. Existing attributes are not transformed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`polarContour`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Input contour.

**`XYTransContour`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

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

Angle of the ray to map the column coordinate *0*
of *`polarContour`* to.

Default:
0.0

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853

Value range:
`-6.2831853
≤
angleStart
≤
6.2831853`

**`angleEnd`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Angle of the ray to map the column coordinate
*`widthIn`*-1 of *`polarContour`* to.

Default:
6.2831853

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853

Value range:
`-6.2831853
≤
angleEnd
≤
6.2831853`

**`radiusStart`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of the circle to map the row coordinate
*0* of *`polarContour`* to.

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

Radius of the circle to map the row coordinate
*`heightIn`*-1 of *`polarContour`* to.

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

**`widthIn`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the virtual input image.

Default:
512

Suggested values:
256, 320, 512, 640, 800, 1024

Value range:
`0
≤
widthIn
≤
32767`

**`heightIn`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the virtual input image.

Default:
512

Suggested values:
240, 256, 480, 512, 600, 1024

Value range:
`0
≤
heightIn
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
`PolarTransContourXld`

## Module

Foundation
