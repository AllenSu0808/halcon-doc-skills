# inspect_shape_model (Operator)

## Name

`inspect_shape_model` — Create the representation of a shape model.

## Signature

`def inspect_shape_model(image: HObject, num_levels: int, contrast: MaybeSequence[int]) -> Tuple[HObject, HObject]`

## Description

`inspect_shape_model` creates a representation of a shape
model. The operator is particularly useful in order to determine
the parameters *`num_levels`* and *`contrast`*, which are
used in [`create_shape_model`](create_shape_model.md),
[`create_scaled_shape_model`](create_scaled_shape_model.md), or
[`create_aniso_shape_model`](create_aniso_shape_model.md), quickly and conveniently. The
representation of the model is created on multiple image pyramid
levels, where the number of levels is determined by
*`num_levels`*. In contrast to [`create_shape_model`](create_shape_model.md),
[`create_scaled_shape_model`](create_scaled_shape_model.md), and
[`create_aniso_shape_model`](create_aniso_shape_model.md), the model is only created for the
rotation and scale of the object in the input image, i.e.,
0° and 1. As output, `inspect_shape_model`
creates an image object *`model_images`* containing the images
of the individual levels of the image pyramid as well as a region in
*`model_regions`* for each pyramid level that represents the
model at the respective pyramid level. The individual objects can
be accessed with [`select_obj`](select_obj.md). If the input image
*`image`* has one channel the representation of the model is
created with the method that is used in [`create_shape_model`](create_shape_model.md),
[`create_scaled_shape_model`](create_scaled_shape_model.md) or
[`create_aniso_shape_model`](create_aniso_shape_model.md) for the metrics
*"use_polarity"*, *"ignore_global_polarity"*, and
*"ignore_local_polarity"*. If the input image has more than
one channel the representation is created with the method that is
used for the metric *"ignore_color_polarity"*. As described
for [`create_shape_model`](create_shape_model.md), [`create_scaled_shape_model`](create_scaled_shape_model.md),
and [`create_aniso_shape_model`](create_aniso_shape_model.md), the number of pyramid levels
should be chosen as large as possible, while taking into account
that the model must be recognizable on the highest pyramid level and
must have enough model points. The parameter *`contrast`*
should be chosen such that only the significant features of the
template object are used for the model. *`contrast`* can also
contain a tuple with two values. In this case, the model is
segmented using a method similar to the hysteresis threshold method
used in [`edges_image`](edges_image.md). Here, the first element of the tuple
determines the lower threshold, while the second element determines
the upper threshold. For more information about the hysteresis
threshold method, see [`hysteresis_threshold`](hysteresis_threshold.md). Optionally,
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
`inspect_shape_model` is called interactively multiple times
with different parameters for *`num_levels`* and
*`contrast`*, until a satisfactory model is obtained. After
this, [`create_shape_model`](create_shape_model.md), [`create_scaled_shape_model`](create_scaled_shape_model.md),
or [`create_aniso_shape_model`](create_aniso_shape_model.md) are called with the parameters
thus obtained.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / uint2)

Input image.

**`model_images`** (output_object)  (multichannel-)image-array `→` HObject (byte / uint2)

Image pyramid of the input image

**`model_regions`** (output_object)  region-array `→` HObject

Model region pyramid

**`num_levels`** (input_control)  integer `→` int

Number of pyramid levels.

Default:
4

List of values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

**`contrast`** (input_control)  number(-array) `→` MaybeSequence[int]

Threshold or hysteresis thresholds for the contrast
of the object in the image and optionally minimum
size of the object parts.

Default:
30

Suggested values:
10, 20, 30, 40, 60, 80, 100, 120, 140, 160

## Result

If the parameters are valid, the operator
`inspect_shape_model` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`reduce_domain`

## Possible Successors

`select_obj`

## See also

`set_generic_shape_model_param`

## Module

Foundation
