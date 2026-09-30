# SetScene3dInstanceParam (Operator)

## Name

`SetScene3dInstanceParam` — Set parameters of an instance in a 3D scene.

## Signature

`static void HOperatorSet.SetScene3dInstanceParam(HTuple scene3D, HTuple instanceIndex, HTuple genParamName, HTuple genParamValue)`

`void HScene3D.SetScene3dInstanceParam(HTuple instanceIndex, HTuple genParamName, HTuple genParamValue)`

`void HScene3D.SetScene3dInstanceParam(int instanceIndex, HTuple genParamName, HTuple genParamValue)`

## Description

`SetScene3dInstanceParam` sets parameters of the
instance *`instanceIndex`* in the 3D scene *`scene3D`*. The name
and value of a parameter must be given in *`genParamName`*
and *`genParamValue`*. All parameters are applied to all instances.

The following values can be set:

- ***"visible"*** —

  Visibility of the 3D object models. If set to
  *"false"* this instance is not displayed.

  List of values:
   *"true"*, *"false"*.

  Default:
   *"true"*.
- ***"attribute"*** —

  Explicitly select in which way a 3D object model is visualized.

  List of values:
   *"auto"*, *"faces"*,
  *"primitive"*, *"points"*,
  *"lines"*.

  Default:
   *"auto"*.
- ***"color"*:** —

  Color of the 3D object model. The available colors can be queried
  with the operator [`QueryColor`](query_color.md). In addition, the color may
  be specified as an RGB triplet in the form *"#rrggbb"*,
  where *"rr"*, *"gg"*, and *"bb"* are
  hexadecimal numbers between *"00"*
  and *"ff"*, respectively.

  Suggested values:
   *"red"*, *"green"*.

  Default:
   *"white"*
- ***"alpha"*:** —

  Transparency of the 3D object models. Displaying 3D object models
  with transparency set to less than 1.0 may significantly increase
  the runtime of [`DisplayScene3d`](display_scene_3d.md) and
  [`RenderScene3d`](render_scene_3d.md).

  Value range:
   floating point value between 0.0 (fully transparent)
  and 1.0 (fully opaque).

  Default:
   1.0
- ***"disp_pose"*:** —

  Flag, if the pose of the 3D object models should be visualized.

  List of values:
   *"true"*, *"false"*.

  Default:
   *"false"*.
- ***"disp_lines"*:** —

  Flag, if the contours of the 3D object models' polygons should be
  displayed.

  List of values:
   *"true"*, *"false"*.

  Default:
   *"false"*.
- ***"disp_normals"*:** —

  Flag, if the surface normals of the 3D object models should be
  visualized.

  List of values:
   *"true"*, *"false"*.

  Default:
   *"false"*.
- ***"line_color"*:** —

  Color of the lines if *"disp_lines"* is set to
  *"true"*. The available colors can be queried with the
  operator [`QueryColor`](query_color.md). In addition, the color may be
  specified as an RGB triplet in the form *"#rrggbb"*,
  where *"rr"*, *"gg"*, and *"bb"* are
  hexadecimal numbers.

  Suggested values:
   *"red"*, *"green"*.

  Default:
   The value of *"color"*.
- ***"line_width"*:** —

  Sets the width of lines in pixel.

  Default:
   *1.0*
- ***"normal_color"*:** —

  Color of the visualized normals if *"disp_normals"* is set
  to *"true"*. The available colors can be queried with the
  operator [`QueryColor`](query_color.md). In addition, the color may be
  specified as an RGB triplet in the form *"#rrggbb"*,
  where *"rr"*, *"gg"*, and *"bb"* are
  hexadecimal numbers.

  Suggested values:
   *"red"*, *"green"*.

  Default:
   The value of *"color"*
- ***"point_size"*:** —

  Sets the diameter of the points in pixel.

  Default:
   *3.5*.
- ***"lut"*:** —

  Sets the LUT that transforms the values of the attribute set with
  *"color_attrib"* into a color.

  See [`SetLut`](set_lut.md) for available LUTs. If *"lut"* is set to
  anything but *"default"*, *"color"* is ignored.

  Default:
   *"default"*.
- ***"color_attrib"*:** —

  Name of a point attribute that is used for false color visualization.

  If an attribute is set, the color of the displayed 3D points is
  determined by the point's attribute value and the currently set
  LUT (see *"lut"*). This way, it is possible to visualize
  attributes in false colors.

  Example: If *"color_attrib"* is set to *"coord_z"*, and
  *"lut"* is set to *"color1"*, the z-coordinates will be
  color coded from red to blue.

  If *"lut"* is set to *"default"*, the attribute values are
  used to scale the color that was set by the parameter *"color"*.

  If *"lut"* is set to a different value, the attribute values of
  all points are internally scaled to the interval [0,255] and used as
  input value for the LUT function.

  The mapping is also controlled by the parameters
  *"color_attrib_start"* and *"color_attrib_end"* (see below).

  If faces are displayed, their color is interpolated between the
  color of the corner points.

  Suggested values:
   *"none"*, *"&distance"*,
  *"coord_x"*, *"coord_y"*,
  *"coord_z"*,
  user defined point attributes,
  or any other point attribute available.

  Default:
   *"none"*.
- ***"color_attrib_start"*,*"color_attrib_end"*:** —

  The range of interest of the values of the attribute set with
  *"color_attrib"*.

  The attribute values between *"color_attrib_start"* and
  *"color_attrib_end"* are scaled to the start and end of the
  selected LUT. Attribute values outside the selected range are clipped.
  This allows to use a fixed color mapping which will not be distorted by
  outliers.

  If set to *"auto"*, the minimum attribute value is mapped to the
  start of the LUT, the maximum is mapped to the end of the LUT,
  *except* if *"color_attrib"* is *"normal_x"*,
  *"normal_y"*, or *"normal_z"*.
  In this case, start and end are automatically set to -1 and 1.

  It is possible to enter start value that is higher than the end value.
  This will in effect flip the used LUT.

  Suggested values:
   *0*, *0.1*, *1*,
  *100*, *255*, *"auto"*.

  Default:
   *"auto"*.
- ***"red_channel_attrib"*,
  *"green_channel_attrib"*,
  *"blue_channel_attrib"*:** —

  Name of a point attribute that is used for the red, green, or blue
  color channel.

  This is most useful when used with a group of three connected
  attributes, like RGB colors or normal vectors.
  This way it is possible to display points in colored texture, e.g.,
  display the object model with overlayed RGB-sensor data, or display
  point normals in false colors.

  To display only a single attribute in false colors, please use
  *"color_attrib"* (see above).

  By default, the attribute values are assumed to lie between 0 and 255.
  If the attributes have a different range, you additionally have to set
  the parameters *"rgb_channel_attrib_start"* and
  *"rgb_channel_attrib_end"* (see below).

  If only 1 or 2 channels are set, the remaining channels use the RGB
  value of the color set with *"color"*.

  If faces are displayed, their color is interpolated between the
  color of the corner points.

  Suggested values:
   *"none"*, *"&red"*,
  *"&green"*, *"&blue"*,
  *"normal_x"*, *"normal_y"*,
  *"normal_z"*,
  user defined point attributes,
  or any other point attribute available.

  Default:
   *"none"*.
- ***"rgb_channel_attrib_start"*,
  *"rgb_channel_attrib_end"*:** —

  The range of interest of the values of attributes set with
  *"red_channel_attrib"*, *"green_channel_attrib"*, and
  *"blue_channel_attrib"*.

  These parameters define the value range that is scaled to the full RGB
  channels. This is useful, if the input attribute values are not in the
  interval [0,255].

  If set to *"auto"*, the minimum attribute value is mapped to 0,
  the maximum is mapped to 255, *except* if the attribute is
  *"normal_x"*, *"normal_y"*, or *"normal_z"*.
  In this case, start and end are automatically set to -1 and 1.

  It is possible to enter start value that is higher than the end value.
  This will in effect invert the displayed RGB colors.

  The range can be set for the channels individually by replacing
  *"rgb"* in the parameter name with the channel name, e.g.,
  *"green_channel_attrib_start"*.

  Suggested values:
   *"auto"*, *0*, *0.1*,
  *1*, *100*, *255*.

  Default:
   *0*, *255*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`instanceIndex`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Index of the instance.

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

Default:
"color"

List of values:
"alpha", "attribute", "blue_channel_attrib", "color", "color_attrib", "color_attrib_end", "color_attrib_start", "disp_lines", "disp_normals", "disp_pose", "green_channel_attrib", "line_color", "line_width", "lut", "normal_color", "point_size", "red_channel_attrib", "rgb_channel_attrib_end", "rgb_channel_attrib_start", "visible"

**`genParamValue`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string* / int / long / double)

Values of the generic parameters.

Default:
"green"

Suggested values:
"true", "false", "coord_x", "coord_y", "coord_z", "normal_x", "normal_y", "normal_z", "red", "green", "blue", "auto", "faces", "primitive", "points", "lines"

## Result

`SetScene3dInstanceParam` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`AddScene3dInstance`

## See also

`SetScene3dParam`

## Module

3D Metrology
