# fuzzy_entropy (Operator)

## Name

`fuzzy_entropy` — Determine the fuzzy entropy of regions.

## Signature

`fuzzy_entropy(Regions, Image : : Apar, Cpar : Entropy)`

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

Note that for `fuzzy_entropy`, the *`Regions`* must lie
completely within the previously defined domain. Otherwise an exception
is raised.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Regions for which the fuzzy entropy is to be
calculated.

**`Image`** (input_object)  singlechannelimage `→` object (byte)

Input image containing the fuzzy membership values.

**`Apar`** (input_control)  integer `→`  (integer)

Start of the fuzzy function.

Default:
0

Suggested values:
0, 5, 10, 20, 50, 100

Value range:
`0
≤
Apar
≤
255` (lin)

Minimum increment:
1

Recommended increment:
5

**`Cpar`** (input_control)  integer `→`  (integer)

End of the fuzzy function.

Default:
255

Suggested values:
50, 100, 150, 200, 220, 255

Value range:
`0
≤
Cpar
≤
255` (lin)

Minimum increment:
1

Recommended increment:
5

Restriction:
`Apar <= Cpar`

**`Entropy`** (output_control)  real(-array) `→`  (real)

Fuzzy entropy of a region.

## Example (HDevelop)

```
* To find a Fuzzy Entropy from an Image
read_image(Image,'monkey')
fuzzy_entropy(Trans,Trans,0,255,Entro)
```

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
