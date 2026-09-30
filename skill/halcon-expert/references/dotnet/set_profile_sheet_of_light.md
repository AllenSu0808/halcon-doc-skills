# SetProfileSheetOfLight (Operator)

## Name

`SetProfileSheetOfLight` — Set sheet of light profiles by measured disparities.

## Signature

`static void HOperatorSet.SetProfileSheetOfLight(HObject profileDisparityImage, HTuple sheetOfLightModelID, HTuple movementPoses)`

`void HImage.SetProfileSheetOfLight(HSheetOfLightModel sheetOfLightModelID, HTuple movementPoses)`

`void HSheetOfLightModel.SetProfileSheetOfLight(HImage profileDisparityImage, HTuple movementPoses)`

## Description

`SetProfileSheetOfLight` adds sheet-of-light profiles to the
sheet-of-light model *`sheetOfLightModelID`*. The profiles are specified
as rows in a disparity image in *`profileDisparityImage`*.
Each of the profiles can have an individual Pose set in
*`movementPoses`* which is interpreted as relative movement
to the previous row.
If no pose is set, the default transformation is
used, which can be set by [`SetSheetOfLightParam`](set_sheet_of_light_param.md). If only one pose
is set, this pose will become the default transformation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- sheetOfLightModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`profileDisparityImage`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2 / real)

Disparity image that contains several profiles.

**`sheetOfLightModelID`** (input_control, state is modified)  sheet_of_light_model `→` [HSheetOfLightModel](HSheetOfLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the sheet-of-light model.

**`movementPoses`** (input_control)  number-array `→` [HTuple](HTuple.md) (*int* / long / double)

Poses describing the movement of the scene under
measurement between the previously processed profile
image and the current profile image.

## Result

The operator `SetProfileSheetOfLight` returns the
value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Successors

`GetSheetOfLightResult`,
`GetSheetOfLightResultObjectModel3d`

## See also

`QuerySheetOfLightParams`,
`GetSheetOfLightParam`,
`GetSheetOfLightResult`,
`ApplySheetOfLightCalibration`

## Module

3D Metrology
