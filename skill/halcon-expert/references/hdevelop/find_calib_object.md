# find_calib_object (Operator)

## Name

`find_calib_object` — Find the HALCON calibration plate and set the extracted points and
contours in a calibration data model.

## Signature

`find_calib_object(Image : : CalibDataID, CameraIdx, CalibObjIdx, CalibObjPoseIdx, GenParamName, GenParamValue : )`

## Description

`find_calib_object` searches in *`Image`* for a HALCON
calibration plate corresponding to the description of the calibration object
with the index *`CalibObjIdx`* from the calibration data model
*`CalibDataID`*. If a calibration plate is found,
`find_calib_object` extracts the centers and the contours of its marks
and estimates the pose of the plate relative to the observing camera
*`CameraIdx`*. All collected observation data is stored in the
calibration data model for the calibration object pose
*`CalibObjPoseIdx`*. In order to ensure a successful detection of the
calibration plate, at least one finder pattern has to be visible in the
image. For calibration plates with hexagonally arranged marks this is
a special mark hexagon where either four or six marks contain a hole, while
for calibration plates with rectangularly arranged marks this is the border
of the calibration plate with a triangle in one corner.

### Preparation of the input data

Before the operator `find_calib_object` can be called, a calibration
data model has to be defined performing the following steps:

1. **Create a calibration data model** with the operator
   [`create_calib_data`](create_calib_data.md), specifying the number of cameras in the setup
   and the number of used calibration objects.
2. **Specify the camera type and the initial internal camera
   parameters** for all cameras with the operator
   [`set_calib_data_cam_param`](set_calib_data_cam_param.md). Note that only cameras of the same
   type can be calibrated in a single setup.
3. **Specify the description of all calibration objects** with the
   operator [`set_calib_data_calib_object`](set_calib_data_calib_object.md).
   Note that for a successful call of `find_calib_object` a valid
   description file of the calibration plate is necessary. This description
   file has to be set beforehand via the operator
   [`set_calib_data_calib_object`](set_calib_data_calib_object.md).
   As a consequence, the usage of a user-defined calibration object can only
   be made by the operator [`set_calib_data_observ_points`](set_calib_data_observ_points.md).

### Collecting observation data

`find_calib_object` is used to collect observations in a calibration
data model. Beyond, it stores additional observation
data that cannot be added to the model with
[`set_calib_data_observ_points`](set_calib_data_observ_points.md) and that is dependent on the used
calibration plate. While for calibration plates with rectangularly arranged
marks (see [`gen_caltab`](gen_caltab.md)) the rim of the calibration plate is added to
the observations, calibration plates with hexagonal pattern (see
[`create_caltab`](create_caltab.md)) store one of their finder pattern. Additionally and
irrespective of the used calibration plate, the contour of each mark is added
to the calibration model.

### Setting additional parameters

Using **calibration plates with hexagonally arranged marks**, the
following additional parameter can be set via *`GenParamName`* and
*`GenParamValue`*:

- ***'sigma'*:** —

  Smoothing factor for the extraction of the mark contours. For increasing
  values of *'sigma'*, the filter width and thereby the amount of
  smoothing increases (see also [`edges_sub_pix`](edges_sub_pix.md) for the influence of
  the filter width on the Canny filter).

  Suggested values:
   *0.5*, *0.7*,
  *0.9*, *1.0*,
  *1.2*, *1.5*

  Default:
   *1.0*

For **calibration plates with rectangularly arranged marks**,
`find_calib_object` essentially encapsulates the sequence of three
operator calls: [`find_caltab`](find_caltab.md), [`find_marks_and_pose`](find_marks_and_pose.md) and
[`set_calib_data_observ_points`](set_calib_data_observ_points.md). For this kind of calibration plates
the following parameters can be set using *`GenParamName`* and
*`GenParamValue`*:

- ***'alpha'*:** —

  Smoothing factor for the extraction of the mark contours. For increasing
  values of *'alpha'*, the filter width and thereby the amount of
  smoothing decreases (see also [`edges_sub_pix`](edges_sub_pix.md) for the influence of
  the filter width on the Lanser2 filter ).

  Suggested values:
   *0.5*, *0.7*,
  *0.9*, *1.0*,
  *1.2*, *1.5*

  Default:
   *0.9*
- ***'gap_tolerance'*:** —

  Tolerance factor for gaps between the marks. If the marks appear
  closer to each other than expected, you might set
  *'gap_tolerance'* < *1.0* to avoid disturbing patterns
  outside the calibration plate to be associated with the calibration
  plate. This can typically happen if the plate is strongly tilted and
  positioned in front of a background that exposes mark-like patterns.
  If the distances between single marks vary in a wide range, e.g., if
  the calibration plate appears with strong perspective distortion in
  the image, you might set *'gap_tolerance'* > *1.0* to
  enforce the marks grouping (see also [`find_caltab`](find_caltab.md)).

  Suggested values:
   *0.75*, *0.9*,
  *1.0*, *1.1*,
  *1.2*, *1.5*

  Default:
   *1.0*
- ***'max_diam_marks'*:** —

  Maximum expected diameter of the marks (needed internally by
  [`find_marks_and_pose`](find_marks_and_pose.md)). By default, this value is estimated
  by the preceding internal call to [`find_caltab`](find_caltab.md). However, if
  the estimation is erroneous for no obvious reason or the internal call to
  [`find_caltab`](find_caltab.md) fails or is simply skipped (see
  *'skip_find_caltab'* below), you might have to adjust this
  value.

  Suggested values:
   *50.0*, *100.0*,
  *150.0*, *200.0*,
  *300.0*
- ***'skip_find_caltab'*:** —

  Skip the internal call to [`find_caltab`](find_caltab.md). If activated, only the
  domain of *`Image`* reduces the search area for the internal call
  of [`find_marks_and_pose`](find_marks_and_pose.md). Thus, a user defined calibration plate
  region can be incorporated by setting
  *'skip_find_caltab'*=*'false'* and reducing
  the *`Image`* domain to the user region.

  List of values:
   *'false'*, *'true'*

  Default:
   *'false'*

If using a HALCON calibration plate as calibration object, it is recommended
to use `find_calib_object` instead of
[`set_calib_data_observ_points`](set_calib_data_observ_points.md) where possible, since the contour
information, which it stores in the calibration data model, enables a more
precise calibration procedure with [`calibrate_cameras`](calibrate_cameras.md).

After a successful call to `find_calib_object`, the extracted
points can be queried by [`get_calib_data_observ_points`](get_calib_data_observ_points.md) and the
extracted contours can be accessed by [`get_calib_data_observ_contours`](get_calib_data_observ_contours.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator modifies the state of the following input parameter:

- CalibDataID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image.

**`CalibDataID`** (input_control, state is modified)  calib_data `→`  (handle)

Handle of a calibration data model.

**`CameraIdx`** (input_control)  number `→`  (integer)

Index of the observing camera.

Default:
0

Suggested values:
0, 1, 2

**`CalibObjIdx`** (input_control)  number `→`  (integer)

Index of the calibration object.

Default:
0

Suggested values:
0, 1, 2

**`CalibObjPoseIdx`** (input_control)  number `→`  (integer)

Index of the observed calibration object.

Default:
0

Suggested values:
0, 1, 2

Restriction:
`CalibObjPoseIdx >= 0`

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Names of the generic parameters to be set.

Default:
[]

List of values:
'alpha', 'gap_tolerance', 'max_diam_marks', 'sigma', 'skip_find_caltab'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (string / real / integer)

Values of the generic parameters to be set.

Default:
[]

Suggested values:
0.5, 0.9, 1.0, 1.2, 1.5, 2.0, 'true', 'false'

## Possible Predecessors

`read_image`,
`find_marks_and_pose`,
`set_calib_data_cam_param`,
`set_calib_data_calib_object`

## Possible Successors

`set_calib_data`,
`calibrate_cameras`

## Alternatives

`find_caltab`,
`find_marks_and_pose`,
`set_calib_data_observ_points`

## Module

Calibration
