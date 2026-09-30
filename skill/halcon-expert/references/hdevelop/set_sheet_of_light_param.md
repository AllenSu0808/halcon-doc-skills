# set_sheet_of_light_param (Operator)

## Name

`set_sheet_of_light_param` — Set selected parameters of the sheet-of-light model.

## Signature

`set_sheet_of_light_param( : : SheetOfLightModelID, GenParamName, GenParamValue : )`

## Description

The operator `set_sheet_of_light_param` is used to set or change
a single parameter of a sheet-of-light model in order to
adapt the model to a particular measurement task.
All parameters, except the internal camera parameters
*'camera_parameters'* and the following poses
*'camera_pose'*, *'lightplane_pose'*, and
*'movement_pose'* can also be set while creating a sheet-of-light
model with [`create_sheet_of_light_model`](create_sheet_of_light_model.md).
The current configuration of the sheet-of-light model can be queried
with the operator [`get_sheet_of_light_param`](get_sheet_of_light_param.md).
A list with the names of all parameters that can be set for the
sheet-of-light model is returned by [`query_sheet_of_light_params`](query_sheet_of_light_params.md).

The following tables gives an overview, which parameters can be set
using `set_sheet_of_light_param` and which can be retrieved using
[`get_sheet_of_light_param`](get_sheet_of_light_param.md).

**Measurement of the profiles:**

| *`GenParamName`* | `set` | `get` |
| --- | --- | --- |
| *'ambiguity_solving'* | `x` | `x` |
| *'method'* | `x` | `x` |
| *'min_gray'* | `x` | `x` |
| *'num_profiles'* | `x` | `x` |
| *'score_type'* | `x` | `x` |

**Calibration of the measurement:**

| *`GenParamName`* | `set` | `get` |
| --- | --- | --- |
| *'calibration'* | `x` | `x` |
| *'calibration_object'* | `x` |  |
| *'camera_parameter'* | `x` | `x` |
| *'camera_pose'* | `x` | `x` |
| *'lightplane_pose'* | `x` | `x` |
| *'movement_pose'* | `x` | `x` |
| *'offset_x'* | `x` | `x` |
| *'offset_y'* | `x` | `x` |
| *'offset_z'* | `x` | `x` |
| *'scale'* | `x` | `x` |
| *'scale_x'* | `x` | `x` |
| *'scale_y'* | `x` | `x` |
| *'scale_z'* | `x` | `x` |

In the following the parameters are described:

**Measurement of the profiles:**

- ***'ambiguity_solving'*:** —

  This model parameter determines which candidate shall be chosen, if the
  determination of the position of the profile is ambiguous.

  - *'first'*: The first encountered candidate is returned.
    This method is the fastest.
  - *'last'*: The last encountered candidate is returned.
  - *'brightest'*: For each candidate, the brightness of the
    profile is computed and the candidate having the highest brightness
    is returned. The brightness is computed according to:
    $$brightness = \frac{1}{n} \sum_{i=0}^{n} g_i$$ ![figure](../assets/d971e2baa8b608b3.svg) where $g_{i}$ is the gray value of the pixel and n
    the number of pixels taken into consideration to determine the position
    of the profile.

  List of values:
   *'first'*, *'last'*, *'brightest'*

  Default:
   *'first'*
- ***'method'*:** —

  Defines the method used to
  determine the position of the profile.
  The values *'default'* and *'center_of_gravity'* both
  refer to the same method, whereby the position of the profile is
  determined column by column with subpixel accuracy by computing the
  center of gravity of the gray values $g_{i}$ of all
  pixels fulfilling the condition:
  $$g_{i}\ge^{\prime}\textit{min}\_\textit{gr ay}^{\prime}$$

  List of values:
   *'center_of_gravity'*, *'default'*

  Default:
   *'center_of_gravity'*
- ***'min_gray'*:** —

  The lowest gray values taken into account for the
  measurement of the position of the profile (see *'method'*
  above).

  Suggested values:
   *20*, *50*,
  *100*, *128*,
  *200*, *220*,
  *250*

  Default:
   *100*
- ***'num_profiles'*:** —

  Number of profiles for which memory has been allocated within the
  sheet-of-light model. By default, *'num_profiles'* is set
  to *512*. If this number of profiles is exceeded during the
  measurement, memory will be reallocated automatically at runtime.
  Since the reallocation process requires some time, we recommend to set
  *'num_profiles'* to a reasonable value before the measurement
  is started.

  Suggested values:
   *1*, *2*,
  *50*, *100*,
  *512*, *1024*,
  *3000*

  Default:
   *512*
- ***'score_type'*:** —

  This model parameter selects which type of score will be calculated
  during the measurement of the disparity. The score values give an
  advice on the quality of the computed disparity.

  *'none'*: No score is computed.

  *'width'*: For each pixel of the disparity, the score value
  is set to the number of pixels used to determine the disparity
  value.

  *'intensity'*: For each pixel of the disparity, a score value
  is evaluated by computing the local intensity of the profile according
  to: $$\text{score} = \frac{1}{n} \sum_{i=0}^{n} g_i$$ ![figure](../assets/2a2584b57e04f124.svg) where $g_{i}$ is the gray value of the pixel and n
  the number of pixels taken into consideration to determine the position
  of the profile.

  List of values:
   *'none'*, *'width'*, *'intensity'*

  Default:
   *'none'*

**Calibration of the measurement:**

- ***'calibration'*:** —

  Extent of the calibration transformation which shall be applied
  to the disparity image:

  *'none'*: No calibration transformation is applied.

  *'xz'*: The calibration transformations which describe the
  geometrical properties of the measurement system (camera and light
  line projector) are taken into account, but the movement of the object
  during the measurement is not taken into account.

  *'xyz'*: The calibration transformations which describe the
  geometrical properties of the measurement system (camera and light
  line projector) as well as the transformation which describe the
  movement of the object during the measurement are taken into
  account.

  *'offset_scale'*: A simplified set of parameters to describe
  the setup, that can be used with default parameters or can be
  controlled by six parameters.
  Three of the parameters describe an anisotropic scaling:
  *'scale_x'* describes the scaling of a
  pixel in column direction into the new x-axis,
  *'scale_y'* describes the linear movement between two profiles,
  and *'scale_z'* describes the scaling of
  to measured disparities into the new z-axis. The other three
  parameters describe the offset of the frame of reference of the
  resulting x,y,z values (*'offset_x'*, *'offset_y'*,
  *'offset_z'*).

  List of values:
   *'offset_scale'*, *'xz'*,
  *'xyz'*, *'none'*

  Default:
   *'none'*
- ***'calibration_object'*:** —

  The calibration object used for calibration with
  [`calibrate_sheet_of_light`](calibrate_sheet_of_light.md). If
  [`calibrate_sheet_of_light`](calibrate_sheet_of_light.md) shall be used for calibration,
  this parameter must be set to the filename of a calibration
  object created with [`create_sheet_of_light_calib_object`](create_sheet_of_light_calib_object.md).
- ***'camera_parameter'*:** —

  The internal parameters of the camera used for the measurement.
  Those parameters are required if the calibration extent has been
  set to *'xz'* or *'xyz'*. If
  [`calibrate_sheet_of_light`](calibrate_sheet_of_light.md) shall be used for calibration,
  this parameter is used to set the initial camera parameters.
- ***'camera_pose'*:** —

  The pose that transforms the camera coordinate system into the
  world coordinate system, i.e., the pose that could be used to
  transform point coordinates from the world coordinate system
  into the camera coordinate system. This pose is required if the
  calibration extent has been set to *'xz'* or
  *'xyz'*.

  Note that the world coordinate system is implicitly defined by
  setting the *'camera_pose'*.
- ***'lightplane_pose'*:** —

  The pose that transforms the light plane coordinate system into
  the world coordinate system, i.e., the pose that could be used
  to transform point coordinates from the world coordinate system
  into the light plane coordinate system.
  The light plane coordinate system must be chosen such that the
  plane z=0 coincides with the light plane. This pose is required
  if the calibration extent has been set to *'xz'* or
  *'xyz'*.
- ***'movement_pose'*:** —

  A pose representing the movement of the object between two successive
  profile images with respect to the measurement system built by the
  camera and the laser. This pose must be expressed in the world
  coordinate system. It is required if the calibration extent has been
  set to *'xyz'*.
- ***'offset_x'*:** —

  This value defines the x offset of reference frame for 3D results.
  This parameter is only applicable
  if the calibration extent has been set to *'offset_scale'*.

  Suggested values:
   *10.0*, *0.0*,
  *0.01*, *0.001*,
  *1.0e-6*

  Default:
   *0.0*
- ***'offset_y'*:** —

  This value defines the y offset of reference frame for xyz results.
  This parameter is only applicable
  if the calibration extent has been set to *'offset_scale'*.

  Suggested values:
   *10.0*, *0.0*,
  *0.01*, *0.001*,
  *1.0e-6*

  Default:
   *0.0*
- ***'offset_z'*:** —

  This value defines the z offset of reference frame for 3D results.
  This parameter is only applicable
  if the calibration extent has been set to *'offset_scale'*.

  Suggested values:
   *10.0*, *0.0*,
  *0.01*, *0.001*,
  *1.0e-6*

  Default:
   *0.0*
- ***'scale'*:** —

  With this value you can scale the 3D coordinates X, Y and Z that result
  when applying the calibration transformations to the disparity image.
  The model parameter *'scale'* must be specified as the ratio
  *desired unit/original unit*. The original unit is determined
  by the coordinates of the calibration object. If the original unit is
  meters (which is the case if you use the standard calibration plate),
  you can set *'scale'* to the desired unit directly by selecting
  *'m'*, *'cm'*, *'mm'*, *'microns'*, or
  *'um'*. This parameter can only be set
  if the calibration extent has been set to *'offset_scale'*,
  *'xz'* or *'xyz'*.

  Suggested values:
   *'m'*, *'cm'*,
  *'mm'*, *'microns'*,
  *'um'*, *1.0*,
  *0.01*, *0.001*,
  *1.0e-6*

  Default:
   *1.0*
- ***'scale_x'*:** —

  This value defines the width of a pixel in the 3D space.
  This parameter is only applicable
  if the calibration extent has been set to *'offset_scale'*.

  Suggested values:
   *10.0*, *1.0*,
  *0.01*, *0.001*,
  *1.0e-6*

  Default:
   *1.0*
- ***'scale_y'*:** —

  This value defines the linear movement between two profiles in
  the 3D space. This parameter is only applicable
  if the calibration extent has been set to *'offset_scale'*.

  Suggested values:
   *100.0*, *10.0*,
  *1.0*, *0.1*,
  *1.0e-6*

  Default:
   *10.0*
- ***'scale_z'*:** —

  This value defines the height of a pixel in
  the 3D space. This parameter is only applicable
  if the calibration extent has been set to *'offset_scale'*.

  Suggested values:
   *10.0*, *1.0*,
  *0.01*, *0.001*,
  *1.0e-6*

  Default:
   *1.0*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- SheetOfLightModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`SheetOfLightModelID`** (input_control, state is modified)  sheet_of_light_model `→`  (handle)

Handle of the sheet-of-light model.

**`GenParamName`** (input_control)  attribute.name `→`  (string)

Name of the model parameter that shall be adjusted for
the sheet-of-light model.

Default:
'method'

List of values:
'ambiguity_solving', 'calibration', 'calibration_object', 'camera_parameter', 'camera_pose', 'lightplane_pose', 'method', 'min_gray', 'movement_pose', 'num_profiles', 'offset_x', 'offset_y', 'offset_z', 'scale', 'scale_x', 'scale_y', 'scale_z', 'score_type'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Value of the model parameter that shall be adjusted
for the sheet-of-light model.

Default:
'center_of_gravity'

Suggested values:
'default', 'center_of_gravity', 'last', 'first', 'brightest', 'none', 'intensity', 'width', 'xz', 'xyz', 'offset_scale', 'm', 'cm', 'mm', 'um', 'microns', 1.0, 1e-2, 1e-3, 1e-6

## Result

The operator `set_sheet_of_light_param` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Successors

`get_sheet_of_light_param`,
`measure_profile_sheet_of_light`,
`apply_sheet_of_light_calibration`

## Alternatives

`create_sheet_of_light_model`

## See also

`query_sheet_of_light_params`,
`get_sheet_of_light_param`,
`get_sheet_of_light_result`

## Module

3D Metrology
