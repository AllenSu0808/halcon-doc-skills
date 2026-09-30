# RefineSurfaceModelPoseImage (Operator)

## Name

`RefineSurfaceModelPoseImage` — Refine the pose of a surface model in a 3D scene and in images.

## Signature

`static void HOperatorSet.RefineSurfaceModelPoseImage(HObject image, HTuple surfaceModelID, HTuple objectModel3D, HTuple initialPose, HTuple minScore, HTuple returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple pose, out HTuple score, out HTuple surfaceMatchingResultID)`

`HPose[] HObjectModel3D.RefineSurfaceModelPoseImage(HImage image, HSurfaceModel surfaceModelID, HPose[] initialPose, HTuple minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score, out HSurfaceMatchingResult[] surfaceMatchingResultID)`

`HPose HObjectModel3D.RefineSurfaceModelPoseImage(HImage image, HSurfaceModel surfaceModelID, HPose initialPose, double minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score, out HSurfaceMatchingResult surfaceMatchingResultID)`

`HPose[] HSurfaceModel.RefineSurfaceModelPoseImage(HImage image, HObjectModel3D objectModel3D, HPose[] initialPose, HTuple minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score, out HSurfaceMatchingResult[] surfaceMatchingResultID)`

`HPose HSurfaceModel.RefineSurfaceModelPoseImage(HImage image, HObjectModel3D objectModel3D, HPose initialPose, double minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score, out HSurfaceMatchingResult surfaceMatchingResultID)`

`static HPose[] HSurfaceMatchingResult.RefineSurfaceModelPoseImage(HImage image, HSurfaceModel surfaceModelID, HObjectModel3D objectModel3D, HPose[] initialPose, HTuple minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score, out HSurfaceMatchingResult[] surfaceMatchingResultID)`

`HPose HSurfaceMatchingResult.RefineSurfaceModelPoseImage(HImage image, HSurfaceModel surfaceModelID, HObjectModel3D objectModel3D, HPose initialPose, double minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score)`

## Description

The operator `RefineSurfaceModelPoseImage` refines the approximate
pose *`initialPose`* of the surface model *`surfaceModelID`* in
the 3D scene comprised of the 3D surface in *`objectModel3D`* and the
images of the scene in *`image`*.
Note that the number of images passed in *`image`* must correspond
to the number of cameras set with [`SetSurfaceModelParam`](set_surface_model_param.md).
Note also that the surface model must have been created by
[`CreateSurfaceModel`](create_surface_model.md) with the parameter *"train_3d_edges"*
enabled.

The refinement simultaneously optimizes the alignment of the
model with the 3D scene as well as the alignment of the reprojected edges
with edges in the passed images. The domain of the images is ignored.

In addition to the parameters documented in
[`RefineSurfaceModelPose`](refine_surface_model_pose.md), `RefineSurfaceModelPoseImage`
also supports the generic parameters *"min_contrast"* and
*"max_deformation"*, documented in [`FindSurfaceModelImage`](find_surface_model_image.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator supports canceling timeouts and interrupts.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2)

Images of the scene.

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
"3d_edge_min_amplitude_abs", "3d_edge_min_amplitude_rel", "3d_edges", "max_deformation", "min_contrast", "pose_ref_dist_threshold_abs", "pose_ref_dist_threshold_rel", "pose_ref_num_steps", "pose_ref_scoring_dist_abs", "pose_ref_scoring_dist_rel", "pose_ref_sub_sampling", "pose_ref_use_scene_normals", "use_3d_edges", "use_self_similar_poses", "use_view_based", "viewpoint"

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

`RefineSurfaceModelPoseImage` returns 2 (
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
`RefineSurfaceModelPose`,
`FindSurfaceModelImage`

## See also

`CreateSurfaceModel`,
`FindSurfaceModel`,
`RefineSurfaceModelPose`

## Module

3D Metrology
