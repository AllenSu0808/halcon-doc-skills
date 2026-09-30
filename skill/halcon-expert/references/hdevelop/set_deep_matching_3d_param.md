# set_deep_matching_3d_param (Operator)

## Name

`set_deep_matching_3d_param` — Set a parameter of a Deep 3D Matching model.

## Signature

`set_deep_matching_3d_param( : : Deep3DMatchingModel, GenParamName, GenParamValue : )`

## Description

The operator `set_deep_matching_3d_param` sets the selected parameters
*`GenParamName`* in the Deep 3D Matching model *`Deep3DMatchingModel`* to
the values passed in *`GenParamValue`*.

The possible parameters are listed and described in
[`get_deep_matching_3d_param`](get_deep_matching_3d_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Deep3DMatchingModel`** (input_control)  deep_matching_3d `→`  (handle)

Deep 3D Matching model.

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Name of parameter.

Default:
'min_score'

Suggested values:
'min_score', 'num_matches', 'min_num_views', 'dl_model_detection', 'dl_model_pose_estimation', 'camera_parameter', 'camera_pose', 'delete_cameras', 'sort_single_views_last'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / real / integer / handle)

Value of parameter.

Default:
0.2

## Module

3D Metrology
