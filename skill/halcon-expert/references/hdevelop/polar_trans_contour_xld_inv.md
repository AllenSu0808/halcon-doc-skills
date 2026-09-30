# polar_trans_contour_xld_inv (Operator)

## Name

`polar_trans_contour_xld_inv` — Transform a contour in polar coordinates back to Cartesian coordinates

## Signature

`polar_trans_contour_xld_inv(PolarContour : XYTransContour : Row, Column, AngleStart, AngleEnd, RadiusStart, RadiusEnd, WidthIn, HeightIn, Width, Height : )`

## Description

`polar_trans_contour_xld_inv` transforms the polar coordinate
representation of a contour, stored in *`PolarContour`*, back
onto an annular arc in Cartesian coordinates, described by the radii
*`RadiusStart`* and *`RadiusEnd`* and the angles
*`AngleStart`* and *`AngleEnd`* with the center point
located at (*`Row`*, *`Column`*). All of these values can
be chosen as real numbers. In addition, the dimensions of the
virtual image containing the contour *`PolarContour`* must be
given in *`WidthIn`* and
*`HeightIn`*. *`WidthIn`*-1 is the column coordinate
corresponding to *`AngleEnd`* and *`HeightIn`*-1 is the
row coordinate corresponding to
*`RadiusEnd`*. *`AngleStart`* and *`RadiusStart`*
correspond to column and row coordinate *0*. Furthermore, the
dimensions *`Width`* and *`Height`* of the virtual output
image containing the transformed contour *`XYTransContour`* are
required. The output contour is cropped at the borders of this
virtual output image.

`polar_trans_contour_xld_inv` is the inverse function of
[`polar_trans_contour_xld`](polar_trans_contour_xld.md).

The call sequence:

|  |
| --- |
| `polar_trans_contour_xld(Contour, PolarContour, Row, Column, rad(360), 0, 0, Radius, Width, Height)` |
| `polar_trans_contour_xld_inv(PolarContour, XYTransContour, Row, Column, rad(360), 0, 0, Radius, Width, Height, WidthOut, HeightOut)` |

returns the contour `Contour`, restricted to the circle
around (`Row`, `Column`) with radius `Radius`,
as its output contour *`XYTransContour`*.

Note that *`XYTransContour`* can consist of more than one
contour because *`PolarContour`* may be cropped at the borders
of the virtual output image given by *`Width`* and
*`Height`*.

If more than one contour is passed in *`PolarContour`*, their
transformations are computed individually and stored as a tuple in
*`XYTransContour`*. However, since one contour may be
transformed into several contours, there is no relation between the
indices of the contours in the input tuple *`PolarContour`* and
the indices in the output tuple *`XYTransContour`*.

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Attention

Only the contour points are transformed. As the polar transformation
is not affine, `polar_trans_contour_xld_inv` only produces
reliable results if the spacing of the contour points is
small. Existing attributes are not transformed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`PolarContour`** (input_object)  xld_cont(-array) `→` object

Input contour.

**`XYTransContour`** (output_object)  xld_cont(-array) `→` object

Output contour.

**`Row`** (input_control)  number `→`  (real / integer)

Row coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 240, 256, 480, 512

**`Column`** (input_control)  number `→`  (real / integer)

Column coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 256, 320, 512, 640

**`AngleStart`** (input_control)  angle.rad `→`  (real)

Angle of the ray to map the column coordinate *0*
of *`PolarContour`* to.

Default:
0.0

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853

Value range:
`-6.2831853
≤
AngleStart
≤
6.2831853`

**`AngleEnd`** (input_control)  angle.rad `→`  (real)

Angle of the ray to map the column coordinate
*`WidthIn`*-1 of *`PolarContour`* to.

Default:
6.2831853

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853

Value range:
`-6.2831853
≤
AngleEnd
≤
6.2831853`

**`RadiusStart`** (input_control)  number `→`  (real / integer)

Radius of the circle to map the row coordinate
*0* of *`PolarContour`* to.

Default:
0

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
RadiusStart
≤
32767`

**`RadiusEnd`** (input_control)  number `→`  (real / integer)

Radius of the circle to map the row coordinate
*`HeightIn`*-1 of *`PolarContour`* to.

Default:
100

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
RadiusEnd
≤
32767`

**`WidthIn`** (input_control)  extent.x `→`  (integer)

Width of the virtual input image.

Default:
512

Suggested values:
256, 320, 512, 640, 800, 1024

Value range:
`0
≤
WidthIn
≤
32767`

**`HeightIn`** (input_control)  extent.y `→`  (integer)

Height of the virtual input image.

Default:
512

Suggested values:
240, 256, 480, 512, 600, 1024

Value range:
`0
≤
HeightIn
≤
32767`

**`Width`** (input_control)  extent.x `→`  (integer)

Width of the virtual output image.

Default:
512

Suggested values:
256, 320, 512, 640, 800, 1024

Value range:
`0
≤
Width
≤
32767`

**`Height`** (input_control)  extent.y `→`  (integer)

Height of the virtual output image.

Default:
512

Suggested values:
240, 256, 480, 512, 600, 1024

Value range:
`0
≤
Height
≤
32767`

## See also

`polar_trans_image_ext`,
`polar_trans_image_inv`,
`polar_trans_region`,
`polar_trans_region_inv`,
`polar_trans_contour_xld`

## Module

Foundation
