# transform_dl_sample_batch (Operator)

## Name

`transform_dl_sample_batch` — Apply a pipeline of transforms on a set of images.

## Signature

`def transform_dl_sample_batch(transform_pipeline: HHandle, dlsample_batch: Sequence[HHandle]) -> Sequence[HHandle]`

## Description

`transform_dl_sample_batch` transforms a batch of samples
prior to their use in [`train_dl_model_batch`](train_dl_model_batch.md) and [`apply_dl_model`](apply_dl_model.md).
The transformations defined in *`transform_pipeline`* may include
adapting the image dimensions, scaling the gray value range, and applying data
augmentation methods.

Besides the image data keys `image` and `image_id` contained in
*`dlsample_batch`*, annotations are also transformed if present.
Currently, only keys for object detection models (including instance
segmentation) are supported.
The behavior for *"instance_type"* =
*"rectangle2"* can be influenced by the parameters
*"ignore_direction"* and *"class_ids_no_orientation"*,
see [`get_dl_transform_pipeline_param`](get_dl_transform_pipeline_param.md).
If *`dlsample_batch`* contains annotation keys for other model
types, an error may be raised.

In addition to transformed keys, *`dlresult_batch`* contains

- *"transformed_full_domain"*: Transformation of the
  rectangular full domain of the input image, clipped to output.
- *"back_transform"*: Transformation that can be used
  together with [`projective_trans_pixel`](projective_trans_pixel.md) or
  [`projective_trans_region`](projective_trans_region.md) to transform inference results of
  [`apply_dl_model`](apply_dl_model.md) back to the coordinate system of the original image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`transform_pipeline`** (input_control)  dl_transform_pipeline `→` HHandle

Transform pipeline handle.

**`dlsample_batch`** (input_control)  dict-array `→` Sequence[HHandle]

Input data.

**`dlresult_batch`** (output_control)  dict-array `→` Sequence[HHandle]

Result data.

## Possible Predecessors

`create_dl_transform_pipeline`

## Possible Successors

`train_dl_model_batch`,
`apply_dl_model`

## See also

`get_dl_transform_pipeline_param`,
`set_dl_transform_pipeline_param`

## Module

Foundation
