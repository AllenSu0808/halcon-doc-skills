# histo_2dim (Operator)

## Name

`histo_2dim` — Calculate the histogram of two-channel gray value images.

## Signature

`def histo_2dim(regions: HObject, image_col: HObject, image_row: HObject) -> HObject`

## Description

The operator `histo_2dim` calculates the 2-dimensional
histogram of two images within *`regions`*. The gray values
of channel 1 (*`image_col`*) are interpreted as row index,
those of channel 2 (*`image_row`*) as column index. The gray
value at one point P(g1,g2) in the output image
*`histo_2dim`* indicates the frequency of the gray value
combination (g1,g2) with g1 indicating the line index and g2
the column index.

## Attention

Note that the operator `histo_2dim` only considers
the given *`regions`* and ignores any previously set domain
of the input images.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Region in which the histogram is to be calculated.

**`image_col`** (input_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1)

Channel 1.

**`image_row`** (input_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1)

Channel 2.

**`histo_2dim`** (output_object)  image `→` HObject (int4)

Histogram to be calculated.

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
