# VectorToPose (Operator)

## Name

`VectorToPose` — Compute an absolute pose out of point correspondences between
world and image coordinates.

## Signature

`static void HOperatorSet.VectorToPose(HTuple worldX, HTuple worldY, HTuple worldZ, HTuple imageRow, HTuple imageColumn, HTuple cameraParam, HTuple method, HTuple qualityType, out HTuple pose, out HTuple quality)`

`static HPose HImage.VectorToPose(HTuple worldX, HTuple worldY, HTuple worldZ, HTuple imageRow, HTuple imageColumn, HCamPar cameraParam, string method, HTuple qualityType, out HTuple quality)`

`static HPose HImage.VectorToPose(HTuple worldX, HTuple worldY, HTuple worldZ, HTuple imageRow, HTuple imageColumn, HCamPar cameraParam, string method, string qualityType, out double quality)`

`HPose HCamPar.VectorToPose(HTuple worldX, HTuple worldY, HTuple worldZ, HTuple imageRow, HTuple imageColumn, string method, HTuple qualityType, out HTuple quality)`

`HPose HCamPar.VectorToPose(HTuple worldX, HTuple worldY, HTuple worldZ, HTuple imageRow, HTuple imageColumn, string method, string qualityType, out double quality)`

`HTuple HPose.VectorToPose(HTuple worldX, HTuple worldY, HTuple worldZ, HTuple imageRow, HTuple imageColumn, HCamPar cameraParam, string method, HTuple qualityType)`

`double HPose.VectorToPose(HTuple worldX, HTuple worldY, HTuple worldZ, HTuple imageRow, HTuple imageColumn, HCamPar cameraParam, string method, string qualityType)`

## Description

The operator `VectorToPose` computes a pose out of at least
three or four (depending on *`method`*) point correspondences
of 3D world coordinates (*`worldX`*, *`worldY`*,
*`worldZ`*), given in meters, and 2D image coordinates
(*`imageRow`*, *`imageColumn`*), given in pixels, as well as
the internal camera parameters (*`cameraParam`*).
Thereby the pose (the external camera parameters) is in the form
$\mathrm{CCS} P_{\mathrm{wcs}}$ ![figure](../assets/4c18b1c4fb564c93.svg), where
*ccs* denotes the camera coordinate system and
*wcs* the world coordinate system
(see [Transformations / Poses](toc_transformations_poses.md)
and `“Solution Guide III-C - 3D Vision”`).

### Parameter Method

By setting the parameter *`method`*, it is possible to choose
what kind of algorithm is used for the pose computation.

Methods supported for **perspective area scan cameras**:

|  |  |  |
| --- | --- | --- |
| *`method`* | *When to use* | *Minimum number of point correspondences* |
| *"analytic"* [1] | Default method for general cases | 4 |
| *"iterative"* [2] | If only three or four point correspondences are used or if the world points are close to being planar | 3 |
| *"planar_analytic"* [4] | If the world points lie in a horizontal plane ($\texttt{WorldZ}=0$) | 4 |

The numbers in square brackets in the table above refer to the publications
the implementations of the corresponding methods are based on.

Methods supported for **telecentric area or line scan cameras**:

|  |  |  |
| --- | --- | --- |
| *`method`* | *When to use* | *Minimum number of point correspondences* |
| *"telecentric"* [3] | Default method for general cases | 4 |
| *"telecentric_robust"* [3] | For very ill-posed point configurations where *`quality`* has an unlikely large value | 4 |
| *"telecentric_planar"* [3] | If the world points lie in a horizontal plane ($\texttt{WorldZ}=0$) | 3 |
| *"telecentric_planar_robust"* [3] | For very ill-posed point configurations where the world points lie in a horizontal plane ($\texttt{WorldZ}=0$) and *`quality`* has an unlikely large value | 3 |

The numbers in square brackets in the table above refer to the publications
the implementations of the corresponding methods are based on.

Methods supported for **perspective line scan cameras**:

|  |  |  |
| --- | --- | --- |
| *`method`* | *When to use* | *Minimum number of point correspondences* |
| *"line_scan"* | Default method for general cases | 3 |

### Parameters CameraParam and Quality

All methods need the inner camera parameters obtained from
[`CameraCalibration`](camera_calibration.md) to solve the pose estimation problem.
They must be passed in *`cameraParam`*.

The user can specify in *`qualityType`* one or more quality
measures of the pose to be evaluated. The resulting quality
evaluations are returned concatenated in *`quality`*.
Currently, only *"error"* is supported. It corresponds to
the root-mean-square error in pixels of the projected 3D world
coordinates.

### General Remarks

If a method for planar world points is chosen, all world points are
assumed to lie in the plane $\texttt{WorldZ}=0$. Therefore, the z-component of the world coordinates can be
left empty (*`worldZ`* = *[]*) since only 2D
correspondences are used in this case.

For telecentric cameras, the translation in *z* obviously
cannot be determined. It is set to *0* in *`pose`*.

For planar world points and telecentric cameras, there are always
two possible equivalent poses. This ambiguity can only be resolved
by some additional knowledge. `VectorToPose` returns an
arbitrary solution of the two possible solutions in this case. The
other solution can be calculated easily by replacing the values of
$\alpha$ and $\beta$ in *`pose`* by
$360-\alpha$ and $360-\beta$.

For perspective line scan cameras, the call to
`VectorToPose` corresponds to the following operator
sequence:

|  |
| --- |
| [`GetLineOfSight(ImageRow, ImageColumn, CameraParam, PX, PY, PZ, QX, QY, QZ)`](get_line_of_sight.md) |
| [`PointsToPlueckerLine(PX, PY, PZ, QX, QY, QZ, LX, LY, LZ, MX, MY, MZ)`](points_to_pluecker_line.md) |
| [`PointPlueckerLineToHomMat3d("rigid", WorldX, WorldY, WorldZ, LX, LY, LZ, MX, MY, MZ, HomMat3D)`](point_pluecker_line_to_hom_mat3d.md) |
| [`HomMat3dToPose(HomMat3D, Pose)`](hom_mat3d_to_pose.md) |
|  |

In contrast to the methods for other camera types, an error in 3D
space is minimized in this case (see
[`PointPlueckerLineToHomMat3d`](point_pluecker_line_to_hom_mat3d.md)). However, like for all
other methods, the quality evaluation is performed in pixels. If it
is essential that a pixel error is optimized, this can be done as
shown in the example below.

## Attention

The method *"analytic"* only allows a maximum number of 32767
point correspondences.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`worldX`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

X-Component of world coordinates.

Number of elements:
WorldX >= 4

**`worldY`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Y-Component of world coordinates.

Number of elements:
WorldY == WorldX

**`worldZ`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Z-Component of world coordinates.

Number of elements:
WorldZ == WorldX || WorldZ == 0

**`imageRow`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row-Component of image coordinates.

Number of elements:
ImageRow == WorldX

**`imageColumn`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column-Component of image coordinates.

Number of elements:
ImageColumn == WorldX

**`cameraParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

The inner camera parameters from camera calibration.

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Kind of algorithm

Default:
"iterative"

List of values:
"analytic", "iterative", "line_scan", "planar_analytic", "telecentric", "telecentric_planar", "telecentric_planar_robust", "telecentric_robust"

**`qualityType`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Type of pose quality to be returned in Quality.

Default:
"error"

List of values:
"error"

**`pose`** (output_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Pose.

**`quality`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Pose quality.

## Example (HDevelop)

```
* Optimize the pixel error line scan cameras. We assume that the
* point correspondences (Row, Col) - (PX, PY, PZ) have already been
* computed and the internal camera parameters CamParam have already
* been calibrated.
vector_to_pose (PX, PY, PZ, Row, Col, CamParam, 'line_scan', \
                'error', PoseObjectSpace, RMS)
* Use PoseObjectSpace as the starting value for a camera calibration
* that only optimizes the pose.
create_calib_data ('calibration_object', 1, 1, CalibDataID)
set_calib_data_cam_param (CalibDataID, 0, [], CamParam)
set_calib_data_calib_object (CalibDataID, 0, [PX, PY, PZ])
set_calib_data (CalibDataID, 'camera', 0, \
                'excluded_settings', 'params')
set_calib_data_observ_points (CalibDataID, 0, 0, 0, Row, Col, \
                              'all', PoseObjectSpace)
calibrate_cameras (CalibDataID, Error)
get_calib_data (CalibDataID, 'calib_obj_pose', [0, 0], 'pose', Pose)
clear_calib_data (CalibDataID)
* As an alternative, the following one-line code can be used.
camera_calibration (PX, PY, PZ, Row, Col, CamParam, PoseObjectSpace, \
                    'pose', _, Pose, Error)
```

## Result

`VectorToPose` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct.

## See also

`ProjHomMat2dToPose`,
`VectorToRelPose`,
`CameraCalibration`

## References

[1] Francesc Moreno-Noguer, Vincent Lepetit, and Pascal Fua:
“Accurate Non-Iterative O(n) Solution to the PnP Problem”;
Eleventh IEEE International Conference on Computer Vision, 2007.
  
[2] Gerald Schweighofer, and Axel Pinz: “Robust Pose Estimation from a Planar
Target”; Transactions on Pattern Analysis and Machine Intelligence (PAMI),
28(12):2024-2030, 2006.
  
[3] Carsten Steger: “Algorithms for the Orthographic-*n*-Point
Problem”; Journal of Mathematical Imaging and Vision, vol. 60,
no. 2, pp. 246-266, 2018.
  
[4] Zhengyou Zhang: “A flexible new technique for camera calibration.”;
Transactions on Pattern Analysis and Machine Intelligence (PAMI),
22(11):1330-1334, 2000.

## Module

Calibration
