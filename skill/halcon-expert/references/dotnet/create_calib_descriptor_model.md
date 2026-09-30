# CreateCalibDescriptorModel (Operator)

## Name

`CreateCalibDescriptorModel` — Create a descriptor model for calibrated perspective matching.

## Signature

`static void HOperatorSet.CreateCalibDescriptorModel(HObject template, HTuple camParam, HTuple referencePose, HTuple detectorType, HTuple detectorParamName, HTuple detectorParamValue, HTuple descriptorParamName, HTuple descriptorParamValue, HTuple seed, out HTuple modelID)`

`public HDescriptorModel(HImage template, HCamPar camParam, HPose referencePose, string detectorType, HTuple detectorParamName, HTuple detectorParamValue, HTuple descriptorParamName, HTuple descriptorParamValue, int seed)`

`void HDescriptorModel.CreateCalibDescriptorModel(HImage template, HCamPar camParam, HPose referencePose, string detectorType, HTuple detectorParamName, HTuple detectorParamValue, HTuple descriptorParamName, HTuple descriptorParamValue, int seed)`

`HDescriptorModel HImage.CreateCalibDescriptorModel(HCamPar camParam, HPose referencePose, string detectorType, HTuple detectorParamName, HTuple detectorParamValue, HTuple descriptorParamName, HTuple descriptorParamValue, int seed)`

`HDescriptorModel HCamPar.CreateCalibDescriptorModel(HImage template, HPose referencePose, string detectorType, HTuple detectorParamName, HTuple detectorParamValue, HTuple descriptorParamName, HTuple descriptorParamValue, int seed)`

`HDescriptorModel HPose.CreateCalibDescriptorModel(HImage template, HCamPar camParam, string detectorType, HTuple detectorParamName, HTuple detectorParamValue, HTuple descriptorParamName, HTuple descriptorParamValue, int seed)`

## Description

The operator `CreateCalibDescriptorModel` prepares a descriptor
model, which is used for calibrated descriptor-based matching, from a
template image that is passed in *`template`* (usually the domain of the
image is reduced to an ROI showing only the object of interest). Note that
the part of the object that is visible in the *`template`* image needs
to be planar.

The internal camera parameters *`camParam`* and the
*`referencePose`*, which describes the 3D position and orientation
of the object plane shown in *`template`*, are used to internally
calculate a model coordinate system. The origin of this model coordinate
system is obtained by projecting the center of gravity of an internally
rectified version of the template image onto the object plane. The axes
of the model coordinate system are built such that they are parallel to
the axes of Reference Pose. To obtain a descriptor model from the template
image, the points extracted by the detector in the internally rectified
template image are projected onto the object plane as well. Their
coordinates in the model coordinate system are stored as world coordinates
in the model. This model then can be used for the pose estimation of a
searched object as described with [`FindCalibDescriptorModel`](find_calib_descriptor_model.md).

A descriptor model created by the use of
`CreateCalibDescriptorModel` can also be used in
[`FindUncalibDescriptorModel`](find_uncalib_descriptor_model.md) to determine a homography. In
contrast, it is not possible to use a model created by
[`CreateUncalibDescriptorModel`](create_uncalib_descriptor_model.md) in
[`FindCalibDescriptorModel`](find_calib_descriptor_model.md).

The descriptor model describes a set of points of interest. It
stores their locations and discriminative descriptions of their local
gray value neighborhood. The interest point extraction is parametrized
by *`detectorType`*, *`detectorParamName`* and
*`detectorParamValue`*. The respective descriptor around the
interest points is parametrized by *`descriptorParamName`* and
*`descriptorParamValue`*. The parameter *`seed`* seeds the
random number generator, which is used during the construction of the
descriptor implemented with *randomized ferns*. The returned
*`modelID`* is a reference to the generated
descriptor model. For further explanation on the descriptor
model and its parameter we refer to the description of
[`CreateUncalibDescriptorModel`](create_uncalib_descriptor_model.md).

The parameters and the location of the final descriptor points can be
determined with [`GetDescriptorModelParams`](get_descriptor_model_params.md) and
[`GetDescriptorModelPoints`](get_descriptor_model_points.md).

`CreateCalibDescriptorModel` stores the detector type, detector
parameters and descriptor parameters, which are used in every succeeding
call of [`FindCalibDescriptorModel`](find_calib_descriptor_model.md) or
[`FindUncalibDescriptorModel`](find_uncalib_descriptor_model.md). The reference point (origin) of
the model is the center of gravity of the template's ROI. Its coordinates
can be changed by [`SetDescriptorModelOrigin`](set_descriptor_model_origin.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`template`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input image whose domain will be used to create
the model.

**`camParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

The parameters of the internal orientation of
the camera.

**`referencePose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

The reference pose of the object in the reference
image.

**`detectorType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

The type of the detector.

Default:
"lepetit"

List of values:
"harris", "harris_binomial", "lepetit"

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
"depth", "max_rot", "max_scale", "min_rot", "min_scale", "number_ferns", "patch_size", "tilt"

**`descriptorParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Values of the descriptor's parameters.

Default:
[]

Suggested values:
0.5, 1.4, 11, 21, 30, -180, 180, "on", "off"

**`seed`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

The seed for the random number generator.

Default:
42

**`modelID`** (output_control)  descriptor_model `→` [HDescriptorModel](HDescriptorModel.md), [HTuple](HTuple.md) (*IntPtr*)

The handle to the descriptor model.

## Possible Predecessors

`PointsLepetit`,
`PointsHarris`,
`ReduceDomain`

## Possible Successors

`GetDescriptorModelParams`,
`FindCalibDescriptorModel`

## See also

`GetDescriptorModelParams`,
`FindCalibDescriptorModel`

## References

V. Lepetit and P. Fua: “Keypoint Recognition using Randomized Trees.“
IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol. 28,
Nr. 9, pp. 1465-1479, 2006.
  
M. Ozuysal, P. Fua, and V. Lepetit: “Fast Keypoint Recognition in Ten Lines
of Code.“
In Proceedings of Conference on Computer Vision and Pattern Recognition,
2007.

## Module

Matching
