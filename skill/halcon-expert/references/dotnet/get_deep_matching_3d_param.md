# GetDeepMatching3dParam (Operator)

## Name

`GetDeepMatching3dParam` — Read a parameter from a Deep 3D Matching model.

## Signature

`static void HOperatorSet.GetDeepMatching3dParam(HTuple deep3DMatchingModel, HTuple genParamName, out HTuple genParamValue)`

`HTuple HDeepMatching3D.GetDeepMatching3dParam(HTuple genParamName)`

`HTuple HDeepMatching3D.GetDeepMatching3dParam(string genParamName)`

## Description

The operator `GetDeepMatching3dParam` returns the parameter values
of *`genParamName`* for the Deep 3D Matching model *`deep3DMatchingModel`*
in *`genParamValue`*.

The following table gives an overview, which parameters can be set
using [`SetDeepMatching3dParam`](set_deep_matching_3d_param.md) and which can be
retrieved using `GetDeepMatching3dParam`.

| *`genParamName`* | `set` | `get` |
| --- | --- | --- |
| *"camera_parameter N"* | `x` | `x` |
| *"camera_pose N"* | `x` | `x` |
| *"delete_cameras"* | `x` |  |
| *"dl_model_detection"* | `x` | `x` |
| *"dl_model_pose_estimation"* | `x` | `x` |
| *"min_num_views"* | `x` | `x` |
| *"sort_single_views_last"* | `x` | `x` |
| *"min_score"* | `x` | `x` |
| *"num_matches"* | `x` | `x` |
| *"orig_3d_model"* |  | `x` |
| *"symmetry_type"* |  | `x` |
| *"symmetry_poses"* |  | `x` |

In the following the parameters are described:

- ***"camera_parameter N"*, *"camera_pose N"*, *"delete_cameras"*:** —

  These parameters control the camera setup used for matching, i.e., the
  camera poses and the camera parameters.
  *"delete_cameras"* can be set with an empty tuple as
  value to delete all cameras from a Deep 3D Matching model.

  The keys for accessing the parameters of the N'th camera are
  *"camera_parameter N"* and *"camera_pose N"*, where N is
  the zero-based index of the camera.
  For example, to access the parameters of the first camera, use
  *"camera_parameter 0"* and *"camera_pose 0"*.
  Note that cameras must be added in order.

  Further note that the camera parameters should not contain too much of a distortion.
  Small distortions can be handled by the model. If the camera distortion is high,
  it is recommended to remove any distortion from the camera parameters and images
  beforehand, using, for example, [`ChangeRadialDistortionCamPar`](change_radial_distortion_cam_par.md)
  in combination with [`ChangeRadialDistortionImage`](change_radial_distortion_image.md) or
  [`GenRadialDistortionMap`](gen_radial_distortion_map.md) and [`MapImage`](map_image.md).

  The camera pose is the pose of the camera in an arbitrary world coordinate
  system. The poses of detected objects are returned in that world coordinate
  system.
  The angles must be passed in degrees and the translations need to be in the
  same unit as the 3D CAD model of the Deep 3D Matching model.
- ***"dl_model_detection"*, *"dl_model_pose_estimation"*:** —

  The deep learning models used for Deep 3D Matching.
  They can be obtained and written back in order to train them using
  [`TrainDlModelBatch`](train_dl_model_batch.md),
  optimize them using [`OptimizeDlModelForInference`](optimize_dl_model_for_inference.md) or change the device
  on which they are executed.

  Note that for setting a 3D pose estimation model, the model has to contain 3D
  information which was attached to a backbone in
  [`CreateDeepMatching3d`](create_deep_matching_3d.md).
- ***"min_num_views"*:** —

  This parameter determines the minimum number of cameras in which an instance
  must be visible in order to be returned by [`ApplyDeepMatching3d`](apply_deep_matching_3d.md).
  The parameter can be either an integer larger than zero, or the
  string *"auto"*.
  If *"auto"*, instances must be visible in a single camera if only a
  single camera is used, and in at least two cameras otherwise.

  Suggested values:
   *"auto"*, *2*,
  *3*

  Value range:
   $\ge$ *0*

  Default:
   *"auto"*
- ***"sort_single_views_last"*:** —

  If this parameter is set to *"true"* (default value) and
  *"min_num_views"* is set to *1*,
  instances that were only seen from a single camera
  will be sorted to the back of the result list, even if they
  have a higher score than instances that were seen from more than one
  camera.
  Internally, this causes instances seen from more cameras
  to be preferred during deduplication.
  This mode is mainly intended so that applications
  receive both "more certain" matches (seen from more than one camera)
  and üncertain" results (seen from only one camera),
  without the uncertain results influencing the more certain ones.
  The uncertain results can, for example, be incorporated into the path
  planning of a robot.

  Suggested values:
   *"true"*, *"false"*

  Default:
   *"true"*
- ***"min_score"*:** —

  This parameter determines the minimum score of detected instances.
  In other words, [`ApplyDeepMatching3d`](apply_deep_matching_3d.md) ignores all detected
  instances with a score smaller than this value.
  The score computed by the Deep 3D Matching model lies between
  *0* and *1*, where *0* indicates a bad match and
  *1* is a very good match.

  Value range:
   [*0*, .., *1*]

  Default:
   *0.2*
- ***"num_matches"*:** —

  This parameter determines the maximum number of matches to return by
  [`ApplyDeepMatching3d`](apply_deep_matching_3d.md).
  If the operator finds more instances than set in *"num_matches"*,
  only the *"num_matches"* instances with the highest scores
  are returned.
  This parameter can be set to zero, in which case all instances
  above *"min_score"* are returned.

  Value range:
   $\ge$ *0*

  Default:
   *0*
- ***"orig_3d_model"*:** —

  This parameter returns the original 3D CAD model used for creating
  the Deep 3D Matching model, see [`CreateDeepMatching3d`](create_deep_matching_3d.md).
  It can be used to visualize detection results.
- ***"symmetry_type"*:** —

  This parameter returns the symmetry type of the original 3D CAD
  model used for creating the Deep 3D Matching model, see
  [`CreateDeepMatching3d`](create_deep_matching_3d.md).
- ***"symmetry_poses"*:** —

  For Deep 3D Matching models of *"symmetry_type"* *"discrete"*,
  this parameter returns the symmetry poses of the original 3D CAD
  model used for creating the Deep 3D Matching model, see
  [`CreateDeepMatching3d`](create_deep_matching_3d.md).

## Attention

Deep 3D Matching requires images to not have too much of a distortion.
Small distortions can be handled by the model. If the camera distortion is high,
it is recommended to remove any distortion from the camera parameters and images
beforehand, using, for example, [`ChangeRadialDistortionCamPar`](change_radial_distortion_cam_par.md)
in combination with [`ChangeRadialDistortionImage`](change_radial_distortion_image.md) or
[`GenRadialDistortionMap`](gen_radial_distortion_map.md) and [`MapImage`](map_image.md).

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
"min_score", "num_matches", "orig_3d_model", "min_num_views", "dl_model_detection", "dl_model_pose_estimation", "camera_parameter", "camera_pose", "symmetry_type", "symmetry_poses", "sort_single_views_last"

**`genParamValue`** (output_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long / HHandle)

Obtained value of parameter.

## Module

3D Metrology
