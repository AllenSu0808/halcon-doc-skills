# Histo2dim (Operator)

## Name

`Histo2dim` — Calculate the histogram of two-channel gray value images.

## Signature

`static void HOperatorSet.Histo2dim(HObject regions, HObject imageCol, HObject imageRow, out HObject histo2Dim)`

`HImage HImage.Histo2dim(HRegion regions, HImage imageRow)`

`HImage HRegion.Histo2dim(HImage imageCol, HImage imageRow)`

## Description

The operator `Histo2dim` calculates the 2-dimensional
histogram of two images within *`regions`*. The gray values
of channel 1 (*`imageCol`*) are interpreted as row index,
those of channel 2 (*`imageRow`*) as column index. The gray
value at one point P(g1,g2) in the output image
*`histo2Dim`* indicates the frequency of the gray value
combination (g1,g2) with g1 indicating the line index and g2
the column index.

## Attention

Note that the operator `Histo2dim` only considers
the given *`regions`* and ignores any previously set domain
of the input images.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region in which the histogram is to be calculated.

**`imageCol`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / direction / cyclic / int1)

Channel 1.

**`imageRow`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / direction / cyclic / int1)

Channel 2.

**`histo2Dim`** (output_object)  image `→` [HImage](HImage.md) (int4)

Histogram to be calculated.

## Example (HDevelop)

```
read_image(Image,'monkey')
get_domain (Image, Domain)
gauss_filter (Image, ImageGauss, 7)
histo_2dim(Domain,ImageGauss, Image,Histo2Dim)
dev_display(Histo2Dim)
```

## Complexity

If F is the plane of the region, the runtime complexity is
O(F + 256^2).

## Result

The operator `Histo2dim` returns the value 2 (
H_MSG_TRUE)
if both
images have defined gray values. The behavior in case of empty
input (no input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`, the behavior
in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Possible Predecessors

`Decompose3`,
`Decompose2`,
`DrawRegion`

## Possible Successors

`Threshold`,
`Class2dimSup`,
`Pouring`,
`LocalMax`,
`GraySkeleton`

## Alternatives

`GrayHisto`,
`GrayHistoAbs`

## See also

`GetGrayval`

## Module

Foundation
