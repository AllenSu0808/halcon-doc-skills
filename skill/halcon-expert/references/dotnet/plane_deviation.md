# PlaneDeviation (Operator)

## Name

`PlaneDeviation` — Calculate the deviation of the gray values from the approximating
image plane.

## Signature

`static void HOperatorSet.PlaneDeviation(HObject regions, HObject image, out HTuple deviation)`

`HTuple HImage.PlaneDeviation(HRegion regions)`

`HTuple HRegion.PlaneDeviation(HImage image)`

## Description

The operator `PlaneDeviation` calculates the deviation of
the gray values in *`image`* from the approximation of the
gray values through a plane. Contrary to the standard deviation in
case of [`Intensity`](intensity.md) slanted gray value planes also
receive the value zero. The gray value plane is calculated
according to [`GenImageGrayRamp`](gen_image_gray_ramp.md).
If F is the area of the region, $\alpha$, $\beta$,
and $\mu$ the parameters of the
image plane, and (r',c') the center of the region, *`deviation`* is
defined by:
$$\mathrm{Deviation} = \sqrt{\frac{\sum_{(r,c)\in Regions} \left(\alpha(r - r') + \beta(c - c') + \mu - \mathrm{Image}(r,c)\right)^2}{F}}.$$ ![figure](../assets/6351df86189f267b.svg)

## Attention

Note that the operator `PlaneDeviation` only considers
the given *`regions`* and ignores any previously set domain
of the input image *`image`*.
It should be noted that the calculation of *`deviation`* does
not follow the usual definition. It is defined to return the value
0.0 for an image with only one pixel.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions, of which the plane deviation is to be
calculated.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / cyclic)

Gray value image.

**`deviation`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Deviation of the gray values within a region.

## Complexity

If F is the area of the region the runtime complexity amounts to
O(F).

## Result

The operator `PlaneDeviation` returns the value 2 (
H_MSG_TRUE)
if
*`image`* is of the type byte. The behavior in
case of empty input (no input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`,
the behavior in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Alternatives

`Intensity`,
`GenImageGrayRamp`,
`SubImage`

## See also

`MomentsGrayPlane`

## Module

Foundation
