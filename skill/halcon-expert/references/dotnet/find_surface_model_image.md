# FindSurfaceModelImage (Operator)

## Name

`FindSurfaceModelImage` — Find the best matches of a surface model in a 3D scene and images.

## Signature

`static void HOperatorSet.FindSurfaceModelImage(HObject image, HTuple surfaceModelID, HTuple objectModel3D, HTuple relSamplingDistance, HTuple keyPointFraction, HTuple minScore, HTuple returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple pose, out HTuple score, out HTuple surfaceMatchingResultID)`

`HPose[] HObjectModel3D.FindSurfaceModelImage(HImage image, HSurfaceModel surfaceModelID, double relSamplingDistance, double keyPointFraction, HTuple minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score, out HSurfaceMatchingResult[] surfaceMatchingResultID)`

`HPose HObjectModel3D.FindSurfaceModelImage(HImage image, HSurfaceModel surfaceModelID, double relSamplingDistance, double keyPointFraction, double minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score, out HSurfaceMatchingResult surfaceMatchingResultID)`

`HPose[] HSurfaceModel.FindSurfaceModelImage(HImage image, HObjectModel3D objectModel3D, double relSamplingDistance, double keyPointFraction, HTuple minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score, out HSurfaceMatchingResult[] surfaceMatchingResultID)`

`HPose HSurfaceModel.FindSurfaceModelImage(HImage image, HObjectModel3D objectModel3D, double relSamplingDistance, double keyPointFraction, double minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score, out HSurfaceMatchingResult surfaceMatchingResultID)`

`static HPose[] HSurfaceMatchingResult.FindSurfaceModelImage(HImage image, HSurfaceModel surfaceModelID, HObjectModel3D objectModel3D, double relSamplingDistance, double keyPointFraction, HTuple minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score, out HSurfaceMatchingResult[] surfaceMatchingResultID)`

`HPose HSurfaceMatchingResult.FindSurfaceModelImage(HImage image, HSurfaceModel surfaceModelID, HObjectModel3D objectModel3D, double relSamplingDistance, double keyPointFraction, double minScore, string returnResultHandle, HTuple genParamName, HTuple genParamValue, out HTuple score)`

## Description

The operator `FindSurfaceModelImage` finds the best matches of
the surface model *`surfaceModelID`* in the scene that is comprised
of the 3D surface in *`objectModel3D`* and the images of the scene in
*`image`*.
Note that the number of images passed in *`image`* must correspond
to the number of cameras set with [`SetSurfaceModelParam`](set_surface_model_param.md).
Note also that the surface model must have been created by
[`CreateSurfaceModel`](create_surface_model.md) with the parameter *"train_3d_edges"*
enabled.

The images are used only in the sparse and dense refinement step.
For this, the refinement simultaneously optimizes the alignment of the
model with the 3D scene as well as the alignment of the reprojected edges
of the model silhouette with edges in the passed images. The domain of
the images is ignored.

In addition to the parameters documented in
[`FindSurfaceModel`](find_surface_model.md), `FindSurfaceModelImage` also supports
the following generic parameters:

- ***"min_contrast"*:** —

  Sets the minimum contrast of the object in the search images. Edges
  with a contrast below this threshold are ignored in the refinement.

  Suggested values:
   *5*, *10*, *20*

  Default:
   *10*

  Restriction:
   *"min_contrast"* >= *0*
- ***"max_deformation"*:** —

  Sets the search range in pixels for corresponding edges in the image.
  This parameter can be used if the shape of the object is slightly deformed
  compared to the original 3D model used in [`CreateSurfaceModel`](create_surface_model.md).
  Note that increasing this parameter can have a significant impact on the
  runtime of the refinement.

  Suggested values:
   *0*, *1*, *5*

  Default:
   *1*

  Restriction:
   *"max_deformation"* >= *0*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

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

**`relSamplingDistance`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Scene sampling distance relative to the diameter
of the surface model.

Default:
0.05

Suggested values:
0.1, 0.07, 0.05, 0.04, 0.03

Restriction:
`0 < RelSamplingDistance < 1`

**`keyPointFraction`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Fraction of sampled scene points used as
key points.

Default:
0.2

Suggested values:
0.3, 0.2, 0.1, 0.05

Restriction:
`0 < KeyPointFraction <= 1`

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

Suggested values:
"true", "false"

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

Default:
[]

List of values:
"3d_edge_min_amplitude_abs", "3d_edge_min_amplitude_rel", "3d_edges", "dense_pose_refinement", "max_deformation", "max_gap", "max_overlap_dist_abs", "max_overlap_dist_rel", "min_contrast", "num_matches", "pose_ref_dist_threshold_abs", "pose_ref_dist_threshold_rel", "pose_ref_num_steps", "pose_ref_scoring_dist_abs", "pose_ref_scoring_dist_rel", "pose_ref_sub_sampling", "pose_ref_use_scene_normals", "scene_invert_normals", "scene_normal_computation", "sparse_pose_refinement", "use_3d_edges", "use_self_similar_poses", "use_view_based", "viewpoint"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*string* / double / int / long)

Values of the generic parameters.

Default:
[]

Suggested values:
0, 1, "true", "false", 0.005, 0.01, 0.03, 0.05, 0.1, "num_scene_points", "model_point_fraction", "num_model_points", "fast", "mls"

**`pose`** (output_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D pose of the surface model in the scene.

**`score`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Score of the found instances of the surface
model.

**`surfaceMatchingResultID`** (output_control)  surface_matching_result(-array) `→` [HSurfaceMatchingResult](HSurfaceMatchingResult.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the matching result, if enabled in
*`returnResultHandle`*.

## Result

`FindSurfaceModelImage` returns 2 (
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
`EdgesObjectModel3d`

## Possible Successors

`RefineSurfaceModelPose`,
`GetSurfaceMatchingResult`,
`ClearSurfaceMatchingResult`,
`ClearObjectModel3d`

## Alternatives

`RefineSurfaceModelPose`,
`FindSurfaceModel`,
`RefineSurfaceModelPoseImage`

## See also

`RefineSurfaceModelPose`,
`FindSurfaceModel`

## Module

3D Metrology
