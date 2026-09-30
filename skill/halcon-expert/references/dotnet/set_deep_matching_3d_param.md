# SetDeepMatching3dParam (Operator)

## Name

`SetDeepMatching3dParam` — Set a parameter of a Deep 3D Matching model.

## Signature

`static void HOperatorSet.SetDeepMatching3dParam(HTuple deep3DMatchingModel, HTuple genParamName, HTuple genParamValue)`

`void HDeepMatching3D.SetDeepMatching3dParam(HTuple genParamName, HTuple genParamValue)`

`void HDeepMatching3D.SetDeepMatching3dParam(string genParamName, string genParamValue)`

## Description

The operator `SetDeepMatching3dParam` sets the selected parameters
*`genParamName`* in the Deep 3D Matching model *`deep3DMatchingModel`* to
the values passed in *`genParamValue`*.

The possible parameters are listed and described in
[`GetDeepMatching3dParam`](get_deep_matching_3d_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`deep3DMatchingModel`** (input_control)  deep_matching_3d `→` [HDeepMatching3D](HDeepMatching3D.md), [HTuple](HTuple.md) (*IntPtr*)

Deep 3D Matching model.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Name of parameter.

Default:
"min_score"

Suggested values:
"min_score", "num_matches", "min_num_views", "dl_model_detection", "dl_model_pose_estimation", "camera_parameter", "camera_pose", "delete_cameras", "sort_single_views_last"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long / HHandle)

Value of parameter.

Default:
0.2

## Module

3D Metrology
