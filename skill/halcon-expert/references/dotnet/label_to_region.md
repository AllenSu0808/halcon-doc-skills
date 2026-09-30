# LabelToRegion (Operator)

## Name

`LabelToRegion` — Extract regions with equal gray values from an image.

## Signature

`static void HOperatorSet.LabelToRegion(HObject labelImage, out HObject regions)`

`HRegion HImage.LabelToRegion()`

## Description

`LabelToRegion` segments an image into regions of equal
gray value. One output region is generated for each gray value
occurring in the image. This is similar to calling
[`Threshold`](threshold.md) multiple times, and accumulating the results
with [`ConcatObj`](concat_obj.md). Another related operator is
[`Regiongrowing`](regiongrowing.md). However, `LabelToRegion`
does not perform a [`Connection`](connection.md) operation on the resulting
regions, i.e., they may be disconnected. A typical application of
`LabelToRegion` is the segmentation of label images,
hence its name.

The number of output regions is limited by the system parameter
*"max_outp_obj_par"*, which can be read via
`get_system(::'max_outp_obj_par':<number>)`.

## Attention

`LabelToRegion` is not implemented for images of type
`real`. The input images must not contain negative gray values.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`labelImage`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / int2 / int4 / int8)

Label image.

**`regions`** (output_object)  region-array `→` [HRegion](HRegion.md)

Regions having a constant gray value.

## Complexity

Let x1 be the minimum x-coordinate, x2 the maximum x-coordinate,
y1 be the minimum y-coordinate, and y2 the maximum y-coordinate
of a particular gray value. Furthermore, let N be the number of
different gray values in the image. Then the runtime complexity is
O(N * (x2 - x1 + 1) * (y2 - y1 + 1))

## Result

`LabelToRegion` returns 2 (
H_MSG_TRUE)
if the gray values lie
within a correct range. The behavior with respect to the input
images and output regions can be determined by setting the values of
the flags *"no_object_result"*,
*"empty_region_result"*, and *"store_empty_region"*
with [`SetSystem`](set_system.md). If necessary, an exception is raised.

## Possible Predecessors

`MinMaxGray`,
`SobelAmp`,
`BinomialFilter`,
`GaussFilter`,
`ReduceDomain`,
`DiffOfGauss`

## Possible Successors

`Connection`,
`Dilation1`,
`Erosion1`,
`Opening`,
`Closing`,
`RankRegion`,
`ShapeTrans`,
`Skeleton`

## See also

`Threshold`,
`ConcatObj`,
`Regiongrowing`,
`RegionToLabel`

## Module

Foundation
