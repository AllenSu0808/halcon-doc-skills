# train_generic_shape_model (Operator)

## Name

`train_generic_shape_model` — Train a shape model for matching.

## Signature

`def train_generic_shape_model(template: HObject, model_id: HHandle) -> None`

## Description

The operator `train_generic_shape_model` trains the shape model
*`model_id`* in order to find the training pattern given in
*`template`*.

*`template`* accepts the training pattern to be of one of the following
types:

- **Image:** —

  The domain of the image given in *`template`* sets the ROI of the
  model. Which channels of a multichannel image are used depends on the
  model parameter *"metric"* (see
  [`set_generic_shape_model_param`](set_generic_shape_model_param.md)).

  The model origin (reference point) is defined by the center of gravity of
  the image domain.
  The origin can be reset to a different point using
  [`set_generic_shape_model_param`](set_generic_shape_model_param.md).
- **XLD contour:** —

  XLD contours passed in *`template`* should represent
  the gray value edges of the pattern to be searched.

  The model origin (reference point) is defined by the center of gravity of
  the smallest axis-parallel rectangle enclosing the contours.
  The origin can be reset to a different point using
  [`set_generic_shape_model_param`](set_generic_shape_model_param.md).

Properties of the model *`model_id`* can be retrieved using
[`get_generic_shape_model_param`](get_generic_shape_model_param.md) and modified using
[`set_generic_shape_model_param`](set_generic_shape_model_param.md).
Note that after modifying certain parameters the model needs to be
(re)trained, see [`set_generic_shape_model_param`](set_generic_shape_model_param.md).

Added training samples:
In case training samples have been added they are freed from the model after
a successful call of `train_generic_shape_model`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator supports canceling timeouts and interrupts.

This operator modifies the state of the following input parameter:

- model_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`template`** (input_object)  (multichannel-)object(-array) `→` HObject

Training image or xld.

**`model_id`** (input_control, state is modified)  shape_model `→` HHandle

Handle of the shape model.

## Result

If the parameters are valid, the operator
`train_generic_shape_model` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`create_generic_shape_model`,
`set_generic_shape_model_param`

## Possible Successors

`find_generic_shape_model`

## Module

Matching
