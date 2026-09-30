# gray_histo_range (Operator)

## Name

`gray_histo_range` — Calculate the gray value distribution of a single channel image within a
certain gray value range.

## Signature

`def gray_histo_range(region: HObject, image: HObject, min: Union[float, int], max: Union[float, int], num_bins: int) -> Tuple[Sequence[int], float]`

`def gray_histo_range_s(region: HObject, image: HObject, min: Union[float, int], max: Union[float, int], num_bins: int) -> Tuple[int, float]`

## Description

`gray_histo_range` calculates the gray value distribution
*`histo`* of the single channel *`image`* within *`region`*
and the gray value range [*`min`*,*`max`*]. The values for
*`min`* and *`max`* are rounded down to the next integer if the
*`image`* is not of type *"real"*. The gray value range is divided
into *`num_bins`* bins of the same size, which is returned in
*`bin_size`*. If a gray value lies between two bins the gray value is
assigned to the smaller bin. If the *`image`* is of type *"real"*
$BinSize = \frac{Max-Min}{NumBins}$ ![figure](../assets/e77fbd30d3031e66.svg).
If the *`image`* has discrete gray values the size of a bin is
computed with
$BinSize = \frac{Max-Min+1}{NumBins}$ ![figure](../assets/a71e09270487a639.svg). Since the accuracy of the histogram *`histo`* can
be adjusted with *`num_bins`*, the calculation of the gray value
histogram with `gray_histo_range` is most useful for images of type
*"real"* and images of type *"integer"*, which have
a high bit depth.

## Attention

Note that the operator `gray_histo_range` only considers
the given *`region`* and ignores any previously set domain
of the input image *`image`*.

If the *`image`* has discrete gray values the value of *`bin_size`*
may cause the following effects:
For *`bin_size`* > *1* multiple neighboring gray values are
assigned to the same bin. If *`bin_size`* is no integer the gray values
are distributed uneven among the bins, e.g., for
*`bin_size`* = *1.5* the first and second gray value are
assigned to the first bin, the third gray value is assigned to the second
bin, and the fourth and fifth gray value are assigned to the third bin.
This becomes noticeable in several peeks in the histogram *`histo`*.
If *`bin_size`* < *1* some classes are not assigned by any
gray value, e.g., for *`bin_size`* = *0.5* the first
gray value is assigned to the first bin and the second gray value is assigned
to the third bin. The histogram *`histo`* shows some gaps, which
resembles the structure of a comb.

If the *`image`* is of type *"real"* and
*`min`* = *`max`*, all pixels of the corresponding gray value
are assigned only to the first bin.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`region`** (input_object)  region `→` HObject

Region in which the histogram is to be calculated.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / cyclic / direction / int1 / uint2 / int2 / int4 / int8 / real)

Input image.

**`min`** (input_control)  real `→` Union[float, int]

Minimum gray value.

Default:
0

Suggested values:
0

**`max`** (input_control)  real `→` Union[float, int]

Maximum gray value.

Default:
255

Suggested values:
255

Restriction:
`Max >= Min`

**`num_bins`** (input_control)  integer `→` int

Number of bins.

Default:
256

Suggested values:
16, 32, 64, 128, 256

Restriction:
`NumBins >= 1`

**`histo`** (output_control)  histogram(-array) `→` Sequence[int]

Histogram to be calculated.

**`bin_size`** (output_control)  real `→` float

Bin size.

## Result

If the parameters are valid, the operator `gray_histo_range`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`min_max_gray`

## Possible Successors

`create_funct_1d_array`

## Alternatives

`gray_histo`,
`gray_histo_abs`

## See also

`histo_2dim`,
`scale_image_max`

## Module

Foundation
