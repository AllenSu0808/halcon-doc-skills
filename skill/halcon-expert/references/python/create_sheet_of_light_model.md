# create_sheet_of_light_model (Operator)

## Name

`create_sheet_of_light_model` — Create a model to perform 3D-measurements using the sheet-of-light
technique.

## Signature

`def create_sheet_of_light_model(profile_region: HObject, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_sheet_of_light_model` creates a model to
perform 3D-Measurements using the sheet-of-light technique.

The sheet-of-light technique performs a three-dimensional reconstruction
of the surface of an opaque and diffuse reflecting solid by using an area
scan camera and a light line projector (typically a laser line projector).
The camera and the line projector must be mounted so that their main axis
form an angle of triangulation. The value of the angle of triangulation is
typically chosen between 30° and 60°. The projected light line defines a
plane in space. This plane intersects the surface of the solid under
measurement and builds a profile of the surface visible for the camera. By
moving the solid in front of the measurement system (i.e., the combination
of the camera and the line projector), it is possible to record the whole
surface of the solid. As an alternative, the measurement system can also
be moved over the surface under measurement. Please note that the profiles
must be oriented roughly horizontal in the profile images, because they
are processed column by column.

If geometrical information about the measurement setup is available, it
is possible to compute true three-dimensional coordinates of the
reconstructed surface. For an overview of the required geometrical (i.e.,
calibration) information, refer to the operator
[`set_sheet_of_light_param`](set_sheet_of_light_param.md). If such information is not available,
the result of the measurement is a disparity image, where each pixel holds
a record of the subpixel precise position of the detected profile.

The operator returns a handle to the sheet-of-light model in
*`sheet_of_light_model_id`*, which is used for all further operations on
the sheet-of-light model, like modifying parameters of the model, measuring
profiles, applying calibration transformations or accessing the results of
measurements.

**Mandatory input iconic parameters**

In order to perform measurements, you will have to set the following
input iconic parameter:

- ***`profile_region`*:** —

  defines the region of the
  profile images, which will be processed by the operator
  [`measure_profile_sheet_of_light`](measure_profile_sheet_of_light.md). This region should be rectangular
  and can be generated e.g., by using the operator [`gen_rectangle1`](gen_rectangle1.md).
  If the region passed to *`profile_region`* is not rectangular,
  its smallest enclosing rectangle (bounding box) will be used.
  Note that *`profile_region`* is only taken into account by the
  operator [`measure_profile_sheet_of_light`](measure_profile_sheet_of_light.md) and is ignored when
  disparity images are processed.

**Default settings of the sheet-of-light model parameters**

The default settings of the sheet-of-light model were chosen to perform
non-calibrated measurements in a basic configuration. The following
list provides an overview of the parameter values used by default
(refer to [`set_sheet_of_light_param`](set_sheet_of_light_param.md) for a detailed description
of all supported generic parameters):

- *"method"*
- *"min_gray"*
- *"num_profiles"*
- *"ambiguity_solving"*
- *"score_type"*
- *"calibration"*

**Modify the sheet-of-light model parameters**

We recommend to adapt the default parameters to your specific measurement
task, in order to enhance the quality of the measurement or to shorten the
runtime. You will also have to modify the default values of the model
parameters if you need calibrated results.

`create_sheet_of_light_model` provides the generic parameters
*`gen_param_name`* and *`gen_param_value`* to modify the default
value of most of the model parameters. Note that model parameters can also
be set by using the operator [`set_sheet_of_light_param`](set_sheet_of_light_param.md). Nevertheless,
with this second operator only one parameter can be set at the same time,
whereas it is possible to set more than one parameter at the time with
`create_sheet_of_light_model`. Refer to
[`set_sheet_of_light_param`](set_sheet_of_light_param.md) for a detailed description of all
supported generic parameters.

Please note that the following model parameters can not be set with the
operator `create_sheet_of_light_model`, and thus have to be set with
the operator [`set_sheet_of_light_param`](set_sheet_of_light_param.md): *"camera_parameter"*,
*"camera_pose"*, *"lightplane_pose"*, and
*"movement_pose"*.

It is possible to query the value of the model parameters with the
operator [`get_sheet_of_light_param`](get_sheet_of_light_param.md). The names of all supported
model parameters are returned by the operator
[`query_sheet_of_light_params`](query_sheet_of_light_params.md).

**Use the simplified sheet-of-light model parameters**

In case of a simple setup or if not a real metric calibration is necessary,
the transformation of the observed disparities into 3D values can
be controlled using a
simplified parameter set of the sheet-of-light model:

By setting the calibration with the [`set_sheet_of_light_param`](set_sheet_of_light_param.md) to
*"offset_scale"*, the poses and camera parameter are changed to such
values, that an offset of one pixel corresponds to one unit in the 3D
result. This allows to create a 3D object model and 3D images from
an uncalibrated sheet-of-light model.

The transformation from disparity to 3D coordinates can be controlled by
six parameters:
*"scale_x"*, *"scale_y"*, *"scale_z"*, *"offset_x"*,
*"offset_y"*, *"offset_z"*. Refer to
[`set_sheet_of_light_param`](set_sheet_of_light_param.md) for a detailed description of all
supported generic parameters.

**Use of a handle in multiple threads**

Please note that you have to take special care when using a handle of
a sheet-of-light-model *`sheet_of_light_model_id`* in multiple threads.
One and the same handle cannot be used concurrently in different threads
if they modify the handle. Thus, you have to be careful especially
if the threads call operators that change the data of the handle.
You can find an according hint in the *'Attention'* section of the
operators.
Anyway, if you still want to use the same handle in operators that
concurrently write into the handle in different threads you have to
synchronize the threads to assure that they do not access the same
handle simultaneously. If you are not sure if the usage of the same
handle is thread-safe, please see the *'Attention'* section of the
respective reference manual entry if it contains a warning pointing
to this problem. However, different handles can be used independently
and safely in different threads.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`profile_region`** (input_object)  region `→` HObject

Region of the images containing the profiles to be
processed. If the provided region is not rectangular,
its smallest enclosing rectangle will be used.

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Names of the generic parameters that can be
adjusted for the sheet-of-light model.

Default:
"min_gray"

List of values:
"ambiguity_solving", "calibration", "method", "min_gray", "num_profiles", "offset_x", "offset_y", "offset_z", "scale", "scale_x", "scale_y", "scale_z", "score_type"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Values of the generic parameters that can be
adjusted for the sheet-of-light model.

Default:
50

Suggested values:
"default", "center_of_gravity", "last", "first", "brightest", "none", "intensity", "width", "offset_scale", 50, 100, 150, 180

**`sheet_of_light_model_id`** (output_control)  sheet_of_light_model `→` HHandle

Handle for using and accessing the sheet-of-light
model.

## Example (HDevelop)

```
* Create the rectangular region in which the profiles are measured.
gen_rectangle1 (ProfileRegion, 120, 75, 195, 710)
*
* Create a model in order to measure profiles according to
* the sheet-of-light technique. Simultaneously set some
* parameters for the model.
create_sheet_of_light_model (ProfileRegion, ['min_gray','num_profiles', \
                             'ambiguity_solving','score_type'], \
                             [70,290,'first','width'], \
  SheetOfLightModelID)
*
* Measure the profile from successive images
for Index := 1 to 290 by 1
    read_image (ProfileImage, 'sheet_of_light/connection_rod_'+Index$'.3')
    dev_display (ProfileImage)
    dev_display (ProfileRegion)
    measure_profile_sheet_of_light (ProfileImage, SheetOfLightModelID, [])
endfor
*
* Get the resulting disparity and score images
get_sheet_of_light_result (Disparity, SheetOfLightModelID, 'disparity')
get_sheet_of_light_result (Score, SheetOfLightModelID, 'score')
*
* Close the sheet-of-light handle once the measurement
* has been performed
```

## Result

The operator `create_sheet_of_light_model` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Predecessors

`gen_rectangle1`

## Possible Successors

`set_sheet_of_light_param`,
`measure_profile_sheet_of_light`

## See also

`clear_sheet_of_light_model`,
`create_sheet_of_light_calib_object`,
`calibrate_sheet_of_light`

## Module

3D Metrology
