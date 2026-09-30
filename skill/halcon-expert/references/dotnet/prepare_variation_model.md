# PrepareVariationModel (Operator)

## Name

`PrepareVariationModel` — Prepare a variation model for comparison with an image.

## Signature

`static void HOperatorSet.PrepareVariationModel(HTuple modelID, HTuple absThreshold, HTuple varThreshold)`

`void HVariationModel.PrepareVariationModel(HTuple absThreshold, HTuple varThreshold)`

`void HVariationModel.PrepareVariationModel(double absThreshold, double varThreshold)`

## Description

`PrepareVariationModel` prepares a variation model for the
image comparison with [`CompareVariationModel`](compare_variation_model.md) or
[`CompareExtVariationModel`](compare_ext_variation_model.md). This is done by converting the
ideal image and the variation image that have been trained with
[`TrainVariationModel`](train_variation_model.md) into two threshold images and storing
them in the variation model. These threshold images are used in
[`CompareVariationModel`](compare_variation_model.md) or
[`CompareExtVariationModel`](compare_ext_variation_model.md) to speed up the comparison of
the current image to the variation model.

Two thresholds are used to compute the threshold images. The
parameter *`absThreshold`* determines the minimum amount of
gray levels by which the image of the current object must differ
from the image of the ideal object. The parameter
*`varThreshold`* determines a factor relative to the variation
image for the minimum difference of the current image and the ideal
image. *`absThreshold`* and *`varThreshold`* each can
contain one or two values. If two values are specified, different
thresholds can be determined for too bright and too dark pixels. In
this mode, the first value refers to too bright pixels, while the
second value refers to too dark pixels. If one value is specified,
this value refers to both the too bright and too dark pixels. Let
i(x,y) be the ideal image, v(x,y) the
variation image,
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
with [`GetThreshImagesVariationModel`](get_thresh_images_variation_model.md). Furthermore, the
training data can be deleted with
[`ClearTrainDataVariationModel`](clear_train_data_variation_model.md) to save memory.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- modelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

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

## Result

`PrepareVariationModel` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`TrainVariationModel`

## Possible Successors

`CompareVariationModel`,
`CompareExtVariationModel`,
`GetThreshImagesVariationModel`,
`ClearTrainDataVariationModel`,
`WriteVariationModel`

## Alternatives

`PrepareDirectVariationModel`

## See also

`CreateVariationModel`

## Module

Matching
