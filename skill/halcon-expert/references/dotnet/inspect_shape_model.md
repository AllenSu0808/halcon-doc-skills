# InspectShapeModel (Operator)

## Name

`InspectShapeModel` — Create the representation of a shape model.

## Signature

`static void HOperatorSet.InspectShapeModel(HObject image, out HObject modelImages, out HObject modelRegions, HTuple numLevels, HTuple contrast)`

`HImage HImage.InspectShapeModel(out HRegion modelRegions, int numLevels, HTuple contrast)`

`HImage HImage.InspectShapeModel(out HRegion modelRegions, int numLevels, int contrast)`

## Description

`InspectShapeModel` creates a representation of a shape
model. The operator is particularly useful in order to determine
the parameters *`numLevels`* and *`contrast`*, which are
used in [`CreateShapeModel`](create_shape_model.md),
[`CreateScaledShapeModel`](create_scaled_shape_model.md), or
[`CreateAnisoShapeModel`](create_aniso_shape_model.md), quickly and conveniently. The
representation of the model is created on multiple image pyramid
levels, where the number of levels is determined by
*`numLevels`*. In contrast to [`CreateShapeModel`](create_shape_model.md),
[`CreateScaledShapeModel`](create_scaled_shape_model.md), and
[`CreateAnisoShapeModel`](create_aniso_shape_model.md), the model is only created for the
rotation and scale of the object in the input image, i.e.,
0° and 1. As output, `InspectShapeModel`
creates an image object *`modelImages`* containing the images
of the individual levels of the image pyramid as well as a region in
*`modelRegions`* for each pyramid level that represents the
model at the respective pyramid level. The individual objects can
be accessed with [`SelectObj`](select_obj.md). If the input image
*`image`* has one channel the representation of the model is
created with the method that is used in [`CreateShapeModel`](create_shape_model.md),
[`CreateScaledShapeModel`](create_scaled_shape_model.md) or
[`CreateAnisoShapeModel`](create_aniso_shape_model.md) for the metrics
*"use_polarity"*, *"ignore_global_polarity"*, and
*"ignore_local_polarity"*. If the input image has more than
one channel the representation is created with the method that is
used for the metric *"ignore_color_polarity"*. As described
for [`CreateShapeModel`](create_shape_model.md), [`CreateScaledShapeModel`](create_scaled_shape_model.md),
and [`CreateAnisoShapeModel`](create_aniso_shape_model.md), the number of pyramid levels
should be chosen as large as possible, while taking into account
that the model must be recognizable on the highest pyramid level and
must have enough model points. The parameter *`contrast`*
should be chosen such that only the significant features of the
template object are used for the model. *`contrast`* can also
contain a tuple with two values. In this case, the model is
segmented using a method similar to the hysteresis threshold method
used in [`EdgesImage`](edges_image.md). Here, the first element of the tuple
determines the lower threshold, while the second element determines
the upper threshold. For more information about the hysteresis
threshold method, see [`HysteresisThreshold`](hysteresis_threshold.md). Optionally,
*`contrast`* can contain a third value as the last element of
the tuple. This value determines a threshold for the selection of
significant model components based on the size of the components,
i.e., components that have fewer points than the minimum size thus
specified are suppressed. As the minimum size is applied on the
extent of the components, the derived model contours can still be
smaller than the specified minimum size. This threshold for the minimum
size is divided by two for each successive pyramid level. If small model
components should be suppressed, but hysteresis thresholding should
not be performed, nevertheless three values must be specified in
*`contrast`*. In this case, the first two values can simply be
set to identical values. In its typical use,
`InspectShapeModel` is called interactively multiple times
with different parameters for *`numLevels`* and
*`contrast`*, until a satisfactory model is obtained. After
this, [`CreateShapeModel`](create_shape_model.md), [`CreateScaledShapeModel`](create_scaled_shape_model.md),
or [`CreateAnisoShapeModel`](create_aniso_shape_model.md) are called with the parameters
thus obtained.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2)

Input image.

**`modelImages`** (output_object)  (multichannel-)image-array `→` [HImage](HImage.md) (byte / uint2)

Image pyramid of the input image

**`modelRegions`** (output_object)  region-array `→` [HRegion](HRegion.md)

Model region pyramid

**`numLevels`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of pyramid levels.

Default:
4

List of values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

**`contrast`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

Threshold or hysteresis thresholds for the contrast
of the object in the image and optionally minimum
size of the object parts.

Default:
30

Suggested values:
10, 20, 30, 40, 60, 80, 100, 120, 140, 160

## Result

If the parameters are valid, the operator
`InspectShapeModel` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`ReduceDomain`

## Possible Successors

`SelectObj`

## See also

`SetGenericShapeModelParam`

## Module

Foundation
