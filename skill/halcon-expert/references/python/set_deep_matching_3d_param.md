# set_deep_matching_3d_param (Operator)

## Name

`set_deep_matching_3d_param` — Set a parameter of a Deep 3D Matching model.

## Signature

`def set_deep_matching_3d_param(deep_3dmatching_model: HHandle, gen_param_name: MaybeSequence[str], gen_param_value: HTupleType) -> None`

## Description

The operator `set_deep_matching_3d_param` sets the selected parameters
*`gen_param_name`* in the Deep 3D Matching model *`deep_3dmatching_model`* to
the values passed in *`gen_param_value`*.

The possible parameters are listed and described in
[`get_deep_matching_3d_param`](get_deep_matching_3d_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`deep_3dmatching_model`** (input_control)  deep_matching_3d `→` HHandle

Deep 3D Matching model.

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Name of parameter.

Default:
"min_score"

Suggested values:
"min_score", "num_matches", "min_num_views", "dl_model_detection", "dl_model_pose_estimation", "camera_parameter", "camera_pose", "delete_cameras", "sort_single_views_last"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` HTupleType

Value of parameter.

Default:
0.2

## Module

3D Metrology
