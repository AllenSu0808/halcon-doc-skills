# Intensity (Operator)

## Name

`Intensity` — Calculate the mean and deviation of gray values.

## Signature

`static void HOperatorSet.Intensity(HObject regions, HObject image, out HTuple mean, out HTuple deviation)`

`HTuple HImage.Intensity(HRegion regions, out HTuple deviation)`

`double HImage.Intensity(HRegion regions, out double deviation)`

`HTuple HRegion.Intensity(HImage image, out HTuple deviation)`

`double HRegion.Intensity(HImage image, out double deviation)`

## Description

The operator `Intensity` calculates the mean and the
deviation of the gray values in the input image within
*`regions`*. If R is a region, p a pixel from R with
the gray value g(p) and F the plane (F = |R|), the features
are defined by:
$$\text{Mean} = \frac{\sum_{p\in R} g(p)}{F}$$ ![figure](../assets/c47b4c245704c8ba.svg)
$$\sqrt{\frac{\sum_{p\in R} (g(p) - \text{Mean})^{2}}{F}}$$ ![figure](../assets/2e6f7bde096d25c5.svg)

## Attention

Note that the operator `Intensity` only considers
the given *`regions`* and ignores any previously set domain
of the input image *`image`*.
The calculation of *`deviation`* does not follow the usual
definition if the region of the image contains only one pixel. In
this case 0.0 is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions in which the features are calculated.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Gray value image.

**`mean`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Mean gray value of a region.

**`deviation`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Deviation of gray values within a region.

## Complexity

If F is the area of the region, the runtime complexity is
O(F).

## Result

The operator `Intensity` returns the value 2 (
H_MSG_TRUE)
. The
behavior in case of empty input (no input images available) is set
via the operator
`set_system(::'no_object_result',<Result>:)`,
the behavior in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Possible Successors

`Threshold`

## Alternatives

`SelectGray`,
`MinMaxGray`

## See also

`MeanImage`,
`GrayHisto`,
`GrayHistoAbs`

## Module

Foundation
