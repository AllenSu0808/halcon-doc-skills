# prepare_direct_variation_model (Operator)

## Name

`prepare_direct_variation_model` — Prepare a variation model for comparison with an image.

## Signature

`prepare_direct_variation_model(RefImage, VarImage : : ModelID, AbsThreshold, VarThreshold : )`

## Description

`prepare_direct_variation_model` prepares a variation model
for the image comparison with [`compare_variation_model`](compare_variation_model.md) or
[`compare_ext_variation_model`](compare_ext_variation_model.md). The variation model must have
been created with `Mode`=*'direct'* with
[`create_variation_model`](create_variation_model.md). In contrast to
[`prepare_variation_model`](prepare_variation_model.md), the ideal image of the object and
the corresponding variation image are not computed with
[`train_variation_model`](train_variation_model.md), but are specified directly in
*`RefImage`* and *`VarImage`*. This is useful if the
variation model should be created from a single image, as described
with [`create_variation_model`](create_variation_model.md). The variation image should
typically be created with edge operators like [`sobel_amp`](sobel_amp.md),
[`edges_image`](edges_image.md), or [`gray_range_rect`](gray_range_rect.md).

`prepare_direct_variation_model` converts the ideal image
*`RefImage`* and the variation image *`VarImage`* into two
threshold images and stores them in the variation model. These
threshold images are used in [`compare_variation_model`](compare_variation_model.md) or
[`compare_ext_variation_model`](compare_ext_variation_model.md) to perform the comparison of
the current image to the variation model.

Two thresholds are used to compute the threshold images. The
parameter *`AbsThreshold`* determines the minimum amount of
gray levels by which the image of the current object must differ
from the image of the ideal object. The parameter
*`VarThreshold`* determines a factor relative to the variation
image for the minimum difference of the current image and the ideal
image.
*`VarThreshold`* utilizes *`VarImage`* to define regions,
in which differences in gray values may occur which should not be
counted as errors.
This allows variations for specific parts of the object to inspect.
*`AbsThreshold`* and *`VarThreshold`* each can
contain one or two values. If two values are specified, different
thresholds can be determined for too bright and too dark pixels. In
this mode, the first value refers to too bright pixels, while the
second value refers to too dark pixels. If one value is specified,
this value refers to both the too bright and too dark pixels. Let
i(x,y) be the ideal image *`RefImage`*,
v(x,y) the variation image *`VarImage`*,
$a_{u}=\texttt{AbsThreshold}[0]$,
$a_{l}=\texttt{AbsThreshold}[1]$,
$b_{u}=\texttt{VarThreshold}[0]$,
and
$b_{l}=\texttt{VarThreshold}[1]$
(or $a_{u}=\texttt{AbsThreshold}$,
$a_{l}=\texttt{AbsThreshold}$,
$b_{u}=\texttt{VarThreshold}$, and
$b_{l}=\texttt{VarThreshold}$,
respectively). Then the two threshold images $t_{u,l}$
are computed as follows:
$$t_{u}(x,y)=i(x,y)+\max \{a_{u},b_{u}v(x,y)\}t_{l}(x,y)=i(x,y)-\max \{a_{l},b_{l}v(x,y)\}.$$
If the current image c(x,y) is compared to the
variation model using [`compare_variation_model`](compare_variation_model.md), the output
region contains all points that differ substantially from the model,
i.e., that fulfill the following condition:
$$c(x,y)>t_{u}(x,y)\vee c(x,y)<t_{l}(x,y).$$
In [`compare_ext_variation_model`](compare_ext_variation_model.md), extended comparison modes
are available, which return only too bright errors, only too dark
errors, or bright and dark errors as separate regions.

After the threshold images have been created they can be read out
with [`get_thresh_images_variation_model`](get_thresh_images_variation_model.md).

It should be noted that *`RefImage`* and *`VarImage`* are
not stored as the ideal and variation images in the model to save
memory in the model.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`RefImage`** (input_object)  singlechannelimage `→` object (byte / int2 / uint2)

Reference image of the object.

**`VarImage`** (input_object)  singlechannelimage `→` object (byte / int2 / uint2)

Variation image of the object.

**`ModelID`** (input_control, state is modified)  variation_model `→`  (handle)

ID of the variation model.

**`AbsThreshold`** (input_control)  number(-array) `→`  (real / integer)

Absolute minimum threshold for the differences
between the image and the variation model.

Default:
10

Suggested values:
0, 5, 10, 15, 20, 30, 40, 50

Restriction:
`AbsThreshold >= 0`

**`VarThreshold`** (input_control)  number(-array) `→`  (real / integer)

Threshold for the differences based on the variation
of the variation model.

Default:
2

Suggested values:
1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5

Restriction:
`VarThreshold >= 0`

## Example (HDevelop)

```
read_image (Image, 'model')
sobel_amp (Image, VarImage, 'sum_abs', 3)
get_image_pointer1 (Image, Pointer, Type, Width, Height)
create_variation_model (Width, Height, Type, 'direct', ModelID)
prepare_direct_variation_model (Image, VarImage, ModelID, 20, 1)
write_variation_model (ModelID, 'model.var')
```

## Result

`prepare_direct_variation_model` returns 2 (
H_MSG_TRUE)
if all
parameters are correct.

## Possible Predecessors

`sobel_amp`,
`edges_image`,
`gray_range_rect`

## Possible Successors

`compare_variation_model`,
`compare_ext_variation_model`,
`get_thresh_images_variation_model`,
`write_variation_model`

## Alternatives

`prepare_variation_model`

## See also

`create_variation_model`

## Module

Matching
