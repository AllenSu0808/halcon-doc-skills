# class_2dim_sup (Operator)

## Name

`class_2dim_sup` — Segment an image using two-dimensional pixel classification.

## Signature

`def class_2dim_sup(image_col: HObject, image_row: HObject, feature_space: HObject) -> HObject`

## Description

`class_2dim_sup` classifies the points in two-channel images
using a two-dimensional feature space. For each point, two gray
values (one from each image) are used as features. The feature
space is represented by the input region. The classification is
done as follows:

A point from the input region of an image is accepted if the point
$(g_{r},g_{c})$, which is determined by the respective gray
values, is contained in the region *`feature_space`*. $g_{r}$
is here a gray value from the image *`image_row`*, while $g_{c}$
is the corresponding gray value from *`image_col`*.

Let $P$ be a point with the coordinates $P=(R,C)$,
$g_{r}$ be the
gray value at position $(R,C)$ in the image *`image_row`*, and
$g_{c}$ be the gray value at position $(R,C)$ in the image
*`image_col`*. Then the point $P$ is aggregated into the
output region if
$$(g_{r},g_{c})\in\texttt{FeatureSpace}$$
$g_{r}$ is interpreted as row coordinate and $g_{c}$ as
column coordinate.

For the generation of *`feature_space`*, see
[`histo_2dim`](histo_2dim.md). The feature space can be modified by
applying region transformation operators, such as [`rank_region`](rank_region.md),
[`dilation1`](dilation1.md), [`shape_trans`](shape_trans.md),
[`elliptic_axis`](elliptic_axis.md), etc., before calling
`class_2dim_sup`.

The parameters *`image_col`* and *`image_row`* must
contain an equal number of images with the same size.
The image points are taken from the intersection of the domains of
both images (see [`reduce_domain`](reduce_domain.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image_col`** (input_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1)

Input image (first channel).

**`image_row`** (input_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1)

Input image (second channel).

**`feature_space`** (input_object)  region(-array) `→` HObject

Region defining the feature space.

**`region_class_2dim`** (output_object)  region(-array) `→` HObject

Classified regions.

## Complexity

Let A be the area of the input region. Then the runtime
complexity is O(256^2 + A).

## Result

`class_2dim_sup` returns 2 (
H_MSG_TRUE)
. If all parameters are correct, the
behavior with respect to the input images and output regions can be
determined by setting the values of the flags *"no_object_result"*,
*"empty_region_result"*, and *"store_empty_region"*
with [`set_system`](set_system.md). If necessary, an exception is raised.

## Possible Predecessors

`histo_2dim`,
`threshold`,
`draw_region`,
`dilation1`,
`opening`,
`shape_trans`

## Possible Successors

`connection`,
`select_shape`,
`select_gray`

## Alternatives

`class_ndim_norm`,
`threshold`

## See also

`histo_2dim`

## Module

Foundation
