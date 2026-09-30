# PrepareDirectVariationModel (Operator)

## Name

`PrepareDirectVariationModel` — Prepare a variation model for comparison with an image.

## Signature

`static void HOperatorSet.PrepareDirectVariationModel(HObject refImage, HObject varImage, HTuple modelID, HTuple absThreshold, HTuple varThreshold)`

`void HVariationModel.PrepareDirectVariationModel(HImage refImage, HImage varImage, HTuple absThreshold, HTuple varThreshold)`

`void HVariationModel.PrepareDirectVariationModel(HImage refImage, HImage varImage, double absThreshold, double varThreshold)`

## Description

`PrepareDirectVariationModel` prepares a variation model
for the image comparison with [`CompareVariationModel`](compare_variation_model.md) or
[`CompareExtVariationModel`](compare_ext_variation_model.md). The variation model must have
been created with `mode`=*"direct"* with
[`CreateVariationModel`](create_variation_model.md). In contrast to
[`PrepareVariationModel`](prepare_variation_model.md), the ideal image of the object and
the corresponding variation image are not computed with
[`TrainVariationModel`](train_variation_model.md), but are specified directly in
*`refImage`* and *`varImage`*. This is useful if the
variation model should be created from a single image, as described
with [`CreateVariationModel`](create_variation_model.md). The variation image should
typically be created with edge operators like [`SobelAmp`](sobel_amp.md),
[`EdgesImage`](edges_image.md), or [`GrayRangeRect`](gray_range_rect.md).

`PrepareDirectVariationModel` converts the ideal image
*`refImage`* and the variation image *`varImage`* into two
threshold images and stores them in the variation model. These
threshold images are used in [`CompareVariationModel`](compare_variation_model.md) or
[`CompareExtVariationModel`](compare_ext_variation_model.md) to perform the comparison of
the current image to the variation model.

Two thresholds are used to compute the threshold images. The
parameter *`absThreshold`* determines the minimum amount of
gray levels by which the image of the current object must differ
from the image of the ideal object. The parameter
*`varThreshold`* determines a factor relative to the variation
image for the minimum difference of the current image and the ideal
image.
*`varThreshold`* utilizes *`varImage`* to define regions,
in which differences in gray values may occur which should not be
counted as errors.
This allows variations for specific parts of the object to inspect.
*`absThreshold`* and *`varThreshold`* each can
contain one or two values. If two values are specified, different
thresholds can be determined for too bright and too dark pixels. In
this mode, the first value refers to too bright pixels, while the
second value refers to too dark pixels. If one value is specified,
this value refers to both the too bright and too dark pixels. Let
i(x,y) be the ideal image *`refImage`*,
v(x,y) the variation image *`varImage`*,
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
variation model using [`CompareVariationModel`](compare_variation_model.md), the output
region contains all points that differ substantially from the model,
i.e., that fulfill the following condition:
$$c(x,y)>t_{u}(x,y)\vee c(x,y)<t_{l}(x,y).$$
In [`CompareExtVariationModel`](compare_ext_variation_model.md), extended comparison modes
are available, which return only too bright errors, only too dark
errors, or bright and dark errors as separate regions.

After the threshold images have been created they can be read out
with [`GetThreshImagesVariationModel`](get_thresh_images_variation_model.md).

It should be noted that *`refImage`* and *`varImage`* are
not stored as the ideal and variation images in the model to save
memory in the model.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- modelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`refImage`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / int2 / uint2)

Reference image of the object.

**`varImage`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / int2 / uint2)

Variation image of the object.

**`modelID`** (input_control, state is modified)  variation_model `→` [HVariationModel](HVariationModel.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the variation model.

**`absThreshold`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Absolute minimum threshold for the differences
between the image and the variation model.

Default:
10

Suggested values:
0, 5, 10, 15, 20, 30, 40, 50

Restriction:
`AbsThreshold >= 0`

**`varThreshold`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

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

`PrepareDirectVariationModel` returns 2 (
H_MSG_TRUE)
if all
parameters are correct.

## Possible Predecessors

`SobelAmp`,
`EdgesImage`,
`GrayRangeRect`

## Possible Successors

`CompareVariationModel`,
`CompareExtVariationModel`,
`GetThreshImagesVariationModel`,
`WriteVariationModel`

## Alternatives

`PrepareVariationModel`

## See also

`CreateVariationModel`

## Module

Matching
