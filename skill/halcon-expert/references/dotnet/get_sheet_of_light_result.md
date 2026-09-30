# GetSheetOfLightResult (Operator)

## Name

`GetSheetOfLightResult` — Get the iconic results of a measurement performed with the sheet-of light
technique.

## Signature

`static void HOperatorSet.GetSheetOfLightResult(out HObject resultValue, HTuple sheetOfLightModelID, HTuple resultName)`

`void HImage.GetSheetOfLightResult(HSheetOfLightModel sheetOfLightModelID, HTuple resultName)`

`void HImage.GetSheetOfLightResult(HSheetOfLightModel sheetOfLightModelID, string resultName)`

`HImage HSheetOfLightModel.GetSheetOfLightResult(HTuple resultName)`

`HImage HSheetOfLightModel.GetSheetOfLightResult(string resultName)`

## Description

The operator `GetSheetOfLightResult` provides access to the
results of the calibrated and uncalibrated measurements performed with
a given sheet-of-light model. The different kinds of results can be
selected by setting the value of the parameter *`resultName`*
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
  image is empty. Refer to [`CreateSheetOfLightModel`](create_sheet_of_light_model.md) and
  [`SetSheetOfLightParam`](set_sheet_of_light_param.md) for details on the possible
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
*`resultName`* to *"x"*, *"y"* or *"z"* have
the semantic of coordinates with respect to the world coordinate
system that is implicitly defined during the calibration of the system.
The unit of the returned coordinates depends on the value of the
parameter *"scale"*. (see [`CreateSheetOfLightModel`](create_sheet_of_light_model.md)
and [`SetSheetOfLightParam`](set_sheet_of_light_param.md) for details on the possible
values of the model parameter *"scale"*.)

The operator `GetSheetOfLightResult` returns an empty object
if the desired result has not been computed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`resultValue`** (output_object)  singlechannelimage `→` [HImage](HImage.md) (real)

Desired measurement result.

**`sheetOfLightModelID`** (input_control)  sheet_of_light_model `→` [HSheetOfLightModel](HSheetOfLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the sheet-of-light model to be used.

**`resultName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Specify which result of the measurement shall
be provided.

Default:
"disparity"

List of values:
"disparity", "score", "x", "y", "z"

## Result

The operator `GetSheetOfLightResult` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Module

3D Metrology
