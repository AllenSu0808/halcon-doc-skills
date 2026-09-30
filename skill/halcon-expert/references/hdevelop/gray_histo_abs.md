# gray_histo_abs (Operator)

## Name

`gray_histo_abs` — Calculate the gray value distribution.

## Signature

`gray_histo_abs(Region, Image : : Quantization : AbsoluteHisto)`

## Description

The operator `gray_histo_abs` calculates for the image
(*`Image`*) within *`Region`* the absolute
(*`AbsoluteHisto`*) ) histogram of the gray values.

The parameter *`Quantization`* defines, how many frequencies of
neighbored gray values are added for one frequency value. The resulting
histogram *`AbsoluteHisto`* is a tuple, whose indices are mapped on the
gray values of the input image *`Image`* and whose elements contain the
frequencies of the gray values. The indices i of the frequency value
are calculated from the gray values g and the quantization q as follows:

- For unsigned image types:
  $$i = \left( \frac{g + 0.5}{q} \right)$$ ![figure](../assets/3b029edb5c3e5c61.svg)
- For signed image types:
  $$i = \left[ \frac{g - \left(MIN - 0.5\right)}{q} \right]$$ ![figure](../assets/272454ec26a2406e.svg)

whereas MIN denotes the minimal gray value, e.g., -128 for an int1
image type. Therefore, the size of the tuple results from the ratio of the
full domain of gray values and the quantization, e.g., for images of
int2 in $\left\lfloor \frac{65536}{3.0} \right\rfloor = 21846$ ![figure](../assets/694bc02cd5a24fda.svg).
The origin gray value of the signed image types int1 resp. int2 is
mapped on the index 128 resp. 32768, negative resp. positive gray values
have smaller resp. greater indices.

## Attention

Note that the operator `gray_histo_abs` only considers
the given *`Region`* and ignores any previously set domain
of the input image *`Image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Region`** (input_object)  region `→` object

Region in which the histogram is to be calculated.

**`Image`** (input_object)  singlechannelimage `→` object (byte / cyclic / direction / int1 / int2 / uint2)

Image the gray value distribution of which is
to be calculated.

**`Quantization`** (input_control)  number `→`  (real / integer)

Quantization of the gray values.

Default:
1.0

Suggested values:
1.0, 2.0, 3.0, 5.0, 10.0

Restriction:
`Quantization >= 1.0`

**`AbsoluteHisto`** (output_control)  histogram-array `→`  (integer)

Absolute frequencies of the gray values.

## Result

The operator `gray_histo_abs` returns the value 2 (
H_MSG_TRUE)
if the image
has defined gray values and the parameters are correct. The
behavior in case of empty input (no input images available) is set
via the operator
`set_system(::'no_object_result',<Result>:)`, the behavior
in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Possible Successors

`histo_to_thresh`,
`gen_region_histo`

## Alternatives

`min_max_gray`,
`intensity`,
`gray_histo`,
`gray_histo_range`

## See also

`disp_image`,
`histo_2dim`,
`scale_image_max`,
`entropy_gray`

## Module

Foundation
