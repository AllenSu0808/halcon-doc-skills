# get_line_of_sight (Operator)

## Name

`get_line_of_sight` — Compute the line of sight corresponding to a point in the image.

## Signature

`def get_line_of_sight(row: Sequence[float], column: Sequence[float], camera_param: Sequence[Union[int, float, str]]) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

## Description

`get_line_of_sight` computes the line of sight corresponding
to a pixel (*`row`*, *`column`*) in the image. The line
of sight is a (straight) line in the camera coordinate system, which
is described by two points (*`px`*,*`py`*,*`pz`*) and
(*`qx`*,*`qy`*,*`qz`*) on the line. The camera is
described by the internal camera parameters *`camera_param`*
(see [Calibration](toc_calibration.md) for details). If a pinhole camera is
used, the second point lies on the focal plane, i.e., for frame cameras, the
output parameter *`qz`* is equivalent to the focal length of
the camera, whereas for linescan cameras, *`qz`* also depends
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

**`row`** (input_control)  real-array `→` Sequence[float]

Row coordinate of the pixel.

**`column`** (input_control)  real-array `→` Sequence[float]

Column coordinate of the pixel.

**`camera_param`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameters.

**`px`** (output_control)  real-array `→` Sequence[float]

X coordinate of the first point on the line of sight
in the camera coordinate system

**`py`** (output_control)  real-array `→` Sequence[float]

Y coordinate of the first point on the line of sight
in the camera coordinate system

**`pz`** (output_control)  real-array `→` Sequence[float]

Z coordinate of the first point on the line of sight
in the camera coordinate system

**`qx`** (output_control)  real-array `→` Sequence[float]

X coordinate of the second point on the line of sight
in the camera coordinate system

**`qy`** (output_control)  real-array `→` Sequence[float]

Y coordinate of the second point on the line of sight
in the camera coordinate system

**`qz`** (output_control)  real-array `→` Sequence[float]

Z coordinate of the second point on the line of sight
in the camera coordinate system

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
