# intensity (Operator)

## Name

`intensity` — Calculate the mean and deviation of gray values.

## Signature

`def intensity(regions: HObject, image: HObject) -> Tuple[Sequence[float], Sequence[float]]`

`def intensity_s(regions: HObject, image: HObject) -> Tuple[float, float]`

## Description

The operator `intensity` calculates the mean and the
deviation of the gray values in the input image within
*`regions`*. If R is a region, p a pixel from R with
the gray value g(p) and F the plane (F = |R|), the features
are defined by:
$$\text{Mean} = \frac{\sum_{p\in R} g(p)}{F}$$ ![figure](../assets/c47b4c245704c8ba.svg)
$$\sqrt{\frac{\sum_{p\in R} (g(p) - \text{Mean})^{2}}{F}}$$ ![figure](../assets/2e6f7bde096d25c5.svg)

## Attention

Note that the operator `intensity` only considers
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

**`regions`** (input_object)  region(-array) `→` HObject

Regions in which the features are calculated.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Gray value image.

**`mean`** (output_control)  real(-array) `→` Sequence[float]

Mean gray value of a region.

**`deviation`** (output_control)  real(-array) `→` Sequence[float]

Deviation of gray values within a region.

## Complexity

If F is the area of the region, the runtime complexity is
O(F).

## Result

The operator `intensity` returns the value 2 (
H_MSG_TRUE)
. The
behavior in case of empty input (no input images available) is set
via the operator
`set_system(::'no_object_result',<Result>:)`,
the behavior in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Possible Successors

`threshold`

## Alternatives

`select_gray`,
`min_max_gray`

## See also

`mean_image`,
`gray_histo`,
`gray_histo_abs`

## Module

Foundation
