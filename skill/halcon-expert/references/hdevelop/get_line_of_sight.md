# get_line_of_sight (Operator)

## Name

`get_line_of_sight` — Compute the line of sight corresponding to a point in the image.

## Signature

`get_line_of_sight( : : Row, Column, CameraParam : PX, PY, PZ, QX, QY, QZ)`

## Description

`get_line_of_sight` computes the line of sight corresponding
to a pixel (*`Row`*, *`Column`*) in the image. The line
of sight is a (straight) line in the camera coordinate system, which
is described by two points (*`PX`*,*`PY`*,*`PZ`*) and
(*`QX`*,*`QY`*,*`QZ`*) on the line. The camera is
described by the internal camera parameters *`CameraParam`*
(see [Calibration](toc_calibration.md) for details). If a pinhole camera is
used, the second point lies on the focal plane, i.e., for frame cameras, the
output parameter *`QZ`* is equivalent to the focal length of
the camera, whereas for linescan cameras, *`QZ`* also depends
on the motion of the camera with respect to the object. The
equation of the line of sight is given by

$$\begin{pmatrix}X\\Y\\Z\end{pmatrix}=\begin{pmatrix}PX\\PY\\PZ\end{pmatrix}+l\cdot\begin{pmatrix}QX- PX\\QY- PY\\QZ- PZ\end{pmatrix}$$ ![figure](../assets/35c14e3e91f07f32.svg)

The advantage of representing the line of sight as two points is
that it is easier to transform the line in 3D. To do so, all that
is necessary is to apply the operator [`affine_trans_point_3d`](affine_trans_point_3d.md)
to the two points.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Row`** (input_control)  real-array `→`  (real)

Row coordinate of the pixel.

**`Column`** (input_control)  real-array `→`  (real)

Column coordinate of the pixel.

**`CameraParam`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters.

**`PX`** (output_control)  real-array `→`  (real)

X coordinate of the first point on the line of sight
in the camera coordinate system

**`PY`** (output_control)  real-array `→`  (real)

Y coordinate of the first point on the line of sight
in the camera coordinate system

**`PZ`** (output_control)  real-array `→`  (real)

Z coordinate of the first point on the line of sight
in the camera coordinate system

**`QX`** (output_control)  real-array `→`  (real)

X coordinate of the second point on the line of sight
in the camera coordinate system

**`QY`** (output_control)  real-array `→`  (real)

Y coordinate of the second point on the line of sight
in the camera coordinate system

**`QZ`** (output_control)  real-array `→`  (real)

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

`get_line_of_sight` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised.

## Possible Predecessors

`read_cam_par`,
`camera_calibration`

## Possible Successors

`affine_trans_point_3d`

## See also

`camera_calibration`,
`disp_caltab`,
`read_cam_par`,
`project_3d_point`,
`affine_trans_point_3d`

## Module

Calibration
