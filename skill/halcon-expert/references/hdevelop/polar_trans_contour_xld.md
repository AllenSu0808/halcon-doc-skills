# polar_trans_contour_xld (Operator)

## Name

`polar_trans_contour_xld` — Transform a contour in an annular arc to polar coordinates.

## Signature

`polar_trans_contour_xld(Contour : PolarTransContour : Row, Column, AngleStart, AngleEnd, RadiusStart, RadiusEnd, Width, Height : )`

## Description

`polar_trans_contour_xld` transforms the *`Contour`* in
the annular arc specified by the center point (*`Row`*,
*`Column`*), the radii *`RadiusStart`* and
*`RadiusEnd`* and the angles *`AngleStart`* and
*`AngleEnd`* to its polar coordinate version
*`PolarTransContour`* in the virtual image of the dimensions
*`Width`* x *`Height`*. The output contour
is cropped at the borders of this virtual image.

The coordinate (0,0) in the output contour always corresponds to the
contour point specified by *`RadiusStart`* and
*`AngleStart`*. Analogously, the coordinate
(*`Height`*-1,*`Width`*-1) in the output contour
always corresponds to the point in the contour that is specified by
*`RadiusEnd`* and *`AngleEnd`*, even if the contour does
not contain these points. In the usual mode (*`AngleStart`*
< *`AngleEnd`* and *`RadiusStart`* <
*`RadiusEnd`*), the polar transformation is performed in the
mathematically positive orientation (counterclockwise).
Furthermore, contour points with smaller radii lie in the upper part
of the output contour. By suitably exchanging the values of these
parameters (e.g., *`AngleStart`* > *`AngleEnd`* or
*`RadiusStart`* > *`RadiusEnd`*), any desired
orientation of the output contour *`PolarTransContour`* can be
achieved.

The angles can be chosen from all real numbers. Center point and
radii can be real as well.

Note that *`PolarTransContour`* can consist of more than one
contour because *`Contour`* may be split at
*`AngleStart`* respectively *`AngleEnd`* or the size of
the angle interval [*`AngleStart`*,*`AngleEnd`*] may be
greater than one 2pi period.

If more than one contour is passed in *`Contour`*, their polar
transformations are computed individually and stored as a tuple in
*`PolarTransContour`*. However, since one contour may be
transformed into several contours, there is no relation between the
indices of the contours in the input tuple *`Contour`* and the
indices in the output tuple *`PolarTransContour`*.

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Attention

Only the contour points are transformed. As the polar transformation
is not affine, `polar_trans_contour_xld` only produces
reliable results if the spacing of the contour points is
small. Existing attributes are not transformed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Contour`** (input_object)  xld_cont(-array) `→` object

Input contour.

**`PolarTransContour`** (output_object)  xld_cont(-array) `→` object

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

Angle of the ray to be mapped to the column coordinate
*0* of *`PolarTransContour`*.

Default:
0.0

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853, 12.566370616

Value range:
`-6.2831853
≤
AngleStart
≤
6.2831853`

**`AngleEnd`** (input_control)  angle.rad `→`  (real)

Angle of the ray to be mapped to the column coordinate
*`Width`*-1 of *`PolarTransContour`* to.

Default:
6.2831853

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853, 12.566370616

Value range:
`-6.2831853
≤
AngleEnd
≤
6.2831853`

**`RadiusStart`** (input_control)  number `→`  (real / integer)

Radius of the circle to be mapped to the row coordinate
*0* of *`PolarTransContour`*.

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

Radius of the circle to be mapped to the row coordinate
*`Height`*-1 of *`PolarTransContour`*.

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
`polar_trans_contour_xld_inv`

## Module

Foundation
