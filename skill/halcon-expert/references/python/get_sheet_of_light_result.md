# get_sheet_of_light_result (Operator)

## Name

`get_sheet_of_light_result` — Get the iconic results of a measurement performed with the sheet-of light
technique.

## Signature

`def get_sheet_of_light_result(sheet_of_light_model_id: HHandle, result_name: MaybeSequence[str]) -> HObject`

## Description

The operator `get_sheet_of_light_result` provides access to the
results of the calibrated and uncalibrated measurements performed with
a given sheet-of-light model. The different kinds of results can be
selected by setting the value of the parameter *`result_name`*
as described below:

**Non-calibrated results:**

- ***"disparity"*:** —

  the measured disparity i.e., the subpixel row value at which the
  profile was detected is returned for each pixel. The disparity
  values can be considered as non-calibrated pseudo-range values.
- ***"score"*:** —

  the score values computed according to the value of the parameter
  *"score_type"* is returned. If the parameter
  *"score_type"* has been set to *"none"*, no score
  value is computed during the measurement, therefore the returned
  image is empty. Refer to [`create_sheet_of_light_model`](create_sheet_of_light_model.md) and
  [`set_sheet_of_light_param`](set_sheet_of_light_param.md) for details on the possible
  values of the model parameter *"score_type"*.

**Calibrated results:**

- ***"x"*:** —

  The calibrated X-coordinates of the reconstructed surface is
  returned as an image.
- ***"y"*:** —

  The calibrated Y-coordinates of the reconstructed surface is
  returned as an image.
- ***"z"*:** —

  The calibrated Z-coordinates of the reconstructed surface is
  returned as an image.

Please, note that the pixel values of the images returned when setting
*`result_name`* to *"x"*, *"y"* or *"z"* have
the semantic of coordinates with respect to the world coordinate
system that is implicitly defined during the calibration of the system.
The unit of the returned coordinates depends on the value of the
parameter *"scale"*. (see [`create_sheet_of_light_model`](create_sheet_of_light_model.md)
and [`set_sheet_of_light_param`](set_sheet_of_light_param.md) for details on the possible
values of the model parameter *"scale"*.)

The operator `get_sheet_of_light_result` returns an empty object
if the desired result has not been computed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`result_value`** (output_object)  singlechannelimage `→` HObject (real)

Desired measurement result.

**`sheet_of_light_model_id`** (input_control)  sheet_of_light_model `→` HHandle

Handle of the sheet-of-light model to be used.

**`result_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Specify which result of the measurement shall
be provided.

Default:
"disparity"

List of values:
"disparity", "score", "x", "y", "z"

## Result

The operator `get_sheet_of_light_result` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Module

3D Metrology
