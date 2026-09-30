# get_calib_data_observ_contours (Operator)

## Name

`get_calib_data_observ_contours` — Get contour-based observation data from a calibration data model.

## Signature

`def get_calib_data_observ_contours(calib_data_id: HHandle, contour_name: str, camera_idx: int, calib_obj_idx: int, calib_obj_pose_idx: int) -> HObject`

## Description

The operator `get_calib_data_observ_contours` reads contour-based
observation data from a calibration data model *`calib_data_id`*
and returns it in *`contours`*.
These contours result from a preceding call of [`find_calib_object`](find_calib_object.md).
The parameters *`camera_idx`*, *`calib_obj_idx`*, and
*`calib_obj_pose_idx`* are indices of the observing camera, calibration
plate, and calibration object pose.
Together, they specify an observation from the calibration model.
Note that if an observation exists, but it was stored
in the calibration model *`calib_data_id`* by
[`set_calib_data_observ_points`](set_calib_data_observ_points.md), no contour-based results can be
returned.

By setting *`contour_name`* to one of the following values, you can
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
  [`find_calib_object`](find_calib_object.md).
  Note that the observation of the successful call to
  [`find_calib_object`](find_calib_object.md) is used and consequently the values in
  *`camera_idx`*, *`calib_obj_idx`*, and *`calib_obj_pose_idx`*
  are ignored.

The mentioned finder pattern depends on the calibration plate:

- Calibration plates with hexagonally arranged marks:
  Special mark hexagon (i.e., a mark and its six neighbors) where either
  four or six marks contain a hole, see [`create_caltab`](create_caltab.md).
- Calibration plates with rectangularly arranged marks:
  The border of the calibration plate with a triangle in one corner.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (output_object)  xld_cont(-array) `→` HObject

Contour-based result(s).

**`calib_data_id`** (input_control)  calib_data `→` HHandle

Handle of a calibration data model.

**`contour_name`** (input_control)  string `→` str

Name of contour objects to be returned.

Default:
"marks"

List of values:
"caltab", "last_caltab", "marks", "marks_with_hole"

**`camera_idx`** (input_control)  number `→` int

Index of the observing camera.

Default:
0

**`calib_obj_idx`** (input_control)  number `→` int

Index of the observed calibration plate.

Default:
0

**`calib_obj_pose_idx`** (input_control)  number `→` int

Index of the observed calibration object pose.

Default:
0

## Module

Calibration
