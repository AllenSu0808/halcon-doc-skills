# polar_trans_contour_xld (Operator)

## Name

`polar_trans_contour_xld` — Transform a contour in an annular arc to polar coordinates.

## Signature

`def polar_trans_contour_xld(contour: HObject, row: Union[int, float], column: Union[int, float], angle_start: float, angle_end: float, radius_start: Union[int, float], radius_end: Union[int, float], width: int, height: int) -> HObject`

## Description

`polar_trans_contour_xld` transforms the *`contour`* in
the annular arc specified by the center point (*`row`*,
*`column`*), the radii *`radius_start`* and
*`radius_end`* and the angles *`angle_start`* and
*`angle_end`* to its polar coordinate version
*`polar_trans_contour`* in the virtual image of the dimensions
*`width`* x *`height`*. The output contour
is cropped at the borders of this virtual image.

The coordinate (0,0) in the output contour always corresponds to the
contour point specified by *`radius_start`* and
*`angle_start`*. Analogously, the coordinate
(*`height`*-1,*`width`*-1) in the output contour
always corresponds to the point in the contour that is specified by
*`radius_end`* and *`angle_end`*, even if the contour does
not contain these points. In the usual mode (*`angle_start`*
< *`angle_end`* and *`radius_start`* <
*`radius_end`*), the polar transformation is performed in the
mathematically positive orientation (counterclockwise).
Furthermore, contour points with smaller radii lie in the upper part
of the output contour. By suitably exchanging the values of these
parameters (e.g., *`angle_start`* > *`angle_end`* or
*`radius_start`* > *`radius_end`*), any desired
orientation of the output contour *`polar_trans_contour`* can be
achieved.

The angles can be chosen from all real numbers. Center point and
radii can be real as well.

Note that *`polar_trans_contour`* can consist of more than one
contour because *`contour`* may be split at
*`angle_start`* respectively *`angle_end`* or the size of
the angle interval [*`angle_start`*,*`angle_end`*] may be
greater than one 2pi period.

If more than one contour is passed in *`contour`*, their polar
transformations are computed individually and stored as a tuple in
*`polar_trans_contour`*. However, since one contour may be
transformed into several contours, there is no relation between the
indices of the contours in the input tuple *`contour`* and the
indices in the output tuple *`polar_trans_contour`*.

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

**`contour`** (input_object)  xld_cont(-array) `→` HObject

Input contour.

**`polar_trans_contour`** (output_object)  xld_cont(-array) `→` HObject

Output contour.

**`row`** (input_control)  number `→` Union[int, float]

Row coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 240, 256, 480, 512

**`column`** (input_control)  number `→` Union[int, float]

Column coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 256, 320, 512, 640

**`angle_start`** (input_control)  angle.rad `→` float

Angle of the ray to be mapped to the column coordinate
*0* of *`polar_trans_contour`*.

Default:
0.0

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853, 12.566370616

Value range:
`-6.2831853
≤
angle_start
≤
6.2831853`

**`angle_end`** (input_control)  angle.rad `→` float

Angle of the ray to be mapped to the column coordinate
*`width`*-1 of *`polar_trans_contour`* to.

Default:
6.2831853

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853, 12.566370616

Value range:
`-6.2831853
≤
angle_end
≤
6.2831853`

**`radius_start`** (input_control)  number `→` Union[int, float]

Radius of the circle to be mapped to the row coordinate
*0* of *`polar_trans_contour`*.

Default:
0

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
radius_start
≤
32767`

**`radius_end`** (input_control)  number `→` Union[int, float]

Radius of the circle to be mapped to the row coordinate
*`height`*-1 of *`polar_trans_contour`*.

Default:
100

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
radius_end
≤
32767`

**`width`** (input_control)  extent.x `→` int

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

**`height`** (input_control)  extent.y `→` int

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

`polar_trans_image_ext`,
`polar_trans_image_inv`,
`polar_trans_region`,
`polar_trans_region_inv`,
`polar_trans_contour_xld_inv`

## Module

Foundation
