# RefineSurfaceModelPose (Operator)

## Name

`RefineSurfaceModelPose` — Refine the pose of a surface model in a 3D scene.

## Signature

`static void HOperatorSet.RefineSurfaceModelPose(HTuple surfaceModelID, HTuple objectModel3D, HTuple initialPose, HTuple minScore, HTuple returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple pose, out HTuple score, out HTuple surfaceMatchingResultID)`

`HPose[] HObjectModel3D.RefineSurfaceModelPose(HSurfaceModel surfaceModelID, HPose[] initialPose, HTuple minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score, out HSurfaceMatchingResult[] surfaceMatchingResultID)`

`HPose HObjectModel3D.RefineSurfaceModelPose(HSurfaceModel surfaceModelID, HPose initialPose, double minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score, out HSurfaceMatchingResult surfaceMatchingResultID)`

`HPose[] HSurfaceModel.RefineSurfaceModelPose(HObjectModel3D objectModel3D, HPose[] initialPose, HTuple minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score, out HSurfaceMatchingResult[] surfaceMatchingResultID)`

`HPose HSurfaceModel.RefineSurfaceModelPose(HObjectModel3D objectModel3D, HPose initialPose, double minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score, out HSurfaceMatchingResult surfaceMatchingResultID)`

`static HPose[] HSurfaceMatchingResult.RefineSurfaceModelPose(HSurfaceModel surfaceModelID, HObjectModel3D objectModel3D, HPose[] initialPose, HTuple minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score, out HSurfaceMatchingResult[] surfaceMatchingResultID)`

`HPose HSurfaceMatchingResult.RefineSurfaceModelPose(HSurfaceModel surfaceModelID, HObjectModel3D objectModel3D, HPose initialPose, double minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score)`

## Description

The operator `RefineSurfaceModelPose` refines the approximate
pose *`initialPose`* of the surface model *`surfaceModelID`* in
the 3D scene *`objectModel3D`*.
The surface model *`surfaceModelID`* must have been created previously
with [`CreateSurfaceModel`](create_surface_model.md) or [`ReadSurfaceModel`](read_surface_model.md).
Additionally, [`SetSurfaceModelParam`](set_surface_model_param.md) can be used to
set certain parameters that influence the refinement, such as
restricting the allowed range of rotations.

`RefineSurfaceModelPose` is useful if the pose of an object in
a scene is approximately known and only needs to be refined.
The refined pose is returned in *`pose`*, along with a score in
*`score`*.
It is possible to pass multiple poses for refinement.
Note that, contrary to [`FindSurfaceModel`](find_surface_model.md), the returned poses are
not sorted by their score but are returned in the same order as the input
poses.

The maximum possible error in the approximate pose that can still be
refined depends on the type of object, the amount of clutter in the scene
and the visible parts of the objects.
In general, differences in the orientation of up to 15° and
differences in the position of up to 10% can be refined.

The accuracy of the pose refinement is limited to around
0.1% of the model's size due to numerical reasons. The accuracy
further depends on the noise of the scene points, the number of
scene points and the shape of the model.

Details about the pose refinement and the parameters are described in the
documentation of [`FindSurfaceModel`](find_surface_model.md) in the section about the
dense pose refinement step.
The following generic parameters can be set for
`RefineSurfaceModelPose`, and are also documented in
[`FindSurfaceModel`](find_surface_model.md):
*"pose_ref_num_steps"*,
*"pose_ref_sub_sampling"*,
*"pose_ref_dist_threshold_rel"*,
*"pose_ref_dist_threshold_abs"*,
*"pose_ref_scoring_dist_rel"*,
*"pose_ref_scoring_dist_abs"*,
*"pose_ref_use_scene_normals"*,
*"3d_edge_min_amplitude_rel"*,
*"3d_edge_min_amplitude_abs"*,
*"3d_edges"*,
*"use_3d_edges"*,
*"use_view_based"*,
*"use_self_similar_poses"*,
*"pose_ref_dist_threshold_edges_rel"*,
*"pose_ref_dist_threshold_edges_abs"*,
*"pose_ref_scoring_dist_edges_rel"*, and
*"pose_ref_scoring_dist_edges_abs"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator supports canceling timeouts and interrupts.

## Parameters

**`surfaceModelID`** (input_control)  surface_model `→` [HSurfaceModel](HSurfaceModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the surface model.

**`objectModel3D`** (input_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model containing the
scene.

**`initialPose`** (input_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Initial pose of the surface model in the scene.

**`minScore`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Minimum score of the returned poses.

Default:
0

Restriction:
`MinScore >= 0`

**`returnResultHandle`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Enable returning a result handle in
*`surfaceMatchingResultID`*.

Default:
"false"

List of values:
"false", "true"

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

Default:
[]

List of values:
"3d_edge_min_amplitude_abs", "3d_edge_min_amplitude_rel", "3d_edges", "pose_ref_dist_threshold_abs", "pose_ref_dist_threshold_rel", "pose_ref_num_steps", "pose_ref_scoring_dist_abs", "pose_ref_scoring_dist_rel", "pose_ref_sub_sampling", "pose_ref_use_scene_normals", "use_3d_edges", "use_self_similar_poses", "use_view_based", "viewpoint"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*string* / double / int / long)

Values of the generic parameters.

Default:
[]

Suggested values:
0, 1, "true", "false", 0.005, 0.01, 0.03, 0.05, 0.1

**`pose`** (output_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D pose of the surface model in the scene.

**`score`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Score of the found instances of the model.

**`surfaceMatchingResultID`** (output_control)  surface_matching_result(-array) `→` [HSurfaceMatchingResult](HSurfaceMatchingResult.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the matching result, if enabled in
*`returnResultHandle`*.

## Result

`RefineSurfaceModelPose` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`XyzToObjectModel3d`,
`GetObjectModel3dParams`,
`ReadSurfaceModel`,
`CreateSurfaceModel`,
`GetSurfaceModelParam`,
`FindSurfaceModel`,
`EdgesObjectModel3d`

## Possible Successors

`GetSurfaceMatchingResult`,
`ClearSurfaceMatchingResult`,
`ClearObjectModel3d`

## Alternatives

`FindSurfaceModel`,
`RefineSurfaceModelPoseImage`,
`FindSurfaceModelImage`

## See also

`CreateSurfaceModel`,
`FindSurfaceModel`,
`RefineSurfaceModelPoseImage`

## Module

3D Metrology
