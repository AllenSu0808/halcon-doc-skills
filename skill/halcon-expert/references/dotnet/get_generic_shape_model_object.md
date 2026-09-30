# GetGenericShapeModelObject (Operator)

## Name

`GetGenericShapeModelObject` — Get iconic objects of the shape model.

## Signature

`static void HOperatorSet.GetGenericShapeModelObject(out HObject objectVal, HTuple modelID, HTuple genParamName)`

`HObject HShapeModel.GetGenericShapeModelObject(HTuple genParamName)`

## Description

The operator `GetGenericShapeModelObject` reads out objects
of the shape model *`modelID`* and returns them in *`objectVal`*.

*`genParamName`* specifies which iconic object will be returned.
The following values are possible:

- ***"clutter_region"*:** —

  The clutter region of the shape model.
- ***"contours"*:** —

  Representation of the shape model *`modelID`* for the bottom-most
  pyramid level as XLD contours. Thereby the contour is translated so that
  the origin of the model with the coordinates *"origin_row"* and
  *"origin_column"* (see [`SetGenericShapeModelParam`](set_generic_shape_model_param.md)) is
  located at the origin of the pixel centered HALCON standard coordinate system
  (see [Transformations / 2D Transformations](toc_transformations_2dtransformations.md)). The contours can be used,
  for example, to visualize the found instances of the model in an image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectVal`** (output_object)  (multichannel-)object(-array) `→` [HObject](HObject.md)

Iconic object to be returned.

**`modelID`** (input_control)  shape_model `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the shape model.

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Parameter names.

Default:
"clutter_region"

List of values:
"clutter_region", "contours"

## Result

If the parameters are valid, the operator
`GetGenericShapeModelObject` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`CreateGenericShapeModel`,
`SetGenericShapeModelObject`,
`TrainGenericShapeModel`

## Module

Matching
