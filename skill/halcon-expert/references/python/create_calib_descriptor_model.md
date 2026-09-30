# create_calib_descriptor_model (Operator)

## Name

`create_calib_descriptor_model` — Create a descriptor model for calibrated perspective matching.

## Signature

`def create_calib_descriptor_model(template: HObject, cam_param: Sequence[Union[float, int, str]], reference_pose: Sequence[Union[float, int]], detector_type: str, detector_param_name: Sequence[str], detector_param_value: Sequence[Union[int, float, str]], descriptor_param_name: Sequence[str], descriptor_param_value: Sequence[Union[int, float, str]], seed: int) -> HHandle`

## Description

The operator `create_calib_descriptor_model` prepares a descriptor
model, which is used for calibrated descriptor-based matching, from a
template image that is passed in *`template`* (usually the domain of the
image is reduced to an ROI showing only the object of interest). Note that
the part of the object that is visible in the *`template`* image needs
to be planar.

The internal camera parameters *`cam_param`* and the
*`reference_pose`*, which describes the 3D position and orientation
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
searched object as described with [`find_calib_descriptor_model`](find_calib_descriptor_model.md).

A descriptor model created by the use of
`create_calib_descriptor_model` can also be used in
[`find_uncalib_descriptor_model`](find_uncalib_descriptor_model.md) to determine a homography. In
contrast, it is not possible to use a model created by
[`create_uncalib_descriptor_model`](create_uncalib_descriptor_model.md) in
[`find_calib_descriptor_model`](find_calib_descriptor_model.md).

The descriptor model describes a set of points of interest. It
stores their locations and discriminative descriptions of their local
gray value neighborhood. The interest point extraction is parametrized
by *`detector_type`*, *`detector_param_name`* and
*`detector_param_value`*. The respective descriptor around the
interest points is parametrized by *`descriptor_param_name`* and
*`descriptor_param_value`*. The parameter *`seed`* seeds the
random number generator, which is used during the construction of the
descriptor implemented with *randomized ferns*. The returned
*`model_id`* is a reference to the generated
descriptor model. For further explanation on the descriptor
model and its parameter we refer to the description of
[`create_uncalib_descriptor_model`](create_uncalib_descriptor_model.md).

The parameters and the location of the final descriptor points can be
determined with [`get_descriptor_model_params`](get_descriptor_model_params.md) and
[`get_descriptor_model_points`](get_descriptor_model_points.md).

`create_calib_descriptor_model` stores the detector type, detector
parameters and descriptor parameters, which are used in every succeeding
call of [`find_calib_descriptor_model`](find_calib_descriptor_model.md) or
[`find_uncalib_descriptor_model`](find_uncalib_descriptor_model.md). The reference point (origin) of
the model is the center of gravity of the template's ROI. Its coordinates
can be changed by [`set_descriptor_model_origin`](set_descriptor_model_origin.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`template`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Input image whose domain will be used to create
the model.

**`cam_param`** (input_control)  campar `→` Sequence[Union[float, int, str]]

The parameters of the internal orientation of
the camera.

**`reference_pose`** (input_control)  pose `→` Sequence[Union[float, int]]

The reference pose of the object in the reference
image.

**`detector_type`** (input_control)  string `→` str

The type of the detector.

Default:
"lepetit"

List of values:
"harris", "harris_binomial", "lepetit"

**`detector_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

The detector's parameter names.

Default:
[]

List of values:
"alpha", "check_neighbor", "mask_size_grd", "mask_size_smooth", "min_check_neighbor_diff", "min_score", "radius", "sigma_grad", "sigma_smooth", "subpix", "threshold"

**`detector_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[int, float, str]]

Values of the detector's parameters.

Default:
[]

Suggested values:
0.08, 1, 1.2, 3, 15, 30, 1000, "on", "off"

**`descriptor_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

The descriptor's parameter names.

Default:
[]

List of values:
"depth", "max_rot", "max_scale", "min_rot", "min_scale", "number_ferns", "patch_size", "tilt"

**`descriptor_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[int, float, str]]

Values of the descriptor's parameters.

Default:
[]

Suggested values:
0.5, 1.4, 11, 21, 30, -180, 180, "on", "off"

**`seed`** (input_control)  integer `→` int

The seed for the random number generator.

Default:
42

**`model_id`** (output_control)  descriptor_model `→` HHandle

The handle to the descriptor model.

## Possible Predecessors

`points_lepetit`,
`points_harris`,
`reduce_domain`

## Possible Successors

`get_descriptor_model_params`,
`find_calib_descriptor_model`

## See also

`get_descriptor_model_params`,
`find_calib_descriptor_model`

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
