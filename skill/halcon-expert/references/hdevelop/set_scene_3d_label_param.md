# set_scene_3d_label_param (Operator)

## Name

`set_scene_3d_label_param` — Set parameters of a text label in a 3D scene.

## Signature

`set_scene_3d_label_param( : : Scene3D, LabelIndex, GenParamName, GenParamValue : )`

## Description

`set_scene_3d_label_param` sets parameters of the
label *`LabelIndex`* in the 3D scene *`Scene3D`*. The name
and value of a parameter must be given in *`GenParamName`*
and *`GenParamValue`*. It is only possible to provide one
*`GenParamName`*,*`GenParamValue`* pair but multiple
labels. The parameter is applied to all labels in *`LabelIndex`*.

The following values can be set:

- ***'reference_point'*:** —

  Coordinates of the reference point, as a tuple of *[X, Y, Z]*
  coordinates. To remove the current reference point, it is
  possible to pass an empty tuple for *'reference_point'*.
  This is only possible if *'relates_to'* is
  *'window'*.
- ***'position'*:** —

  Position (relative or absolute depending on the parameter
  *'relates_to'*) of the label, as a tuple of
  *[Row, Column]* coordinates or one of the following predefined
  positions.

  List of values:
   *'top_left'*, *'top'*, *'top_right'*,
  *'left'*, *'center'*, *'right'*,
  *'bottom_left'*, *'bottom'*, or
  *'bottom_right'*.
- ***'relates_to'*:** —

  Relation of the position. May be *'window'*
  (fixed positioning in window coordinates) or *'point'*
  (positioning relative to the reference point).
  *'relates_to'* cannot be set to *'point'* if
  the reference point has been set to an empty tuple.

  List of values:
   *'window'* , *'point'*.

  Default:
   *'window'*.
- ***'text'*:** —

  Text of the label. Multiple Lines must be separated with
  *'\n'*.
- ***'font'*:** —

  Font of the text label.

  Suggested values:
   Available fonts can be queried using
  [`query_font`](query_font.md).

  Default:
   Font of the first window the scene is
  displayed in, default system font otherwise.
- ***'text_color'*:** —

  Color of the text on the label. The available colors can be queried
  with the operator [`query_color`](query_color.md). In addition, the color may
  be specified as an RGB triplet in the form *'#rrggbb'*,
  where *'rr'*, *'gg'*, and *'bb'* are
  hexadecimal numbers between *'00'*
  and *'ff'*, respectively.

  Suggested values:
   *'red'*, *'green'*.

  Default:
   *'white'*.
- ***'alpha'*:** —

  Transparency of the text label's background.

  Value range:
   floating point value between 0.0 (fully transparent)
  and 1.0 (fully opaque).

  Default:
   *1.0*.
- ***'color'*:** —

  Color of the label itself. The available colors can be queried
  with the operator [`query_color`](query_color.md). In addition, the color may
  be specified as an RGB triplet in the form *'#rrggbb'*,
  where *'rr'*, *'gg'*, and *'bb'* are
  hexadecimal numbers between *'00'*
  and *'ff'*, respectively.

  Suggested values:
   *'red'*, *'green'*.

  Default:
   *'gray'*.
- ***'disp_background'*:** —

  Flag that determines if the background of the label should be
  visualized.

  List of values:
   *'true'*, *'false'*.

  Default:
   *'true'*.
- ***'disp_connecting_line'*:** —

  Flag that determines if the connecting line between the label and
  reference 3D point should be visualized.

  List of values:
   *'true'*, *'false'*.

  Default:
   *'true'*.
- ***'visible'*:** —

  Sets the visibility of the label. If set to
  *'if_point_is_visible'*, the label is only visible if
  its reference point is visible.
  If the compatibility mode is enabled or no reference point is set,
  *'if_point_is_visible'* is equal to *'true'*.

  List of values:
   *'true'*, *'false'*,
  *'if_point_is_visible'*.

  Default:
   *'true'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Scene3D`** (input_control)  scene_3d `→`  (handle)

Handle of the 3D scene.

**`LabelIndex`** (input_control)  integer(-array) `→`  (integer)

Index of the text label.

**`GenParamName`** (input_control)  string `→`  (string)

Names of the generic parameters.

Default:
'color'

List of values:
'color', 'disp_background', 'disp_connecting_line', 'font', 'position', 'reference_point', 'relates_to', 'text', 'text_color', 'visible'

**`GenParamValue`** (input_control)  string-array `→`  (string / integer / real)

Values of the generic parameters.

Default:
'red'

List of values:
'blue', 'bottom', 'bottom_left', 'bottom_right', 'center', 'green', 'left', 'point', 'red', 'right', 'top', 'top_left', 'top_right', 'window'

## Result

`set_scene_3d_label_param` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`add_scene_3d_label`

## Module

3D Metrology
