# fuzzy_entropy (Operator)

## Name

`fuzzy_entropy` — Determine the fuzzy entropy of regions.

## Signature

`def fuzzy_entropy(regions: HObject, image: HObject, apar: int, cpar: int) -> Sequence[float]`

`def fuzzy_entropy_s(regions: HObject, image: HObject, apar: int, cpar: int) -> float`

## Description

`fuzzy_entropy` calculates the fuzzy entropy of a fuzzy
set. To do so, the image is regarded as a fuzzy set. The entropy
then is a measure of how well the image approximates a white or
black image. It is defined as follows:
$$H(X) = \frac{1}{M N \ln 2} \sum_i T_e(l) h(l)$$ ![figure](../assets/53b31047264a54c4.svg)
where MxN is the size of the image, and h(l) is
the histogram of the image. Furthermore,
$$T_{e}(l)=-\mu(l)\ln \mu(l)-(1-\mu(l))\ln (1-\mu(l))$$
Here, u(x(m,n)) is a fuzzy membership function defining the fuzzy
set (see [`fuzzy_perimeter`](fuzzy_perimeter.md)). The same restrictions hold
as in [`fuzzy_perimeter`](fuzzy_perimeter.md).

## Attention

Note that for `fuzzy_entropy`, the *`regions`* must lie
completely within the previously defined domain. Otherwise an exception
is raised.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Regions for which the fuzzy entropy is to be
calculated.

**`image`** (input_object)  singlechannelimage `→` HObject (byte)

Input image containing the fuzzy membership values.

**`apar`** (input_control)  integer `→` int

Start of the fuzzy function.

Default:
0

Suggested values:
0, 5, 10, 20, 50, 100

Value range:
`0
≤
apar
≤
255` (lin)

Minimum increment:
1

Recommended increment:
5

**`cpar`** (input_control)  integer `→` int

End of the fuzzy function.

Default:
255

Suggested values:
50, 100, 150, 200, 220, 255

Value range:
`0
≤
cpar
≤
255` (lin)

Minimum increment:
1

Recommended increment:
5

Restriction:
`Apar <= Cpar`

**`entropy`** (output_control)  real(-array) `→` Sequence[float]

Fuzzy entropy of a region.

## Result

The operator `fuzzy_entropy` returns the value 2 (
H_MSG_TRUE)
if
the parameters are correct. Otherwise an exception is raised.

## See also

`fuzzy_perimeter`

## References

M.K. Kundu, S.K. Pal: “Automatic selection of object enhancement
operator with quantitative justification based on fuzzy set theoretic
measures”; Pattern Recognition Letters 11; 1990; pp. 811-829.

## Module

Foundation
