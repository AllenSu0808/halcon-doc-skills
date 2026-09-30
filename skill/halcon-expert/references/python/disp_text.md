# disp_text (Operator)

## Name

`disp_text` — Display text in a window.

## Signature

`def disp_text(window_handle: HHandle, string: MaybeSequence[str], coord_system: str, row: MaybeSequence[Union[int, float, str]], column: MaybeSequence[Union[int, float, str]], color: MaybeSequence[str], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, int, float]]) -> None`

## Description

`disp_text` displays text in the graphics window *`window_handle`*
at the position (*`row`*,*`column`*).

If only a single position is defined, one text line is displayed for each
element of *`string`*. Also, *"\n"*
will be interpreted as a newline character, i.e., a line break is performed.

If multiple positions are defined, only a single string or one string for
each position is allowed in *`string`*. In this case, line breaks have
to be forced with *"\n"*.

Newlines (*"\n"*) at the end of
*`string`* are ignored.

The position of the text may be specified in window coordinates
(*`coord_system`* = *"window"*) or in image coordinates
(*`coord_system`* = *"image"*), which is useful when using
zoomed images.

In addition to supplying (*`row`*,*`column`*) coordinates, it is
also possible to pass predefined values to *`row`* and *`column`*
to display the text at a fixed Position in the window
(only if *`coord_system`* = *"window"*).:

|  |  |  |
| --- | --- | --- |
| *"top"*, *"left"* | *"top"*, *"center"* | *"top"*, *"right"* |
| *"center"*, *"left"* | *"center"*, *"center"* | *"center"*, *"right"* |
| *"bottom"*, *"left"* | *"bottom"*, *"center"* | *"bottom"*, *"right"* |

The parameter *`color`* also accepts tuples of values. In that case,
the specified colors are used cyclically for every new text position or
for every new text line if a single position is used.

**Generic Parameters**

`disp_text` may display the *`string`* within a box (default).
This behavior and the look of the box are defined with the generic parameters
in *`gen_param_name`* and *`gen_param_value`*.

- **'box'** —

  If *"box"* is set to *"true"*, the text is written within
  a box. The look of the box and its optional shadow can be configured
  with the generic parameters below.

  List of values:
   *"true"* and *"false"*

  Default:
   *"true"*
- **'box_color'** —

  Sets the color of the box.

  List of values:
   a string containing the color name (e.g., *"white"*,
  *"red"*, or *"#aa00bba0"*)

  Default:
   *"#fce9d4"* (which is a light orange)
- **'shadow'** —

  If *"shadow"* is set to *"true"*, an additional shadow
  is displayed beneath the box (if *"box"* is *"true"*).

  List of values:
   *"true"* and *"false"*

  Default:
   *"true"* if *"box_color"* is set to a color
  without alpha value, *"false"* otherwise
- **'shadow_color'** —

  Sets the color of the shadow if *"shadow"* is *"true"*.

  List of values:
   a string containing the color name (e.g., *"black"*,
  *"red"*, or *"#aa00bba0"*)

  Default:
   *"#f28d26"* (which is a darker orange) if
  *"box_color"* is not set, *"white"*
  otherwise
- **'border_radius'** —

  Controls the roundness of the box's corners. For sharp corners set it to
  *0*, for smoother corners to higher values.

  List of values:
   positive real numbers or *0*

  Default:
   2
- **'box_padding'** —

  Controls to which amount in pixels the box is extended around the text.

  List of values:
   positive real number

  Default:
   0
- **'shadow_sigma'** —

  Controls to which amount the shadow beneath the box is blurred. Set it to
  *0* for a sharp shadow.

  List of values:
   positive real number or *0*

  Default:
   1.5
- **'shadow_dx' and 'shadow_dy'** —

  Controls the offset of the shadow in column (*"shadow_dx"*) and
  row (*"shadow_dy"*) direction in pixels.

  List of values:
   any real number

  Default:
   2
- **'backdrop_blur_sigma'** —

  Controls to which amount the background of the box is blurred. s only an
  effect if *"box"* is *"true"* and *"box_color"* is not opaque
  (i.e. alpha is not 255). It is recommended to use
  *"backdrop_blur_sigma"* with *"shadow"* set to *"false"*.

  List of values:
   positive real number or *0*

  Default:
   0
- **'rotate_phi'** —

  Angle in degrees to rotate the displayed text.

  List of values:
   any real number

  Default:
   0
- **'rotate_col'** —

  Column coordinate of the rotation center if *"rotate_phi"* is different
  to zero. Choose either a column coordinate by setting a real number or determine
  the rotation center on the left edge (*"text_left"*), the right edge
  (*"text_right"*), or in the center (*"text_center"*) of the text box.

  List of values:
   any real number or *"text_left"*, *"text_center"*,
  *"text_right"*

  Default:
   *"text_center"*
- **'rotate_row'** —

  Row coordinate of the rotation center if *"rotate_phi"* is different
  to zero. Choose either a row coordinate by setting a real number or determine
  the rotation center on the top edge (*"text_top"*), the bottom edge
  (*"text_bottom"*), or in the center (*"text_center"*) of the text box.

  List of values:
   any real number or *"text_top"*, *"text_center"*,
  *"text_bottom"*

  Default:
   *"text_center"*
- **'border_color'** —

  Sets the color of the border of the text box.

  List of values:
   a string containing the color name (e.g., *"black"*,
  *"red"*, or *"#aa00bba0"*)

  Default:
   *"#ffffff"*
- **'border_width'** —

  Controls the width of the text box border.

  List of values:
   positive real numbers or *0*

  Default:
   0

## Attention

`disp_text` depends on the library libhcanvas, which might not be
available on embedded systems.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`string`** (input_control)  string(-array) `→` MaybeSequence[str]

A tuple of strings containing the text message to be
displayed.
Each value of the tuple will be displayed in a single line.

Default:
"hello"

**`coord_system`** (input_control)  string `→` str

If set to 'window', the text position is given with respect to
the window coordinate system. If set to 'image', image
coordinates are used (this may be useful in zoomed images).

Default:
"window"

List of values:
"image", "window"

**`row`** (input_control)  point.y(-array) `→` MaybeSequence[Union[int, float, str]]

The vertical text alignment or the row coordinate of the
desired text position.

Default:
12

List of values:
12, "bottom", "center", "top"

**`column`** (input_control)  point.x(-array) `→` MaybeSequence[Union[int, float, str]]

The horizontal text alignment or the column coordinate of
the desired text position.

Default:
12

List of values:
12, "center", "left", "right"

**`color`** (input_control)  string(-array) `→` MaybeSequence[str]

A tuple of strings defining the colors of the texts.

Default:
"black"

List of values:
"black", "blue", "coral", "cyan", "forest green", "green", "lime green", "magenta", "red", "slate blue", "yellow"

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Generic parameter names.

Default:
[]

List of values:
"backdrop_blur_sigma", "border_color", "border_radius", "border_width", "box", "box_color", "box_padding", "rotate_col", "rotate_phi", "rotate_row", "shadow", "shadow_color", "shadow_dx", "shadow_dy", "shadow_sigma"

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[str, int, float]]

Generic parameter values.

Default:
[]

List of values:
5.0, "black", "blue", "false", "forest green", "red", "true", "white"

## Example (HDevelop)

```
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
disp_text (WindowHandle, 'Display some text in a box', 'window', 12, 12, \
           'black', [], [])
```

## Possible Predecessors

`open_window`,
`set_font`,
`get_string_extents`

## Alternatives

`write_string`

## See also

`get_string_extents`,
`set_font`

## Module

Foundation
