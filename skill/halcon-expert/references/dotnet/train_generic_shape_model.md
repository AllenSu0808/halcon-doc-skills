# TrainGenericShapeModel (Operator)

## Name

`TrainGenericShapeModel` — Train a shape model for matching.

## Signature

`static void HOperatorSet.TrainGenericShapeModel(HObject template, HTuple modelID)`

`void HShapeModel.TrainGenericShapeModel(HObject template)`

`void HImage.TrainGenericShapeModel(HShapeModel modelID)`

`void HXLDCont.TrainGenericShapeModel(HShapeModel modelID)`

## Description

The operator `TrainGenericShapeModel` trains the shape model
*`modelID`* in order to find the training pattern given in
*`template`*.

*`template`* accepts the training pattern to be of one of the following
types:

- **Image:** —

  The domain of the image given in *`template`* sets the ROI of the
  model. Which channels of a multichannel image are used depends on the
  model parameter *"metric"* (see
  [`SetGenericShapeModelParam`](set_generic_shape_model_param.md)).

  The model origin (reference point) is defined by the center of gravity of
  the image domain.
  The origin can be reset to a different point using
  [`SetGenericShapeModelParam`](set_generic_shape_model_param.md).
- **XLD contour:** —

  XLD contours passed in *`template`* should represent
  the gray value edges of the pattern to be searched.

  The model origin (reference point) is defined by the center of gravity of
  the smallest axis-parallel rectangle enclosing the contours.
  The origin can be reset to a different point using
  [`SetGenericShapeModelParam`](set_generic_shape_model_param.md).

Properties of the model *`modelID`* can be retrieved using
[`GetGenericShapeModelParam`](get_generic_shape_model_param.md) and modified using
[`SetGenericShapeModelParam`](set_generic_shape_model_param.md).
Note that after modifying certain parameters the model needs to be
(re)trained, see [`SetGenericShapeModelParam`](set_generic_shape_model_param.md).

Added training samples:
In case training samples have been added they are freed from the model after
a successful call of `TrainGenericShapeModel`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator supports canceling timeouts and interrupts.

This operator modifies the state of the following input parameter:

- modelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`template`** (input_object)  (multichannel-)object(-array) `→` [HObject](HObject.md)

Training image or xld.

**`modelID`** (input_control, state is modified)  shape_model `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the shape model.

## Result

If the parameters are valid, the operator
`TrainGenericShapeModel` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`CreateGenericShapeModel`,
`SetGenericShapeModelParam`

## Possible Successors

`FindGenericShapeModel`

## Module

Matching
