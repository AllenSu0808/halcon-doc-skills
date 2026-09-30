# entropy_gray (Operator)

## Name

`entropy_gray` — Determine the entropy and anisotropy of images.

## Signature

`entropy_gray(Regions, Image : : : Entropy, Anisotropy)`

## Description

The operator `entropy_gray` creates the histogram of
relative frequencies of the gray values in the input image and
calculates from these frequencies the entropy and the anisotropy
coefficient for each region from *`Regions`* according to the
following formulae:

Entropy:
$$Entropy = -\sum_{i=0}^{255} rel[i] * log_2(rel[i])$$ ![figure](../assets/6230f9371f377c73.svg)
Anisotropy coefficient:
$$Anisotropy = \frac{\sum_{0}^{k} re[l_i] * log_2(re[l_i])}{Entropy}$$ ![figure](../assets/907f847a3b5aeaf9.svg)
where
rel[i] histogram of relative gray value frequencies
i Gray value of input image (0..255)
and k Smallest possible gray value with sum(rel[i]) >= 0.5

## Attention

Note that the operator `entropy_gray` only considers
the given *`Regions`* and ignores any previously set domain
of the input image *`Image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Regions where the features are to be determined.

**`Image`** (input_object)  singlechannelimage `→` object (byte)

Gray value image.

**`Entropy`** (output_control)  real(-array) `→`  (real)

Information content (entropy) of the gray values.

Assertion:
`0 <= Entropy && Entropy <= 8`

**`Anisotropy`** (output_control)  real(-array) `→`  (real)

Measure of the symmetry of gray value distribution.

## Complexity

If F is the area of the region the runtime complexity is O(F + 255).

## Result

The operator `entropy_gray` returns the value 2 (
H_MSG_TRUE)
if an
image with defined gray values is entered and the parameters are
correct. The behavior in case of empty input (no input images
available) is set via the operator
`set_system(::'no_object_result',<Result>:)`, the behavior
in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Alternatives

`select_gray`

## See also

`entropy_image`,
`gray_histo`,
`gray_histo_abs`,
`fuzzy_entropy`,
`fuzzy_perimeter`

## Module

Foundation
