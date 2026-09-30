# elliptic_axis_gray (Operator)

## Name

`elliptic_axis_gray` — Compute the orientation and major axes of a region in a gray value
image.

## Signature

`def elliptic_axis_gray(regions: HObject, image: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

`def elliptic_axis_gray_s(regions: HObject, image: HObject) -> Tuple[float, float, float]`

## Description

The operator `elliptic_axis_gray` calculates the length of the
axes *`ra`* and *`rb`* and the orientation *`phi`* of the
ellipse having the “same orientation” and the “aspect ratio” as the
input region in *`regions`*. Therefore, gray value moments which are
derived from the *`image`* are used.
Several input regions can be passed in *`regions`* as tuples. The
length of the major axis *`ra`* and the minor axis *`rb`*
as well as the orientation of the major axis with regard to the
x-axis (*`phi`*) are determined. The angle is returned in
radians. The calculation is done analogously to
[`elliptic_axis`](elliptic_axis.md). The only difference is that in
`elliptic_axis_gray` the gray value moments are used instead
of the region moments. For the definition of the gray value
moments, see [`area_center_gray`](area_center_gray.md).

Note, that in the case where the gray value area is zero the length
of the axes *`ra`* and *`rb`* as well as the orientation
*`phi`* are also set to zero.

## Attention

Note that the operator `elliptic_axis_gray` only considers
the given *`regions`* and ignores any previously set domain
of the input image *`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Region(s) to be examined.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Gray value image.

**`ra`** (output_control)  real(-array) `→` Sequence[float]

Major axis of the region.

**`rb`** (output_control)  real(-array) `→` Sequence[float]

Minor axis of the region.

**`phi`** (output_control)  angle.rad(-array) `→` Sequence[float]

Angle enclosed by the major axis and the x-axis.

## Result

`elliptic_axis_gray` returns 2 (
H_MSG_TRUE)
if all parameters are
correct and no error occurs during execution. If the input is empty
the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## Possible Successors

`gen_ellipse`

## Alternatives

`elliptic_axis`

## See also

`area_center_gray`

## Module

Foundation
