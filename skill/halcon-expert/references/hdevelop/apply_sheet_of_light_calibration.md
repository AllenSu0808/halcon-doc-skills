# apply_sheet_of_light_calibration (Operator)

## Name

`apply_sheet_of_light_calibration` — Apply the calibration transformations to the input disparity image.

## Signature

`apply_sheet_of_light_calibration(Disparity : : SheetOfLightModelID : )`

## Description

The operator `apply_sheet_of_light_calibration` reads the disparity
image *`Disparity`*, stores it to the sheet-of-light model specified
by *`SheetOfLightModelID`* and applies the calibration transformation
to this image, in order to compute the calibrated coordinates of the
reconstructed 3D surface points. The resulting calibrated coordinates can
be retrieved from the model by using the operator
[`get_sheet_of_light_result`](get_sheet_of_light_result.md). The corresponding 3D object model
can be retrieved with [`get_sheet_of_light_result_object_model_3d`](get_sheet_of_light_result_object_model_3d.md).
Note that prior to the next call of `apply_sheet_of_light_calibration`
for a disparity image of smaller height, [`reset_sheet_of_light_model`](reset_sheet_of_light_model.md)
should be called.

The disparity image *`Disparity`* may have been acquired previously
by using the operator [`measure_profile_sheet_of_light`](measure_profile_sheet_of_light.md) or by an
image acquisition device, which directly provides disparity values and
works according to the sheet-of-light technique.

In order to compute the calibrated coordinates, the parameters listed
below must have been set for the sheet-of-light model with the help of
the operator [`set_sheet_of_light_param`](set_sheet_of_light_param.md):

- ***'calibration'*:** —

  extent of the calibration transformation which shall be applied
  to the disparity image. *'calibration'* must be set to
  *'xz'*, *'xyz'* or *'offset_scale'*. Refer to
  [`set_sheet_of_light_param`](set_sheet_of_light_param.md) for details on this parameter.
- ***'camera_parameter'*:** —

  the internal parameters of the camera used for the measurement.
  This pose is required when the calibration extent has been set
  to *'xyz'* or *'xz'*.
- ***'camera_pose'*:** —

  the pose of the world coordinate system relative to the camera
  coordinate system. This pose is required when the calibration extent
  has been set to *'xyz'* or *'xz'*.
- ***'lightplane_pose'*:** —

  the pose of the light-plane coordinate system relative to the
  world coordinate system. The light-plane
  coordinate system must be chosen so that its plane z=0 coincides
  with the light plane described by the light line projector.
  This pose is required when the calibration extent has been set
  to *'xyz'* or *'xz'*.
- ***'movement_pose'*:** —

  a pose representing the movement of the object between two successive
  profile images with respect to the measurement system built by the
  camera and the laser. This pose is required when the calibration
  extent has been set to *'xyz'*. It is ignored when the
  calibration extent has been set to *'xz'*.
- ***'scale'*:** —

  with this parameter you can scale the 3D coordinates X, Y and Z
  that result when applying the calibration transformations to the
  disparity image. *'scale'* must be specified as the ratio
  *desired unit/original unit*. The original unit is determined
  by the coordinates of the calibration object. If the original unit is
  meters (which is the case if you use the standard calibration plate),
  you can set the desired unit directly by selecting 'm', 'cm', 'mm'
  or 'um' for the parameter Scale. By default, *'scale'* is set
  to 1.0.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- SheetOfLightModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`Disparity`** (input_object)  singlechannelimage `→` object (real)

Height or range image to be calibrated.

**`SheetOfLightModelID`** (input_control, state is modified)  sheet_of_light_model `→`  (handle)

Handle of the sheet-of-light model.

## Example (HDevelop)

```
* ...
* Read an already acquired disparity map from file
read_image (Disparity, 'sheet_of_light/connection_rod_disparity.tif')
*
* Create a model and set the required parameters
gen_rectangle1 (ProfileRegion, 120, 75, 195, 710)
create_sheet_of_light_model (ProfileRegion, ['min_gray','num_profiles', \
                             'ambiguity_solving'], [70,290,'first'], \
                              SheetOfLightModelID)
set_sheet_of_light_param (SheetOfLightModelID, 'calibration', 'xyz')
set_sheet_of_light_param (SheetOfLightModelID, 'scale', 'mm')
set_sheet_of_light_param (SheetOfLightModelID, 'camera_parameter', \
                          CameraParameter)
set_sheet_of_light_param (SheetOfLightModelID, 'camera_pose', CameraPose)
set_sheet_of_light_param (SheetOfLightModelID, 'lightplane_pose', \
                          LightPlanePose)
set_sheet_of_light_param (SheetOfLightModelID, 'movement_pose', \
                          MovementPose)
*
* Apply the calibration transforms and
* get the resulting calibrated coordinates
apply_sheet_of_light_calibration (Disparity, SheetOfLightModelID)
get_sheet_of_light_result (X, SheetOfLightModelID, 'x')
get_sheet_of_light_result (Y, SheetOfLightModelID, 'y')
get_sheet_of_light_result (Z, SheetOfLightModelID, 'z')
*
```

## Result

The operator `apply_sheet_of_light_calibration` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Successors

`get_sheet_of_light_result`,
`get_sheet_of_light_result_object_model_3d`

## Module

3D Metrology
