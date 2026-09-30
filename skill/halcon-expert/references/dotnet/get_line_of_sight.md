# GetLineOfSight (Operator)

## Name

`GetLineOfSight` — Compute the line of sight corresponding to a point in the image.

## Signature

`static void HOperatorSet.GetLineOfSight(HTuple row, HTuple column, HTuple cameraParam, out HTuple PX, out HTuple PY, out HTuple PZ, out HTuple QX, out HTuple QY, out HTuple QZ)`

`void HCamPar.GetLineOfSight(HTuple row, HTuple column, out HTuple PX, out HTuple PY, out HTuple PZ, out HTuple QX, out HTuple QY, out HTuple QZ)`

## Description

`GetLineOfSight` computes the line of sight corresponding
to a pixel (*`row`*, *`column`*) in the image. The line
of sight is a (straight) line in the camera coordinate system, which
is described by two points (*`PX`*,*`PY`*,*`PZ`*) and
(*`QX`*,*`QY`*,*`QZ`*) on the line. The camera is
described by the internal camera parameters *`cameraParam`*
(see [Calibration](toc_calibration.md) for details). If a pinhole camera is
used, the second point lies on the focal plane, i.e., for frame cameras, the
output parameter *`QZ`* is equivalent to the focal length of
the camera, whereas for linescan cameras, *`QZ`* also depends
on the motion of the camera with respect to the object. The
equation of the line of sight is given by

$$\begin{pmatrix}X\\Y\\Z\end{pmatrix}=\begin{pmatrix}PX\\PY\\PZ\end{pmatrix}+l\cdot\begin{pmatrix}QX- PX\\QY- PY\\QZ- PZ\end{pmatrix}$$ ![figure](../assets/35c14e3e91f07f32.svg)

The advantage of representing the line of sight as two points is
that it is easier to transform the line in 3D. To do so, all that
is necessary is to apply the operator [`AffineTransPoint3d`](affine_trans_point_3d.md)
to the two points.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`row`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the pixel.

**`column`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the pixel.

**`cameraParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters.

**`PX`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

X coordinate of the first point on the line of sight
in the camera coordinate system

**`PY`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Y coordinate of the first point on the line of sight
in the camera coordinate system

**`PZ`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Z coordinate of the first point on the line of sight
in the camera coordinate system

**`QX`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

X coordinate of the second point on the line of sight
in the camera coordinate system

**`QY`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Y coordinate of the second point on the line of sight
in the camera coordinate system

**`QZ`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Z coordinate of the second point on the line of sight
in the camera coordinate system

## Example (HDevelop)

```
* Set internal camera parameters.
* Note the, typically, these values are the result of a prior
* calibration.
gen_cam_par_area_scan_division (0.01, 30, 4.65e-006, 4.65e-006, \
                                640, 480, 1280, 960, CameraParam)
* Inverse projection.
get_line_of_sight([50, 100], [100, 200], CameraParam, PX, PY, PZ, QX, QY, QZ)
```

## Result

`GetLineOfSight` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised.

## Possible Predecessors

`ReadCamPar`,
`CameraCalibration`

## Possible Successors

`AffineTransPoint3d`

## See also

`CameraCalibration`,
`DispCaltab`,
`ReadCamPar`,
`Project3dPoint`,
`AffineTransPoint3d`

## Module

Calibration
