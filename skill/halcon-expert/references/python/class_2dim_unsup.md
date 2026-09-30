# class_2dim_unsup (Operator)

## Name

`class_2dim_unsup` — Segment two images by clustering.

## Signature

`def class_2dim_unsup(image_1: HObject, image_2: HObject, threshold: int, num_classes: int) -> HObject`

## Description

`class_2dim_unsup` performs a classification with two
single-channel images. First, a two-dimensional histogram of the two
images is computed ([`histo_2dim`](histo_2dim.md)). In this histogram,
the first maximum is extracted; it serves as the first cluster
center. The histogram is computed with the intersection of the
domains of both images (see [`reduce_domain`](reduce_domain.md)). After this,
all pixels in the images that are at most *`threshold`*
pixels from the cluster center in the maximum norm, are determined.
These pixels form one output region. Next, the pixels thus
classified are deleted from the histogram so that they are not taken
into account for the next class. In this modified histogram, again
the maximum is extracted; it again serves as a cluster center. The
above steps are repeated *`num_classes`* times; thus,
*`num_classes`* output regions result. Only pixels defined in
both images are returned.

## Attention

Both input images must have the same size.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_1`** (input_object)  singlechannelimage `→` HObject (byte)

First input image.

**`image_2`** (input_object)  singlechannelimage `→` HObject (byte)

Second input image.

**`classes`** (output_object)  region-array `→` HObject

Classification result.

**`threshold`** (input_control)  integer `→` int

Threshold (maximum distance to the cluster's center).

Default:
15

Suggested values:
0, 2, 5, 8, 12, 17, 20, 30, 50, 70

**`num_classes`** (input_control)  integer `→` int

Number of classes (cluster centers).

Default:
5

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 30, 40, 50

## Result

`class_2dim_unsup` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior with respect to the input images and output regions
can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`set_system`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`decompose2`,
`decompose3`,
`median_image`,
`anisotropic_diffusion`,
`reduce_domain`

## Possible Successors

`select_shape`,
`select_gray`,
`connection`

## Alternatives

`threshold`,
`histo_2dim`,
`class_2dim_sup`,
`class_ndim_norm`

## Module

Foundation
