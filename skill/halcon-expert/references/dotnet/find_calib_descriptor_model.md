# FindCalibDescriptorModel (Operator)

## Name

`FindCalibDescriptorModel` — Find the best matches of a calibrated descriptor model in an image and
return their 3D pose.

## Signature

`static void HOperatorSet.FindCalibDescriptorModel(HObject image, HTuple modelID, HTuple detectorParamName, HTuple detectorParamValue, HTuple descriptorParamName, HTuple descriptorParamValue, HTuple minScore, HTuple numMatches, HTuple camParam, HTuple scoreType, out HTuple pose, out HTuple score)`

`HPose[] HDescriptorModel.FindCalibDescriptorModel(HImage image, HTuple detectorParamName, HTuple detectorParamValue, HTuple descriptorParamName, HTuple descriptorParamValue, HTuple minScore, int numMatches, HCamPar camParam, HTuple scoreType, out HTuple score)`

`HPose HDescriptorModel.FindCalibDescriptorModel(HImage image, HTuple detectorParamName, HTuple detectorParamValue, HTuple descriptorParamName, HTuple descriptorParamValue, double minScore, int numMatches, HCamPar camParam, string scoreType, out double score)`

`HPose[] HImage.FindCalibDescriptorModel(HDescriptorModel modelID, HTuple detectorParamName, HTuple detectorParamValue, HTuple descriptorParamName, HTuple descriptorParamValue, HTuple minScore, int numMatches, HCamPar camParam, HTuple scoreType, out HTuple score)`

`HPose HImage.FindCalibDescriptorModel(HDescriptorModel modelID, HTuple detectorParamName, HTuple detectorParamValue, HTuple descriptorParamName, HTuple descriptorParamValue, double minScore, int numMatches, HCamPar camParam, string scoreType, out double score)`

`HPose[] HCamPar.FindCalibDescriptorModel(HImage image, HDescriptorModel modelID, HTuple detectorParamName, HTuple detectorParamValue, HTuple descriptorParamName, HTuple descriptorParamValue, HTuple minScore, int numMatches, HTuple scoreType, out HTuple score)`

`HPose HCamPar.FindCalibDescriptorModel(HImage image, HDescriptorModel modelID, HTuple detectorParamName, HTuple detectorParamValue, HTuple descriptorParamName, HTuple descriptorParamValue, double minScore, int numMatches, string scoreType, out double score)`

`static HTuple HPose.FindCalibDescriptorModel(HImage image, HDescriptorModel modelID, HTuple detectorParamName, HTuple detectorParamValue, HTuple descriptorParamName, HTuple descriptorParamValue, HTuple minScore, int numMatches, HCamPar camParam, HTuple scoreType, out HPose[] pose)`

`double HPose.FindCalibDescriptorModel(HImage image, HDescriptorModel modelID, HTuple detectorParamName, HTuple detectorParamValue, HTuple descriptorParamName, HTuple descriptorParamValue, double minScore, int numMatches, HCamPar camParam, string scoreType)`

## Description

The operator `FindCalibDescriptorModel` finds the best
*`numMatches`* matches of the descriptor model *`modelID`*
in *`image`*. The descriptor model must have been created
previously by calling [`CreateCalibDescriptorModel`](create_calib_descriptor_model.md) or
[`ReadDescriptorModel`](read_descriptor_model.md).

The operator returns the 3D *`pose`* (in camera coordinate system)
of the template object found in the search *`image`*. As two
different cameras can be used for the model generation and the online
search, the camera parameters of the camera used to create *`image`*
have to be set in *`camParam`*. Therefore, there is no need to
correct any distortions in *`image`* manually.

The detection process is the same as for
[`FindUncalibDescriptorModel`](find_uncalib_descriptor_model.md). The setting of
*`detectorParamName`*, *`detectorParamValue`*,
*`descriptorParamName`*, *`descriptorParamValue`*,
*`minScore`*, *`numMatches`* and *`scoreType`* are
explained with [`FindUncalibDescriptorModel`](find_uncalib_descriptor_model.md). After the object
was detected, and using the world (from reference plane) coordinates of
the matched model points (explained with
[`CreateCalibDescriptorModel`](create_calib_descriptor_model.md)), the pose of the object is
computed similarly to applying [`VectorToPose`](vector_to_pose.md) operator.

The point correspondences for each object can be queried with
[`GetDescriptorModelPoints`](get_descriptor_model_points.md).

## Attention

Note that the domain of the search image should contain the whole
object to be searched for because interest points are only extracted
inside the domain of the search image. This means that if the domain
does not contain the full object to be searched for, the resulting
*`score`* will decrease. Note also that matches may be found even
if the reference point (origin) of the model lies outside of the
domain of the search image. Both is in contrast to shape-based
matching, where the domain of the search image defines the search
space for the reference point of the model.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input image where the model should be found.

**`modelID`** (input_control)  descriptor_model `→` [HDescriptorModel](HDescriptorModel.md), [HTuple](HTuple.md) (*IntPtr*)

The handle to the descriptor model.

**`detectorParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

The detector's parameter names.

Default:
[]

List of values:
"alpha", "check_neighbor", "mask_size_grd", "mask_size_smooth", "min_check_neighbor_diff", "min_score", "radius", "sigma_grad", "sigma_smooth", "subpix", "threshold"

**`detectorParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Values of the detector's parameters.

Default:
[]

Suggested values:
0.08, 1, 1.2, 3, 15, 30, 1000, "on", "off"

**`descriptorParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

The descriptor's parameter names.

Default:
[]

List of values:
"guided_matching", "min_score_descr"

**`descriptorParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of the descriptor's parameters.

Default:
[]

Suggested values:
0.0, 0.001, 0.005, 0.01, "on", "off"

**`minScore`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum score of the instances of the models to
be found.

Default:
0.2

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Value range:
`0
≤
minScore
≤
1`

**`numMatches`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximal number of found instances.

Default:
1

Suggested values:
1, 2, 3, 4

Restriction:
`NumMatches >= 1`

**`camParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Camera parameter (inner orientation) obtained from
camera calibration.

**`scoreType`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Score type to be evaluated in *`score`*.

Default:
"num_points"

List of values:
"inlier_ratio", "num_points"

**`pose`** (output_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D pose of the object.

**`score`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

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

`CreateCalibDescriptorModel`,
`ReadDescriptorModel`

## See also

`VectorToPose`,
`PointsLepetit`,
`CreateCalibDescriptorModel`

## Module

Matching
