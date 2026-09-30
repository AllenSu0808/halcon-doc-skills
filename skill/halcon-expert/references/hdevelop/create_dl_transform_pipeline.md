# create_dl_transform_pipeline (Operator)

## Name

`create_dl_transform_pipeline` — Create a pipeline of transforms for the training of a deep learning model.

## Signature

`create_dl_transform_pipeline( : : Transforms, GenParamName, GenParamValue : TransformPipeline)`

## Description

The operator `create_dl_transform_pipeline` creates a pipeline of
transforms *`Transforms`* for transforming a batch of samples
prior to their use in [`train_dl_model_batch`](train_dl_model_batch.md) and [`apply_dl_model`](apply_dl_model.md).
Transforms may include adaptation of image dimensions or gray value range
as well as augmentation methods.

The execution order of the transforms is defined by their order in the
tuple *`Transforms`*. The execution is performed with the operator
[`transform_dl_sample_batch`](transform_dl_sample_batch.md).

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'fill_value'*:** —

  Value used to fill the padded regions if required by the transforms.

  Restriction:
  Only values of type integer or float are allowed.

  Default:
   *0.0*.
- ***'bbox_min_side_length'*:** —

  Minimum allowed side length of a transformed box instance. Smaller
  box instances are not transferred to output.

  Default:
   *2*
- ***'instance_min_visibility'*:** —

  Minimum allowed visibility fraction of a transformed instance.
  Instances with lower visibility are not transferred to output.

  Default:
   *0.5*
- ***'ignore_direction'*:** —

  Determines whether directions of oriented bounding boxes shall be
  used (*'false'*) or ignored (*'true'*).
  Only for transformation of samples for detection models of
  *'instance_type'* = *'rectangle2'*.

  List of values:
   *'true'*, *'false'*

  Default:
   *'false'*

Note that additionally *'class_ids_no_orientation'* can be set
using [`set_dl_transform_pipeline_param`](set_dl_transform_pipeline_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Transforms`** (input_control)  dl_transform(-array) `→`  (handle)

Tuple with the transform handles

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Names of the generic parameters that can be adjusted
for the transform pipeline.

Default:
[]

List of values:
'bbox_min_side_length', 'fill_value', 'ignore_direction', 'instance_min_visibility'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (real / integer)

Values of the generic parameters that can be adjusted
for the transform pipeline.

Default:
[]

Suggested values:
0.0

**`TransformPipeline`** (output_control)  dl_transform_pipeline `→`  (handle)

Transform pipeline handle

## Possible Predecessors

`create_dl_transform_flip`,
`create_dl_transform_normalize`,
`create_dl_transform_random_crop`,
`create_dl_transform_random_geometric`,
`create_dl_transform_random_hsv`,
`create_dl_transform_resize`

## Possible Successors

`get_dl_transform_pipeline_param`,
`set_dl_transform_pipeline_param`,
`transform_dl_sample_batch`

## Module

Foundation
