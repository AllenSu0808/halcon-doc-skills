# polar_trans_region (Operator)

## Name

`polar_trans_region` — Transform a region within an annular arc to polar coordinates.

## Signature

`def polar_trans_region(region: HObject, row: Union[int, float], column: Union[int, float], angle_start: float, angle_end: float, radius_start: Union[int, float], radius_end: Union[int, float], width: int, height: int, interpolation: str) -> HObject`

## Description

`polar_trans_region` transforms a *`region`* within the
annular arc specified by the center point (*`row`*,
*`column`*), the radii *`radius_start`* and
*`radius_end`* and the angles *`angle_start`* and
*`angle_end`* to its polar coordinate version in a virtual image
of the dimensions *`width`* x *`height`*.

The polar transformation is a change of the coordinate
system. Instead of a row and a column coordinate, each point's
position is expressed by its radius r (i.e. the distance to the
center point *`row`*, *`column`*) and the angle phi
between the column axis (through the center point) and the line from
the center point towards the point. Note that this transformation is
not affine.

The coordinate (0,0) in the output region always corresponds to
the point in the input region that is specified by
*`radius_start`* and *`angle_start`*. Analogously, the
coordinate (*`height`*-1, *`width`*-1) corresponds to
the point in the input region that is specified by
*`radius_end`* and *`angle_end`*. In the usual mode
(*`angle_start`* < *`angle_end`* and *`radius_start`*
< *`radius_end`*), the polar transformation is performed in
the mathematically positive orientation (counterclockwise).
Furthermore, points with smaller radii lie in the upper part of the
output region. By suitably exchanging the values of these
parameters (e.g., *`angle_start`* > *`angle_end`* or
*`radius_start`* > *`radius_end`*), any desired
orientation of the output region can be achieved.

The angles can be chosen from all real numbers. Center point and
radii can be real as well. However, if they are both integers and
the difference of *`radius_end`* and *`radius_start`* equals
*`height`*-1, calculation will be sped up through an
optimized routine.

The radii and angles are inclusive, which means that the first row
of the virtual target image contains the circle with radius
*`radius_start`* and the last row contains the circle with
radius *`radius_end`*. For complete circles, where the
difference between *`angle_start`* and *`angle_end`* equals
$2\pi$ (360 degrees), this also means that the first
column of the target image will be the same as the last.

To avoid this, do not make this difference $2\pi$, but
$2\pi\bigl(1 - \frac{1}{\mathrm{widt}h}\bigr)$ ![figure](../assets/7a628e5fd266ca23.svg) degrees instead.

The parameter *`interpolation`* is used to select the
interpolation method *"bilinear"* or
*"nearest_neighbor"*. Setting *`interpolation`* to
*"bilinear"* leads to smoother region boundaries, especially
if regions are enlarged. However, the runtime increases
significantly.

If more than one region is passed in *`region`*, their polar
transformations are computed individually and stored as a tuple in
*`polar_trans_region`*. Please note that the indices of an
input region and its transformation only correspond if the system
variable *"store_empty_regions"* is set to *"true"*
(see [`set_system`](set_system.md)). Otherwise empty output regions are
discarded and the length of the input tuple *`region`* is most
likely not equal to the length of the output tuple
*`polar_trans_region`*.

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Attention

If *`width`* or *`height`* are chosen greater than the
dimensions of the current image, the system variable
*"clip_region"* should be set to *"false"* (see
[`set_system`](set_system.md)). Otherwise, an output region that does not lie
within the dimensions of the current image can produce an error
message.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Input region.

**`polar_trans_region`** (output_object)  region(-array) `→` HObject

Output region.

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

Angle of the ray to be mapped to column coordinate
*0* of *`polar_trans_region`*.

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

Angle of the ray to be mapped to column coordinate
*`width`*-1 of *`polar_trans_region`*.

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

Radius of the circle to be mapped to row coordinate
*0* of *`polar_trans_region`*.

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

Radius of the circle to be mapped to row coordinate
*`height`*-1 of *`polar_trans_region`*.

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
`2
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
`2
≤
height
≤
32767`

**`interpolation`** (input_control)  string `→` str

Interpolation method for the transformation.

Default:
"nearest_neighbor"

List of values:
"bilinear", "nearest_neighbor"

## See also

`polar_trans_image_ext`,
`polar_trans_image_inv`,
`polar_trans_region_inv`,
`polar_trans_contour_xld`,
`polar_trans_contour_xld_inv`

## Module

Foundation
