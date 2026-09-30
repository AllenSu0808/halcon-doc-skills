# GetMetrologyModelParam (Operator)

## Name

`GetMetrologyModelParam` — Get parameters that are valid for the entire metrology model.

## Signature

`static void HOperatorSet.GetMetrologyModelParam(HTuple metrologyHandle, HTuple genParamName, out HTuple genParamValue)`

`HTuple HMetrologyModel.GetMetrologyModelParam(string genParamName)`

## Description

`GetMetrologyModelParam` queries parameters that are
valid for the entire metrology model.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by
the handle *`metrologyHandle`*.

The following generic parameter names for *`genParamName`*
are possible:

- ***"camera_param"*:** —

  The internal
  camera parameters that are set for the metrology model.
- ***"plane_pose"*:** —

  The 3D pose of the
  measurement plane that is set for the metrology model. The 3D pose is
  given in camera coordinates.
- ***"reference_system"*:** —

  The rotation and translation of the current
  reference coordinate system with respect to the image coordinate system.
  The tuple returned in *`genParamValue`* contains [row, column, angle].
- ***"scale"*:** —

  The scaling factor or
  unit of the results of the measurement returned by
  [`GetMetrologyObjectResult`](get_metrology_object_result.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`metrologyHandle`** (input_control)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

**`genParamName`** (input_control)  attribute.name `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter.

Default:
"camera_param"

List of values:
"camera_param", "plane_pose", "reference_system", "scale"

**`genParamValue`** (output_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long)

Value of the generic parameter.

## Result

If the parameters are valid, the operator
`GetMetrologyModelParam` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`GetMetrologyObjectIndices`,
`SetMetrologyModelParam`

## Possible Successors

`GetMetrologyObjectParam`

## See also

`GetMetrologyObjectParam`,
`GetMetrologyObjectNumInstances`

## Module

2D Metrology
