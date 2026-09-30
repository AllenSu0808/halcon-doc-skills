# gray_histo_range (Operator)

## Name

`gray_histo_range` — Calculate the gray value distribution of a single channel image within a
certain gray value range.

## Signature

`gray_histo_range(Region, Image : : Min, Max, NumBins : Histo, BinSize)`

## Description

`gray_histo_range` calculates the gray value distribution
*`Histo`* of the single channel *`Image`* within *`Region`*
and the gray value range [*`Min`*,*`Max`*]. The values for
*`Min`* and *`Max`* are rounded down to the next integer if the
*`Image`* is not of type *'real'*. The gray value range is divided
into *`NumBins`* bins of the same size, which is returned in
*`BinSize`*. If a gray value lies between two bins the gray value is
assigned to the smaller bin. If the *`Image`* is of type *'real'*
$BinSize = \frac{Max-Min}{NumBins}$ ![figure](../assets/e77fbd30d3031e66.svg).
If the *`Image`* has discrete gray values the size of a bin is
computed with
$BinSize = \frac{Max-Min+1}{NumBins}$ ![figure](../assets/a71e09270487a639.svg). Since the accuracy of the histogram *`Histo`* can
be adjusted with *`NumBins`*, the calculation of the gray value
histogram with `gray_histo_range` is most useful for images of type
*'real'* and images of type *'integer'*, which have
a high bit depth.

## Attention

Note that the operator `gray_histo_range` only considers
the given *`Region`* and ignores any previously set domain
of the input image *`Image`*.

If the *`Image`* has discrete gray values the value of *`BinSize`*
may cause the following effects:
For *`BinSize`* > *1* multiple neighboring gray values are
assigned to the same bin. If *`BinSize`* is no integer the gray values
are distributed uneven among the bins, e.g., for
*`BinSize`* = *1.5* the first and second gray value are
assigned to the first bin, the third gray value is assigned to the second
bin, and the fourth and fifth gray value are assigned to the third bin.
This becomes noticeable in several peeks in the histogram *`Histo`*.
If *`BinSize`* < *1* some classes are not assigned by any
gray value, e.g., for *`BinSize`* = *0.5* the first
gray value is assigned to the first bin and the second gray value is assigned
to the third bin. The histogram *`Histo`* shows some gaps, which
resembles the structure of a comb.

If the *`Image`* is of type *'real'* and
*`Min`* = *`Max`*, all pixels of the corresponding gray value
are assigned only to the first bin.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Region`** (input_object)  region `→` object

Region in which the histogram is to be calculated.

**`Image`** (input_object)  singlechannelimage `→` object (byte / cyclic / direction / int1 / uint2 / int2 / int4 / int8 / real)

Input image.

**`Min`** (input_control)  real `→`  (real / integer)

Minimum gray value.

Default:
0

Suggested values:
0

**`Max`** (input_control)  real `→`  (real / integer)

Maximum gray value.

Default:
255

Suggested values:
255

Restriction:
`Max >= Min`

**`NumBins`** (input_control)  integer `→`  (integer)

Number of bins.

Default:
256

Suggested values:
16, 32, 64, 128, 256

Restriction:
`NumBins >= 1`

**`Histo`** (output_control)  histogram(-array) `→`  (integer)

Histogram to be calculated.

**`BinSize`** (output_control)  real `→`  (real)

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
