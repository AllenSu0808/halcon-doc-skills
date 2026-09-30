# SetPaint (Operator)

## Name

`SetPaint` — Define the gray value output mode.

## Signature

`static void HOperatorSet.SetPaint(HTuple windowHandle, HTuple mode)`

`void HWindow.SetPaint(HTuple mode)`

## Description

`SetPaint` defines the output mode for gray value display
(single- or multichannel) in the window. The mode is used by
[`DispObj`](disp_obj.md), [`DispImage`](disp_image.md), and [`DispColor`](disp_color.md).

Different image types and their possible implication on the *`mode`*:

- Gray images can also be interpreted as 3D data, depending on the
  gray value. To view these 3D plots, select the modes *"3d_plot"*.
- Three-channel images are interpreted as RGB images.
- Vector field images can be viewed as *"vector_field"*.

In most cases the setting *`mode`* *"default"*
is the most suitable.

Depending on the selected mode, the *`mode`* may accept a tuple as value.
In these cases the entries can be passed the following ways:

- Only the name of the mode is passed: The defaults or the most
  recently used values are used, respectively.

  Example: `set_paint(WindowHandle,'3d_plot')`
- All values are passed: All output characteristics can be set.

  *Example:* `set_paint(WindowHandle, ['3d_plot', 'shaded', 8,
  0.939, -0.052, 0.296, -0.165, 0.401, 0.072, -0.047, -0.073])`
- Only the first n values are passed: Only the passed values are
  changed.

  *Example:* `set_paint(WindowHandle,['3d_plot','texture'])`
- Some of the values are replaced by an asterisk ('*'): The value of
  the replaced parameters is not changed.

  *Example:* `set_paint(WindowHandle,['3d_plot', '*' ,8])`

If the current mode is *"default"*, HALCON chooses a suitable
algorithm for the output of 2- and 3-channel images. No
`SetPaint` call is necessary in this case.

Apart from `SetPaint` there are other operators that affect
the output of gray values. The most important of them are
[`SetPart`](set_part.md), [`SetPartStyle`](set_part_style.md) and [`SetLut`](set_lut.md).
Some output modes display gray values using
region output (e.g., *"3d_plot"*).
In these modes, parameters set with [`SetColor`](set_color.md),
[`SetRgb`](set_rgb.md), [`SetHsi`](set_hsi.md), [`SetShape`](set_shape.md), and [`SetLineWidth`](set_line_width.md)
influence gray value output.
In case of unexpected results, check the values of the display parameters.

All available painting modes can be queried with [`QueryPaint`](query_paint.md).
Possible values for *`mode`*:

- ***"default"*** —

  Optimal display on given hardware (default value).
  Its behavior depends on the number of channels of the input image:

  - One-channel image: Output the single channel.
  - Two-channel images: Output the first channel.
  - Three-channel images: Output as RGB image.
- ***["3d_plot", Mode, Step, qa, qb, qc, qd, ZoomFac, CenterRow,
  CenterCol, CenterHeight]*** —

  Gray values are interpreted as a 3D height field and displayed using OpenGL.
  Thereby the different parameters are:

  - *"Mode"*: Specifies the way in which the height
    field is displayed. The following modes are supported:

    - *"texture"*: The height field is displayed as a closed
      surface and colored using texture mapping.
      The texture is passed as the second channel (for a gray-valued texture)
      or as the second to fourth channel (for a colored texture) of the image
      to display.
    - *"shaded"*: The height field is displayed as a closed
      surface and colored using the current LUT.
    - *"hidden_lines"*: The height field is displayed as a hidden
      line plot and colored using the current LUT.
    - *"contour_lines"*: Height lines are extracted
      and displayed at their actual height.
      Again the lines are colored using the current LUT.
  - *"Step"*: Step width, i.e., at what intervals samples in row
    and column direction are taken from the image. The smaller
    this parameter is chosen, the finer the resulting height field.
    However, computation time increases while this parameter decreases.
    In the case of *"contour_lines"* this parameter corresponds to the
    number of intervals the height range is divided into.
  - *"qa"*,*"qb"*,*"qc"*,*"qd"*: The four values of a
    unit quaternion, describing the orientation of the height field
    (see [`AxisAngleToQuat`](axis_angle_to_quat.md) for more information on quaternions).
  - *"ZoomFac"*: Zooming factor, whereby smaller values implicate
    higher zooming.
  - *"CenterRow"*, *"CenterCol"*, *"CenterHeight"*:
    Position of the actual center of view defined by row, column, and height.
    These values must be scaled to the interval [*-0.5*, *0.5*].

  Automatic parameter determination:
  You can set *"qa"* (fourth value in the tuple) or
  *"ZoomFac"* (eighth value in the tuple) to *"auto"*.
  Then, the zooming factor and the center of view are
  determined automatically such that the plot of the height field fills the
  window as good as possible.
  By setting *"qa"* to *"auto"*, the previous
  orientation (or the default one) is kept.
  By setting *"ZoomFac"* to *"auto"*,
  the provided orientation is used.
  It is important that the part of the window is
  set correctly (using [`SetPart`](set_part.md)) before `SetPaint` is called.
  It is not possible to set any parameters after *"auto"* in the tuple.
  Furthermore *"auto"* will only work correctly if
  *"scale_plot"* is set
  to *"true"* using [`SetWindowParam`](set_window_param.md).

  *Example:*
  `set_paint(WindowHandle, ['3d_plot','shaded',4,'auto'])`

  This mode allows interactive display of the 3D data.
  For an interactive rate, your graphics card needs to
  be powerful enough and support OpenGL. See the operator
  [`UpdateWindowPose`](update_window_pose.md) for an intuitive way of modifying the
  parameters of the 3D plot (e.g., with the mouse).

  The colors of the axis are influenced by the colors set using
  [`SetRgb`](set_rgb.md), [`SetColor`](set_color.md), and [`SetColored`](set_colored.md). The first
  three colors set this way are used as colors for row, column, and height
  axis (in this order).

  Additional parameters concerning the 3D plot can be set using the operator
  [`SetWindowParam`](set_window_param.md).

  If you intend to use *"3d_plot"* on a Unix-like system, make sure
  you have sufficient permissions on your graphics device.

  Default:
   *["3d_plot", "shaded", 8, 0.939, -0.052, 0.296,
  -0.165, 0.401, 0.072, -0.047, -0.073]*

  Restriction:
   Only for one-channel images.
- ***["vector_field", Mode, Step, MinLength, ScaleLength,
  CircleSize]*** —

  Output a vector field. Thus, for *`mode`* *"vector_field"*
  a circle is drawn for each vector at the position of the pixel.
  Furthermore, a line segment is drawn with the current vector.
  Thereby the different parameters are:

  - *"Mode"*: Tells whether the visualized vector fields contain
    absolute or relative coordinates. Possible values:

    - *"auto"* (*default*): The visualization depends on
      the semantic type of the vector field.
    - *"absolute"*: Display vector fields containing absolute
      coordinates.
    - *"relative"*: Display vector fields containing relative
      coordinates.
  - *"Step"*: Step size for drawing the vectors, i.e., the
    distance between the drawn vectors.
  - *"MinLength"*: Minimum length a vector needs in order to be
    displayed.
  - *"ScaleLength"*: Scales the vector length.
  - *"CircleSize"*: Diameter of the drawn circles.

  It should be noted that by setting *"vector_field"* only the
  internal parameters *"Mode"*, *"Step"*, *"MinLength"*,
  *"ScaleLength"*, and *"CircleSize"* are changed.
  The current display mode is not changed.

  Vector field images are always displayed as vector fields, no matter which
  *`mode`* is selected with `SetPaint`.

  *Example:*
  `set_paint(WindowHandle,['vector_field','auto',16,2,3,5])`

  This results in an output of every 16th vector, that is longer than 2
  pixels. Each vector is multiplied by 3 for output.

  Restriction:
   Only for vector field images.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`mode`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string* / int / long / double)

Output mode. Additional parameters possible.

Default:
"default"

List of values:
"3d_plot", "default", "vector_field"

## Result

`SetPaint` returns 2 (
H_MSG_TRUE)
if the parameter is correct and the
window is valid. Otherwise an exception is raised.

## Possible Predecessors

`QueryPaint`,
`GetPaint`

## Possible Successors

`DispImage`

## See also

`GetPaint`,
`QueryPaint`,
`DispImage`,
`SetShape`,
`SetRgb`,
`SetColor`,
`SetGray`,
`SetWindowParam`,
`UpdateWindowPose`

## Module

Foundation
