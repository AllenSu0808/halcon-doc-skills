# GetSheetOfLightResultObjectModel3d (Operator)

## Name

`GetSheetOfLightResultObjectModel3d` — Get the result of a calibrated measurement performed with the
sheet-of-light technique as a 3D object model.

## Signature

`static void HOperatorSet.GetSheetOfLightResultObjectModel3d(HTuple sheetOfLightModelID, out HTuple objectModel3D)`

`void HObjectModel3D.GetSheetOfLightResultObjectModel3d(HSheetOfLightModel sheetOfLightModelID)`

`HObjectModel3D HSheetOfLightModel.GetSheetOfLightResultObjectModel3d()`

## Description

The operator `GetSheetOfLightResultObjectModel3d` returns the
result of a fully calibrated sheet-of-light measurement as a 3D object
model. The handle of the sheet-of-light model with which the
measurement is performed must be passed to *`sheetOfLightModelID`*.
The calibration extent of the sheet-of-light model (*"calibration"*)
must have been set to *"xyz"* or *"offset_scale"*
before applying the measurement,
otherwise the computed coordinates cannot be returned as a 3D object model
and an exception is raised.

The handle of the 3D object model resulting from the measurement is returned
in *`objectModel3D`*. For the 3D points within this 3D object model
no triangular meshing is available, therefore no faces are stored in the 3D
object model. If a 3D object model with triangular meshing is required for
the subsequent processing, use the operator [`GetSheetOfLightResult`](get_sheet_of_light_result.md)
in order to retrieve the *"x"*, *"y"*, and *"z"*
coordinates from the sheet-of-light model and then call the operator
[`XyzToObjectModel3d`](xyz_to_object_model_3d.md) with suitable parameters. Refer to
[`XyzToObjectModel3d`](xyz_to_object_model_3d.md) for more information about 3D object models.

The unit of the returned coordinates depends on the value of the parameter
*"scale"* that was set for the sheet-of-light model before applying
the measurement.
See [`CreateSheetOfLightModel`](create_sheet_of_light_model.md) and [`SetSheetOfLightParam`](set_sheet_of_light_param.md)
for details on the possible values of the model parameter *"scale"*.
The operator `GetSheetOfLightResultObjectModel3d` returns a
handle to an empty 3D object model if the desired result has not been
measured yet.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`sheetOfLightModelID`** (input_control)  sheet_of_light_model `→` [HSheetOfLightModel](HSheetOfLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle for accessing the sheet-of-light model.

**`objectModel3D`** (output_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the resulting 3D object model.

## Result

The operator `GetSheetOfLightResultObjectModel3d` returns the
value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Predecessors

`CreateSheetOfLightModel`,
`MeasureProfileSheetOfLight`,
`CalibrateSheetOfLight`

## Possible Successors

`ClearObjectModel3d`

## Module

3D Metrology
