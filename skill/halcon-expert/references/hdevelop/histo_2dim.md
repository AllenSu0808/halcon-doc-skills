# histo_2dim (Operator)

## Name

`histo_2dim` — Calculate the histogram of two-channel gray value images.

## Signature

`histo_2dim(Regions, ImageCol, ImageRow : Histo2Dim : : )`

## Description

The operator `histo_2dim` calculates the 2-dimensional
histogram of two images within *`Regions`*. The gray values
of channel 1 (*`ImageCol`*) are interpreted as row index,
those of channel 2 (*`ImageRow`*) as column index. The gray
value at one point P(g1,g2) in the output image
*`Histo2Dim`* indicates the frequency of the gray value
combination (g1,g2) with g1 indicating the line index and g2
the column index.

## Attention

Note that the operator `histo_2dim` only considers
the given *`Regions`* and ignores any previously set domain
of the input images.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Region in which the histogram is to be calculated.

**`ImageCol`** (input_object)  (multichannel-)image `→` object (byte / direction / cyclic / int1)

Channel 1.

**`ImageRow`** (input_object)  (multichannel-)image `→` object (byte / direction / cyclic / int1)

Channel 2.

**`Histo2Dim`** (output_object)  image `→` object (int4)

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

The operator `histo_2dim` returns the value 2 (
H_MSG_TRUE)
if both
images have defined gray values. The behavior in case of empty
input (no input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`, the behavior
in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Possible Predecessors

`decompose3`,
`decompose2`,
`draw_region`

## Possible Successors

`threshold`,
`class_2dim_sup`,
`pouring`,
`local_max`,
`gray_skeleton`

## Alternatives

`gray_histo`,
`gray_histo_abs`

## See also

`get_grayval`

## Module

Foundation
