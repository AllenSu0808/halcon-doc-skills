# CreateDlTransformPipeline (Operator)

## Name

`CreateDlTransformPipeline` — Create a pipeline of transforms for the training of a deep learning model.

## Signature

`static void HOperatorSet.CreateDlTransformPipeline(HTuple transforms, HTuple genParamName, HTuple genParamValue, out HTuple transformPipeline)`

`static HDlTransformPipeline HDlTransform.CreateDlTransformPipeline(HDlTransform[] transforms, HTuple genParamName, HTuple genParamValue)`

`HDlTransformPipeline HDlTransform.CreateDlTransformPipeline(HTuple genParamName, HTuple genParamValue)`

`public HDlTransformPipeline(HDlTransform[] transforms, HTuple genParamName, HTuple genParamValue)`

`public HDlTransformPipeline(HDlTransform transforms, HTuple genParamName, HTuple genParamValue)`

`void HDlTransformPipeline.CreateDlTransformPipeline(HDlTransform[] transforms, HTuple genParamName, HTuple genParamValue)`

`void HDlTransformPipeline.CreateDlTransformPipeline(HDlTransform transforms, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `CreateDlTransformPipeline` creates a pipeline of
transforms *`transforms`* for transforming a batch of samples
prior to their use in [`TrainDlModelBatch`](train_dl_model_batch.md) and [`ApplyDlModel`](apply_dl_model.md).
Transforms may include adaptation of image dimensions or gray value range
as well as augmentation methods.

The execution order of the transforms is defined by their order in the
tuple *`transforms`*. The execution is performed with the operator
[`TransformDlSampleBatch`](transform_dl_sample_batch.md).

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

- ***"fill_value"*:** —

  Value used to fill the padded regions if required by the transforms.

  Restriction:
  Only values of type integer or float are allowed.

  Default:
   *0.0*.
- ***"bbox_min_side_length"*:** —

  Minimum allowed side length of a transformed box instance. Smaller
  box instances are not transferred to output.

  Default:
   *2*
- ***"instance_min_visibility"*:** —

  Minimum allowed visibility fraction of a transformed instance.
  Instances with lower visibility are not transferred to output.

  Default:
   *0.5*
- ***"ignore_direction"*:** —

  Determines whether directions of oriented bounding boxes shall be
  used (*"false"*) or ignored (*"true"*).
  Only for transformation of samples for detection models of
  *"instance_type"* = *"rectangle2"*.

  List of values:
   *"true"*, *"false"*

  Default:
   *"false"*

Note that additionally *"class_ids_no_orientation"* can be set
using [`SetDlTransformPipelineParam`](set_dl_transform_pipeline_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`transforms`** (input_control)  dl_transform(-array) `→` [HDlTransform](HDlTransform.md), [HTuple](HTuple.md) (*IntPtr*)

Tuple with the transform handles

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters that can be adjusted
for the transform pipeline.

Default:
[]

List of values:
"bbox_min_side_length", "fill_value", "ignore_direction", "instance_min_visibility"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*double* / int / long)

Values of the generic parameters that can be adjusted
for the transform pipeline.

Default:
[]

Suggested values:
0.0

**`transformPipeline`** (output_control)  dl_transform_pipeline `→` [HDlTransformPipeline](HDlTransformPipeline.md), [HTuple](HTuple.md) (*IntPtr*)

Transform pipeline handle

## Possible Predecessors

`CreateDlTransformFlip`,
`CreateDlTransformNormalize`,
`CreateDlTransformRandomCrop`,
`CreateDlTransformRandomGeometric`,
`CreateDlTransformRandomHsv`,
`CreateDlTransformResize`

## Possible Successors

`GetDlTransformPipelineParam`,
`SetDlTransformPipelineParam`,
`TransformDlSampleBatch`

## Module

Foundation
