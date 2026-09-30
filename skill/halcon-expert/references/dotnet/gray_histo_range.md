# GrayHistoRange (Operator)

## Name

`GrayHistoRange` — Calculate the gray value distribution of a single channel image within a
certain gray value range.

## Signature

`static void HOperatorSet.GrayHistoRange(HObject region, HObject image, HTuple min, HTuple max, HTuple numBins, out HTuple histo, out HTuple binSize)`

`HTuple HImage.GrayHistoRange(HRegion region, HTuple min, HTuple max, int numBins, out double binSize)`

`int HImage.GrayHistoRange(HRegion region, double min, double max, int numBins, out double binSize)`

`HTuple HRegion.GrayHistoRange(HImage image, HTuple min, HTuple max, int numBins, out double binSize)`

`int HRegion.GrayHistoRange(HImage image, double min, double max, int numBins, out double binSize)`

## Description

`GrayHistoRange` calculates the gray value distribution
*`histo`* of the single channel *`image`* within *`region`*
and the gray value range [*`min`*,*`max`*]. The values for
*`min`* and *`max`* are rounded down to the next integer if the
*`image`* is not of type *"real"*. The gray value range is divided
into *`numBins`* bins of the same size, which is returned in
*`binSize`*. If a gray value lies between two bins the gray value is
assigned to the smaller bin. If the *`image`* is of type *"real"*
$BinSize = \frac{Max-Min}{NumBins}$ ![figure](../assets/e77fbd30d3031e66.svg).
If the *`image`* has discrete gray values the size of a bin is
computed with
$BinSize = \frac{Max-Min+1}{NumBins}$ ![figure](../assets/a71e09270487a639.svg). Since the accuracy of the histogram *`histo`* can
be adjusted with *`numBins`*, the calculation of the gray value
histogram with `GrayHistoRange` is most useful for images of type
*"real"* and images of type *"integer"*, which have
a high bit depth.

## Attention

Note that the operator `GrayHistoRange` only considers
the given *`region`* and ignores any previously set domain
of the input image *`image`*.

If the *`image`* has discrete gray values the value of *`binSize`*
may cause the following effects:
For *`binSize`* > *1* multiple neighboring gray values are
assigned to the same bin. If *`binSize`* is no integer the gray values
are distributed uneven among the bins, e.g., for
*`binSize`* = *1.5* the first and second gray value are
assigned to the first bin, the third gray value is assigned to the second
bin, and the fourth and fifth gray value are assigned to the third bin.
This becomes noticeable in several peeks in the histogram *`histo`*.
If *`binSize`* < *1* some classes are not assigned by any
gray value, e.g., for *`binSize`* = *0.5* the first
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

**`region`** (input_object)  region `→` [HRegion](HRegion.md)

Region in which the histogram is to be calculated.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / cyclic / direction / int1 / uint2 / int2 / int4 / int8 / real)

Input image.

**`min`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Minimum gray value.

Default:
0

Suggested values:
0

**`max`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum gray value.

Default:
255

Suggested values:
255

Restriction:
`Max >= Min`

**`numBins`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of bins.

Default:
256

Suggested values:
16, 32, 64, 128, 256

Restriction:
`NumBins >= 1`

**`histo`** (output_control)  histogram(-array) `→` [HTuple](HTuple.md) (*int* / long)

Histogram to be calculated.

**`binSize`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Bin size.

## Result

If the parameters are valid, the operator `GrayHistoRange`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`MinMaxGray`

## Possible Successors

`CreateFunct1dArray`

## Alternatives

`GrayHisto`,
`GrayHistoAbs`

## See also

`Histo2dim`,
`ScaleImageMax`

## Module

Foundation
