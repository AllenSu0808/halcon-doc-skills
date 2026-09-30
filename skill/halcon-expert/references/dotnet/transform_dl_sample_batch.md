# TransformDlSampleBatch (Operator)

## Name

`TransformDlSampleBatch` — Apply a pipeline of transforms on a set of images.

## Signature

`static void HOperatorSet.TransformDlSampleBatch(HTuple transformPipeline, HTuple DLSampleBatch, out HTuple DLResultBatch)`

`HDict[] HDlTransformPipeline.TransformDlSampleBatch(HDict[] DLSampleBatch)`

## Description

`TransformDlSampleBatch` transforms a batch of samples
prior to their use in [`TrainDlModelBatch`](train_dl_model_batch.md) and [`ApplyDlModel`](apply_dl_model.md).
The transformations defined in *`transformPipeline`* may include
adapting the image dimensions, scaling the gray value range, and applying data
augmentation methods.

Besides the image data keys `image` and `image_id` contained in
*`DLSampleBatch`*, annotations are also transformed if present.
Currently, only keys for object detection models (including instance
segmentation) are supported.
The behavior for *"instance_type"* =
*"rectangle2"* can be influenced by the parameters
*"ignore_direction"* and *"class_ids_no_orientation"*,
see [`GetDlTransformPipelineParam`](get_dl_transform_pipeline_param.md).
If *`DLSampleBatch`* contains annotation keys for other model
types, an error may be raised.

In addition to transformed keys, *`DLResultBatch`* contains

- *"transformed_full_domain"*: Transformation of the
  rectangular full domain of the input image, clipped to output.
- *"back_transform"*: Transformation that can be used
  together with [`ProjectiveTransPixel`](projective_trans_pixel.md) or
  [`ProjectiveTransRegion`](projective_trans_region.md) to transform inference results of
  [`ApplyDlModel`](apply_dl_model.md) back to the coordinate system of the original image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`transformPipeline`** (input_control)  dl_transform_pipeline `→` [HDlTransformPipeline](HDlTransformPipeline.md), [HTuple](HTuple.md) (*IntPtr*)

Transform pipeline handle.

**`DLSampleBatch`** (input_control)  dict-array `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Input data.

**`DLResultBatch`** (output_control)  dict-array `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Result data.

## Possible Predecessors

`CreateDlTransformPipeline`

## Possible Successors

`TrainDlModelBatch`,
`ApplyDlModel`

## See also

`GetDlTransformPipelineParam`,
`SetDlTransformPipelineParam`

## Module

Foundation
