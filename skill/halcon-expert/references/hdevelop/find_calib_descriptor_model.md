# find_calib_descriptor_model (Operator)

## Name

`find_calib_descriptor_model` — Find the best matches of a calibrated descriptor model in an image and
return their 3D pose.

## Signature

`find_calib_descriptor_model(Image : : ModelID, DetectorParamName, DetectorParamValue, DescriptorParamName, DescriptorParamValue, MinScore, NumMatches, CamParam, ScoreType : Pose, Score)`

## Description

The operator `find_calib_descriptor_model` finds the best
*`NumMatches`* matches of the descriptor model *`ModelID`*
in *`Image`*. The descriptor model must have been created
previously by calling [`create_calib_descriptor_model`](create_calib_descriptor_model.md) or
[`read_descriptor_model`](read_descriptor_model.md).

The operator returns the 3D *`Pose`* (in camera coordinate system)
of the template object found in the search *`Image`*. As two
different cameras can be used for the model generation and the online
search, the camera parameters of the camera used to create *`Image`*
have to be set in *`CamParam`*. Therefore, there is no need to
correct any distortions in *`Image`* manually.

The detection process is the same as for
[`find_uncalib_descriptor_model`](find_uncalib_descriptor_model.md). The setting of
*`DetectorParamName`*, *`DetectorParamValue`*,
*`DescriptorParamName`*, *`DescriptorParamValue`*,
*`MinScore`*, *`NumMatches`* and *`ScoreType`* are
explained with [`find_uncalib_descriptor_model`](find_uncalib_descriptor_model.md). After the object
was detected, and using the world (from reference plane) coordinates of
the matched model points (explained with
[`create_calib_descriptor_model`](create_calib_descriptor_model.md)), the pose of the object is
computed similarly to applying [`vector_to_pose`](vector_to_pose.md) operator.

The point correspondences for each object can be queried with
[`get_descriptor_model_points`](get_descriptor_model_points.md).

## Attention

Note that the domain of the search image should contain the whole
object to be searched for because interest points are only extracted
inside the domain of the search image. This means that if the domain
does not contain the full object to be searched for, the resulting
*`Score`* will decrease. Note also that matches may be found even
if the reference point (origin) of the model lies outside of the
domain of the search image. Both is in contrast to shape-based
matching, where the domain of the search image defines the search
space for the reference point of the model.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image where the model should be found.

**`ModelID`** (input_control)  descriptor_model `→`  (handle)

The handle to the descriptor model.

**`DetectorParamName`** (input_control)  attribute.name-array `→`  (string)

The detector's parameter names.

Default:
[]

List of values:
'alpha', 'check_neighbor', 'mask_size_grd', 'mask_size_smooth', 'min_check_neighbor_diff', 'min_score', 'radius', 'sigma_grad', 'sigma_smooth', 'subpix', 'threshold'

**`DetectorParamValue`** (input_control)  attribute.value-array `→`  (integer / real / string)

Values of the detector's parameters.

Default:
[]

Suggested values:
0.08, 1, 1.2, 3, 15, 30, 1000, 'on', 'off'

**`DescriptorParamName`** (input_control)  attribute.name-array `→`  (string)

The descriptor's parameter names.

Default:
[]

List of values:
'guided_matching', 'min_score_descr'

**`DescriptorParamValue`** (input_control)  attribute.value-array `→`  (real / integer / string)

Values of the descriptor's parameters.

Default:
[]

Suggested values:
0.0, 0.001, 0.005, 0.01, 'on', 'off'

**`MinScore`** (input_control)  real(-array) `→`  (real)

Minimum score of the instances of the models to
be found.

Default:
0.2

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Value range:
`0
≤
MinScore
≤
1`

**`NumMatches`** (input_control)  integer `→`  (integer)

Maximal number of found instances.

Default:
1

Suggested values:
1, 2, 3, 4

Restriction:
`NumMatches >= 1`

**`CamParam`** (input_control)  campar `→`  (real / integer / string)

Camera parameter (inner orientation) obtained from
camera calibration.

**`ScoreType`** (input_control)  string(-array) `→`  (string)

Score type to be evaluated in *`Score`*.

Default:
'num_points'

List of values:
'inlier_ratio', 'num_points'

**`Pose`** (output_control)  pose(-array) `→`  (real / integer)

3D pose of the object.

**`Score`** (output_control)  number(-array) `→`  (real / integer)

Score of the found instances according to the
ScoreType input.

## Example (HDevelop)

```
*  Perform camera calibration (with standard calibration plate)
calibrate_cameras (CalibDataID, Error)
get_calib_data (CalibDataID, 'camera', 0, 'params', CamParam)
*  World coordinate system is defined by calibration plate in first image
get_calib_data (CalibDataID, 'calib_obj_pose',  [0,0], 'pose', \
                ObjInCameraPose)
*  Compensate thickness of plate
set_origin_pose(ObjInCameraPose, 0, 0, 0.0006, WorldPose)

* Create descriptor model:
create_calib_descriptor_model (Image,CamParam,WorldPose, \
                               'harris',[],[],[],[],42,ModelID)

get_descriptor_model_params (ModelID,DetectorType, \
                             DetectorParamName,DetectorParamValue, \
                             DescriptorParamName,DescriptorParamValue)
write_descriptor_model (ModelID,'simple_example.dsm')

read_descriptor_model ('simple_example.dsm',ModelID)
find_calib_descriptor_model (SearchImage,ModelID,[],[],[],[],0.2,1, \
                             CamParam,['num_points','inlier_ratio'], \
                             Pose,Score)
```

## Possible Predecessors

`create_calib_descriptor_model`,
`read_descriptor_model`

## See also

`vector_to_pose`,
`points_lepetit`,
`create_calib_descriptor_model`

## Module

Matching
