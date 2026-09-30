# disp_object_model_3d (Operator)

## Name

`disp_object_model_3d` — Display 3D object models.

## Signature

`disp_object_model_3d( : : WindowHandle, ObjectModel3D, CamParam, Pose, GenParamName, GenParamValue : )`

## Description

`disp_object_model_3d` displays the 3D object models of
*`ObjectModel3D`* in the window *`WindowHandle`*.
Set *`CamParam`* and the individual poses (in *`Pose`*) of the
3D object models to setup the displayed scene.
If an empty tuple is given for *`CamParam`*,
`disp_object_model_3d` uses default camera parameters that correspond
to the window size.
If *`CamParam`* is not empty, note that sometimes the aspect ratio
of *`WindowHandle`* should be similar to width and height
stored in *`CamParam`* in order to obtain the wanted results.
*`Pose`* can contain either multiple poses (one pose for each 3D
object model) or one pose for all 3D object models.
Thereby the poses are in the form $\mathrm{ccs} \mathbf{P}_{\mathrm{mcs}}$ ![figure](../assets/36630faf4c6dcd27.svg),
where *ccs* denotes the camera coordinate system and
*mcs* the model coordinate system (which is a 3D world coordinate
system), see [Transformations / Poses](toc_transformations_poses.md) and
`“Solution Guide III-C - 3D Vision”`.

If an empty tuple is given for *`Pose`*, `disp_object_model_3d`
estimates a pose, such that all 3D object models are visible.

3D object models containing triangles or polygons are displayed as solids,
whereas 3D object models containing only coordinates are displayed as point
clouds. 3D primitives (e.g., obtained by
[`fit_primitives_object_model_3d`](fit_primitives_object_model_3d.md)) are displayed as solids as well.
The generic parameter *'attribute'* can be used to explicitly select
in which way a 3D object model is visualized.

To render the 3D object models into an image, the operator
[`render_object_model_3d`](render_object_model_3d.md) can be used.

*`GenParamName`* and *`GenParamValue`* are used to further
configure the scene. The following values influence the whole scene:

- ***'disp_background'*:** —

  Flag, if the current window content should be used as background.

  List of values:
   *'true'*, *'false'*.

  Default:
   *'false'*.
- ***'light_position'*:** —

  Position of the light source. Must be given as a string
  containing four space separated floating point numbers.
  If the fourth number is 0.0, a directional light source is
  used (the first three components represent the direction),
  otherwise a point light source is used (with the first
  three components representing the position).

  Default:
   *'-100.0 -100.0 0.0 1.0'*.
- ***'light_ambient'*:** —

  Ambient part of the light source. Must be given as a string
  containing three space separated floating point numbers.

  Default:
   *'0.2 0.2 0.2'*.
- ***'light_diffuse'*:** —

  Diffuse part of the light source. Must be given as a string
  containing three space separated floating point numbers.

  Default:
   *'0.8 0.8 0.8'*.
- ***'colored'*:** —

  Display 3D object models in different colors. The value of this
  parameter defines the number of colors that are used.

  List of values:
   *3*, *6*, *12*.

  Default:
   all objects are displayed white.
- ***'object_index_persistence'*:** —

  Must be set to *'true'* to enable the object index query
  with [`get_disp_object_model_3d_info`](get_disp_object_model_3d_info.md).

  List of values:
   *'true'*, *'false'*.

  Default:
   *'false'*.
- ***'depth_persistence'*:** —

  Must be set to *'true'* to enable the depth query with
  [`get_disp_object_model_3d_info`](get_disp_object_model_3d_info.md).

  List of values:
   *'true'*, *'false'*.

  Default:
   *'false'*.
- ***'quality'*:** —

  Must be set to *'low'* to enable faster rendering without
  anti aliasing.

  List of values:
   *'low'*, *'high'*.

  Default:
   *'high'*.

The following parameters can be set for all 3D object models in the scene or
for a specific 3D object model by appending the index of the 3D object model
to the parameter name (e.g., *'color_0'* to set the color of the
first 3D object model).

- ***'attribute'*** —

  Explicitly select in which way a 3D object model is visualized.

  List of values:
   *'auto'*, *'faces'*,
  *'primitive'*, *'points'*,
  *'lines'*.

  Default:
   *'auto'*.
- ***'color'*:** —

  Color of the 3D object models. The available colors can be queried
  with the operator [`query_color`](query_color.md). In addition, the color may
  be specified as an RGB triplet in the form *'#rrggbb'*,
  where 'rr', 'gg', and 'bb' are hexadecimal numbers between '00'
  and 'ff', respectively.

  Suggested values:
   *'red'*, *'green'*.

  Default:
   *'white'*.
- ***'alpha'*:** —

  Translucency of the 3D object models. Displaying 3D object models
  with translucency set to less than 1.0 may significantly increase
  the runtime of `disp_object_model_3d`.

  Value range:
   [*0.0* (fully transparent) ...
  *1.0* (fully opaque)].

  Default:
   *1.0*.
- ***'disp_pose'*:** —

  Flag, if the pose of the 3D object models should be visualized.

  List of values:
   *'true'*, *'false'*.

  Default:
   *'false'*.
- ***'disp_lines'*:** —

  Flag, if the contours of the 3D object models' polygons should be
  displayed.

  List of values:
   *'true'*, *'false'*.

  Default:
   *'false'*.
- ***'disp_normals'*:** —

  Flag, if the surface normals of the 3D object models should be
  visualized.

  List of values:
   *'true'*, *'false'*.

  Default:
   *'false'*.
- ***'line_color'*:** —

  Color of the lines if *'disp_lines'* is set to
  *'true'*. The available colors can be queried with the
  operator [`query_color`](query_color.md). In addition, the color may be
  specified as an RGB triplet in the form *'#rrggbb'*,
  where 'rr', 'gg', and 'bb' are hexadecimal numbers.

  Suggested values:
   *'red'*, *'green'*.

  Default:
   The value of *'color'*.
- ***'line_width'*:** —

  Sets the width of lines in pixel.

  Default:
   *1.0*.
- ***'normal_color'*:** —

  Color of the visualized normals if *'disp_normals'* is set
  to *'true'*. The available colors can be queried with the
  operator [`query_color`](query_color.md). In addition, the color may be
  specified as an RGB triplet in the form *'#rrggbb'*,
  where 'rr', 'gg', and 'bb' are hexadecimal numbers.

  Suggested values:
   *'red'*, *'green'*.

  Default:
   The value of *'color'*.
- ***'point_size'*:** —

  Sets the diameter of the points in pixel.

  Default:
   *3.5*.
- ***'lut'*:** —

  Sets the LUT that transforms the values of the attribute set with
  *'color_attrib'* into a color.

  See [`set_lut`](set_lut.md) for available LUTs. If *'lut'* is set to
  anything but *'default'*, *'color'* is ignored.

  Default:
   *'default'*.
- ***'color_attrib'*:** —

  Name of a point attribute that is used for false color visualization.

  If an attribute is set, the color of the displayed 3D points is
  determined by the point's attribute value and the currently set
  LUT (see *'lut'*). This way, it is possible to visualize
  attributes in false colors.

  Example: If *'color_attrib'* is set to *'coord_z'*, and
  *'lut'* is set to *'color1'*, the z-coordinates will be
  color coded from red to blue.

  If *'lut'* is set to *'default'*, the attribute values are
  used to scale the color that was set by the parameter *'color'*.

  If *'lut'* is set to a different value, the attribute values of
  all points are internally scaled to the interval [0,255] and used as
  input value for the LUT function.

  The mapping is also controlled by the parameters
  *'color_attrib_start'* and *'color_attrib_end'* (see below).

  If faces are displayed, their color is interpolated between the
  color of the corner points.

  Suggested values:
   *'none'*, *'&distance'*,
  *'coord_x'*, *'coord_y'*,
  *'coord_z'*,
  user defined point attributes, or any other
  point attribute available.

  Default:
   *'none'*.
- ***'color_attrib_start'*,*'color_attrib_end'*:** —

  The range of interest of the values of the attribute set with
  *'color_attrib'*.

  The attribute values between *'color_attrib_start'* and
  *'color_attrib_end'* are scaled to the start and end of the
  selected LUT. Attribute values outside the selected range are clipped.
  This allows to use a fixed color mapping which will not be distorted by
  outliers.

  If set to *'auto'*, the minimum attribute value is mapped to the
  start of the LUT, the maximum is mapped to the end of the LUT,
  *except* if *'color_attrib'* is *'normal_x'*,
  *'normal_y'*, or *'normal_z'*.
  In this case, start and end are automatically set to *-1* and
  *1*.

  It is possible to enter start value that is higher than the end value.
  This will in effect flip the used LUT.

  Suggested values:
   *'auto'*, *0*, *0.1*,
  *1*, *100*, *255*.

  Default:
   *'auto'*.
- ***'red_channel_attrib'*,
  *'green_channel_attrib'*,
  *'blue_channel_attrib'*:** —

  Name of a point attribute that is used for the red, green, or blue
  color channel.

  This is most useful when used with a group of three connected
  attributes, like RGB colors or normal vectors.
  This way it is possible to display points in colored texture, e.g.,
  display the object model with overlayed RGB-sensor data, or display
  point normals in false colors.

  To display only a single attribute in false colors, please use
  *'color_attrib'* (see above).

  By default, the attribute values are assumed to lie between
  *0* and *255*.
  If the attributes have a different range, you additionally have to set
  the parameters *'rgb_channel_attrib_start'* and
  *'rgb_channel_attrib_end'* (see below).

  If only 1 or 2 channels are set, the remaining channels use the RGB
  value of the color set with *'color'*.

  If faces are displayed, their color is interpolated between the
  color of the corner points.

  Suggested values:
   *'none'*, *'&red'*,
  *'&green'*, *'&blue'*,
  *'normal_x'*, *'normal_y'*,
  *'normal_z'*, user defined point
  attributes, or any other point
  attribute available.

  Default:
   *'none'*.
- ***'rgb_channel_attrib_start'*,
  *'rgb_channel_attrib_end'*:** —

  The range of interest of the values of attributes set with
  *'red_channel_attrib'*, *'green_channel_attrib'*, and
  *'blue_channel_attrib'*.

  These parameters define the value range that is scaled to the full RGB
  channels. This is useful, if the input attribute values are not in the
  interval [0,255].

  If set to *'auto'*, the minimum attribute value is mapped to
  *0*, the maximum is mapped to *255*, *except*
  if the attribute is *'normal_x'*, *'normal_y'*,
  or *'normal_z'*.
  In this case, start and end are automatically set to *-1* and
  *1*.

  It is possible to enter start value that is higher than the end value.
  This will in effect invert the displayed RGB colors.

  The range can be set for the channels individually by replacing
  *'rgb'* in the parameter name with the channel name, e.g.,
  *'green_channel_attrib_start'*.

  Suggested values:
   *'auto'*, *0*, *0.1*,
  *1*, *100*, *255*.

  Default:
   *0*, *255*.

All generic parameters are evaluated from left to right. For example, to set
the color of the first 3D object model to red and the color of all other
3D object models to green, set *`GenParamName`* to
*['color','color_0']* and *`GenParamValue`* to
*['green','red']*.

`disp_object_model_3d` requires OpenGL 2.1, GLSL 1.2, and the OpenGL
extensions GL_EXT_framebuffer_object and GL_EXT_framebuffer_blit.
Otherwise the compatibility mode is automatically enabled.
On graphics cards with low memory the following error messages could occur
if rendering in a window with high resolution:

Low level error: 'Incomplete attachment'

Unhanded Exception: 'Required framebuffer object is unsupported'

Solutions:

Set the parameter *'quality'* to *'low'* or use the
compatibility mode to reduce the requirements of the graphics card.

The system variable (see [`set_system`](set_system.md))
*'opengl_compatibility_mode_enable'* can be set to *'true'*
to permanently enable the visualization in compatibility mode with lower
OpenGL requirements.
This mode requires OpenGL 1.1.
In compatibility mode the parameters *'object_index_persistence'*,
*'depth_persistence'* and *'quality'* are not used.

On Linux Remote Desktop *'disp_background'* is not supported.

## Attention

Cameras with hypercentric lenses are not supported.
For displaying large faces (or primitives) with a non-zero distortion
in *`CamParam`*, note that the distortion is only applied to the
points of the model. In the projection, these points are subsequently
connected by straight lines. For a good approximation of the distorted
lines, please use a triangulation with sufficiently small triangles.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`ObjectModel3D`** (input_control)  object_model_3d(-array) `→`  (handle)

Handles of the 3D object models.

**`CamParam`** (input_control)  campar `→`  (real / integer / string)

Camera parameters of the scene.

Default:
[]

**`Pose`** (input_control)  pose(-array) `→`  (real / integer)

3D poses of the objects.

Default:
[]

**`GenParamName`** (input_control)  string-array `→`  (string)

Names of the generic parameters.

Default:
[]

List of values:
'alpha', 'attribute', 'blue_channel_attrib', 'color', 'color_attrib', 'color_attrib_end', 'color_attrib_start', 'colored', 'compatibility_mode_enable', 'depth_persistence', 'disp_background', 'disp_lines', 'disp_normals', 'disp_pose', 'green_channel_attrib', 'light_ambient', 'light_diffuse', 'light_position', 'line_color', 'line_width', 'lut', 'normal_color', 'object_index_persistence', 'point_size', 'quality', 'red_channel_attrib', 'rgb_channel_attrib_end', 'rgb_channel_attrib_start'

**`GenParamValue`** (input_control)  string-array `→`  (string / integer / real)

Values of the generic parameters.

Default:
[]

List of values:
'auto', 'blue', 'coord_x', 'coord_y', 'coord_z', 'faces', 'false', 'green', 'lines', 'normal_x', 'normal_y', 'normal_z', 'points', 'primitive', 'red', 'true'

## Result

`disp_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.
If the image rendering exceeds the available memory of the graphics card, the
error 5188 is raised.

## Possible Predecessors

`find_surface_model`,
`fit_primitives_object_model_3d`,
`read_object_model_3d`,
`segment_object_model_3d`

## Possible Successors

`get_disp_object_model_3d_info`

## See also

`render_object_model_3d`,
`project_object_model_3d`,
`project_shape_model_3d`,
`object_model_3d_to_xyz`

## Module

3D Metrology
