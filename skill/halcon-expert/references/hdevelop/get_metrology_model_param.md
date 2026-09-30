# get_metrology_model_param (Operator)

## Name

`get_metrology_model_param` — Get parameters that are valid for the entire metrology model.

## Signature

`get_metrology_model_param( : : MetrologyHandle, GenParamName : GenParamValue)`

## Description

`get_metrology_model_param` queries parameters that are
valid for the entire metrology model.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by
the handle *`MetrologyHandle`*.

The following generic parameter names for *`GenParamName`*
are possible:

- ***'camera_param'*:** —

  The internal
  camera parameters that are set for the metrology model.
- ***'plane_pose'*:** —

  The 3D pose of the
  measurement plane that is set for the metrology model. The 3D pose is
  given in camera coordinates.
- ***'reference_system'*:** —

  The rotation and translation of the current
  reference coordinate system with respect to the image coordinate system.
  The tuple returned in *`GenParamValue`* contains [row, column, angle].
- ***'scale'*:** —

  The scaling factor or
  unit of the results of the measurement returned by
  [`get_metrology_object_result`](get_metrology_object_result.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MetrologyHandle`** (input_control)  metrology_model `→`  (handle)

Handle of the metrology model.

**`GenParamName`** (input_control)  attribute.name `→`  (string)

Name of the generic parameter.

Default:
'camera_param'

List of values:
'camera_param', 'plane_pose', 'reference_system', 'scale'

**`GenParamValue`** (output_control)  attribute.value(-array) `→`  (string / real / integer)

Value of the generic parameter.

## Result

If the parameters are valid, the operator
`get_metrology_model_param` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`get_metrology_object_indices`,
`set_metrology_model_param`

## Possible Successors

`get_metrology_object_param`

## See also

`get_metrology_object_param`,
`get_metrology_object_num_instances`

## Module

2D Metrology
