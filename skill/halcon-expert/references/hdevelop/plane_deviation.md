# plane_deviation (Operator)

## Name

`plane_deviation` — Calculate the deviation of the gray values from the approximating
image plane.

## Signature

`plane_deviation(Regions, Image : : : Deviation)`

## Description

The operator `plane_deviation` calculates the deviation of
the gray values in *`Image`* from the approximation of the
gray values through a plane. Contrary to the standard deviation in
case of [`intensity`](intensity.md) slanted gray value planes also
receive the value zero. The gray value plane is calculated
according to [`gen_image_gray_ramp`](gen_image_gray_ramp.md).
If F is the area of the region, $\alpha$, $\beta$,
and $\mu$ the parameters of the
image plane, and (r',c') the center of the region, *`Deviation`* is
defined by:
$$\mathrm{Deviation} = \sqrt{\frac{\sum_{(r,c)\in Regions} \left(\alpha(r - r') + \beta(c - c') + \mu - \mathrm{Image}(r,c)\right)^2}{F}}.$$ ![figure](../assets/6351df86189f267b.svg)

## Attention

Note that the operator `plane_deviation` only considers
the given *`Regions`* and ignores any previously set domain
of the input image *`Image`*.
It should be noted that the calculation of *`Deviation`* does
not follow the usual definition. It is defined to return the value
0.0 for an image with only one pixel.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Regions, of which the plane deviation is to be
calculated.

**`Image`** (input_object)  singlechannelimage `→` object (byte / cyclic)

Gray value image.

**`Deviation`** (output_control)  real(-array) `→`  (real)

Deviation of the gray values within a region.

## Complexity

If F is the area of the region the runtime complexity amounts to
O(F).

## Result

The operator `plane_deviation` returns the value 2 (
H_MSG_TRUE)
if
*`Image`* is of the type byte. The behavior in
case of empty input (no input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`,
the behavior in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Alternatives

`intensity`,
`gen_image_gray_ramp`,
`sub_image`

## See also

`moments_gray_plane`

## Module

Foundation
