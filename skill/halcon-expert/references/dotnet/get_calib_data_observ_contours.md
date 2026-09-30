# GetCalibDataObservContours (Operator)

## Name

`GetCalibDataObservContours` — Get contour-based observation data from a calibration data model.

## Signature

`static void HOperatorSet.GetCalibDataObservContours(out HObject contours, HTuple calibDataID, HTuple contourName, HTuple cameraIdx, HTuple calibObjIdx, HTuple calibObjPoseIdx)`

`HXLDCont HCalibData.GetCalibDataObservContours(string contourName, int cameraIdx, int calibObjIdx, int calibObjPoseIdx)`

## Description

The operator `GetCalibDataObservContours` reads contour-based
observation data from a calibration data model *`calibDataID`*
and returns it in *`contours`*.
These contours result from a preceding call of [`FindCalibObject`](find_calib_object.md).
The parameters *`cameraIdx`*, *`calibObjIdx`*, and
*`calibObjPoseIdx`* are indices of the observing camera, calibration
plate, and calibration object pose.
Together, they specify an observation from the calibration model.
Note that if an observation exists, but it was stored
in the calibration model *`calibDataID`* by
[`SetCalibDataObservPoints`](set_calib_data_observ_points.md), no contour-based results can be
returned.

By setting *`contourName`* to one of the following values, you can
select the specific type of the contour results:

- ***"marks"*:** —

  The contours of the calibration plate marks.
- ***"marks_with_hole"*:** —

  The calibration plate marks which contain a hole. In this case, the
  output returned in *`contours`* are regions instead of contours.
- ***"caltab"*:** —

  The contour of the calibration plate finder pattern.
- ***"last_caltab"*:** —

  The contour of the calibration plate finder pattern, which has been
  extracted by the last successful preceding call to
  [`FindCalibObject`](find_calib_object.md).
  Note that the observation of the successful call to
  [`FindCalibObject`](find_calib_object.md) is used and consequently the values in
  *`cameraIdx`*, *`calibObjIdx`*, and *`calibObjPoseIdx`*
  are ignored.

The mentioned finder pattern depends on the calibration plate:

- Calibration plates with hexagonally arranged marks:
  Special mark hexagon (i.e., a mark and its six neighbors) where either
  four or six marks contain a hole, see [`CreateCaltab`](create_caltab.md).
- Calibration plates with rectangularly arranged marks:
  The border of the calibration plate with a triangle in one corner.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Contour-based result(s).

**`calibDataID`** (input_control)  calib_data `→` [HCalibData](HCalibData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a calibration data model.

**`contourName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of contour objects to be returned.

Default:
"marks"

List of values:
"caltab", "last_caltab", "marks", "marks_with_hole"

**`cameraIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Index of the observing camera.

Default:
0

**`calibObjIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Index of the observed calibration plate.

Default:
0

**`calibObjPoseIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Index of the observed calibration object pose.

Default:
0

## Module

Calibration
