# set_window_param (Operator)

## Name

`set_window_param` — Set window parameters.

## Signature

`set_window_param( : : WindowHandle, Param, Value : )`

## Description

The operator `set_window_param` allows setting different parameters
of an open window.

General window parameters:

- ***'flush'*** —

  Enables or disables flushing the contents of the window after the display
  of every object. If *'flush'* is set to *'false'*,
  [`flush_buffer`](flush_buffer.md) must be called to update the contents of the window.
  If you want to interact with the content of the graphics window
  (e.g., zoom or move the content), you have to set *'flush'* to
  *'true'*.

  List of values:
   *'true'*, *'false'*.

  Default:
   *'true'*.
- ***'region_quality'*** —

  Influences the quality of the rendering of region objects. Especially if
  the region to display has to be scaled down for visualization,
  *'good'* produces a more accurate and pleasing impression.
  *'low'* is a bit inaccurate in these cases but significantly
  faster. If only the border of the region is displayed
  (see [`set_draw`](set_draw.md)), the fractional part of the line width
  (see [`set_line_width`](set_line_width.md)) is ignored.

  List of values:
   *'low'*, *'good'*.

  Default:
   *'low'*.
- ***'background_color'*** —

  Sets the background color of the window *`WindowHandle`*. The
  operator [`clear_window`](clear_window.md) uses this color to clear the window.

  Suggested values:
   a string containing the color name
  (e.g., *'black'*, *'red'*).
- ***'window_title'*** —

  Allows changing the text in the title bar of an already opened HALCON
  window.

  Note that you cannot set *'window_title'* for buffer windows.
  This restriction also applies to HDevelop windows, that is windows opened
  via `dev_open_window`, which are in fact buffer windows.

  Value range:
   a string containing up to 1023 characters.
- ***'anti_aliasing'*** —

  Enables or disables the anti aliasing of contours and regions.

  List of values:
   *'true'*, *'false'*.

  Default:
   *'true'*.
- ***'graphics_stack'*** —

  Enables or disables the graphics stack of a window. With
  activated graphics stack changing the window part with [`set_part`](set_part.md)
  triggers the display of previously displayed objects with respect to
  the new part. With this it is possible to move or scale the contents of
  the window. This parameter has no effect on the graphics stack of a
  HDevelop graphics window.

  List of values:
   *'true'*, *'false'*.

  Default:
   *'false'*.
- ***'graphics_stack_max_element_num'*** —

  Maximum number of elements in the graphics stack. This number corresponds
  to the number of display operations recorded. This parameter has no effect
  on the graphics stack of a
  HDevelop graphics window and is effective not before the next call to a
  display operator.

  Suggested values:
   positive number or *'unlimited'*.

  Default:
   *50*.
- ***'graphics_stack_max_memory_size'*** —

  Limits the memory consumption of the graphics stack. If this limit is
  exceeded, older display operations are removed from the graphics stack.
  This parameter has no effect on the graphics stack of a HDevelop
  graphics window and is effective not before the next call to a
  display operator.

  Suggested values:
   memory limit in bytes or *'unlimited'*.

  Default:
   *'unlimited'*.
- ***'pixel_grid_enable'*** —

  Enables or disables the pixel grid. If the pixel grid is activated, a grid
  is drawn around the displayed pixels as soon as the image part is enlarged
  sufficiently (see *'pixel_grid_min_resolution'*). This
  parameter is effective as soon as the window content is updated.

  List of values:
   *'true'*, *'false'*.

  Default:
   *'false'*.

  Restriction:
   Has no effect, when the HDevelop option
  `Pixel Grid` is enabled.
- ***'pixel_grid_min_resolution'*** —

  Specifies the minimum required resolution of an image pixel in the
  graphics window which is necessary for the pixel grid to be drawn. This
  parameter has an effect only if *'pixel_grid_enable'* has been set
  to *'true'*. Assuming this value is set to *20*, the pixel
  grid will be visible as soon as a pixel in the displayed image part
  takes up at least *20* x *20* pixels in the graphics window.
  Furthermore, this parameter is effective as soon as the window content is
  updated.

  Suggested values:
   Positive integer.

  Default:
   *20*.
- ***'pixel_grid_color'*** —

  Specifies the color of the lines of the pixel grid. This parameter has an
  effect only if *'pixel_grid_enable'* has been set to
  *'true'*. Furthermore, this parameter is effective as soon as the
  window content is updated.

  Suggested values:
   Color value, see [`set_color`](set_color.md) for an
  overview.

  Default:
   *'#696969c0'*.

  Restriction:
   Has no effect, when the HDevelop option
  `Pixel Grid` is enabled.
- ***'pixel_grid_line_width'*** —

  Specifies the line width in pixels that is used to display the lines of
  the pixel grid. This parameter has an effect only if
  *'pixel_grid_enable'* has been set to *'true'*. Furthermore,
  this parameter is effective as soon as the window content is updated.

  Value range:
   [*1.0*, *2000.0*].

  Default:
   *1.0*.

Parameters concerning the *'3d_plot'* (see [`set_paint`](set_paint.md)):

- ***'angle_of_view'*** —

  Set the angle of view of the virtual camera used to display the 3D plot.
  The angle must be provided in radians and lie within the interval
  [0,PI). An angle of 0 radians implies orthogonal projection. Another
  way to choose orthogonal projection is to set *'angle_of_view'*
  to *'orthogonal'*.

  Suggested values:
   *'orthogonal'* or an angle in radians.

  Default:
   *1.22173* (70 degrees).
- ***'axis_captions'*** —

  The axis captions for row, column, and height can be set by passing a
  tuple containing the strings for the captions in the specified order row,
  column, and height axis, (e.g., ['row','col','height']). Pass empty strings
  to display no captions at all.

  Value range:
   A tuple containing three strings. Each string can
  contain up to 31 characters.

  Default:
   *[' ',' ',' ']*.
- ***'caption_color'*** —

  The color of the axis captions for row, column, and height. You can
  either pass one color for all three axes or a tuple of three colors
  to set individual colors for each axis.

  Suggested values:
   a string or tuple with three strings containing the
  color name (e.g., *'black'*, *'red'*).

  Default:
   *'black'*.
- ***'plot_quality'*** —

  Influences the quality of the 3D plot. Depending on the capabilities of
  your graphics card better settings for the quality may reduce the
  frame rate of the 3D plot significantly.

  List of values:
   *'low'*, *'medium'*,
  *'good'*, *'best'*.

  Default:
   *'medium'*.
- ***'scale_plot'*** —

  If set to *'true'* the height values of an image are transformed into
  the interval [0,255] before display. If set to 'false' the aspect ratio
  between row/column and height is considered. Images of the type byte,
  cyclic, or direction are not scaled, i.e. in their cases this parameter is
  ignored.

  List of values:
   *'true'*, *'false'*.

  Default:
   *'true'*.
- ***'display_grid'*** —

  If set to *'true'* a grid is displayed at height 0.

  List of values:
   *'true'*, *'false'*.

  Default:
   *'true'*.
- ***'display_axes'*** —

  If set to *'true'* coordinate axes are displayed.
  List of values:
   *'true'*, *'false'*.

  Default:
   *'true'*.

## Attention

The parameters *'anti_aliasing'*, *'flush'*,
*'graphics_stack'*, *'graphics_stack_max_element_num'*,
*'graphics_stack_max_memory_size'*, and *'region_quality'*
depend on the library libcanvas, which might not be available on embedded
systems.

The parameter *'window_title'* cannot be set for buffer windows.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Param`** (input_control)  string `→`  (string)

Name of the parameter.

Default:
'flush'

List of values:
'angle_of_view', 'anti_aliasing', 'axis_captions', 'background_color', 'caption_color', 'display_axes', 'display_grid', 'flush', 'graphics_stack', 'graphics_stack_max_element_num', 'graphics_stack_max_memory_size', 'pixel_grid_color', 'pixel_grid_enable', 'pixel_grid_line_width', 'pixel_grid_min_resolution', 'plot_quality', 'region_quality', 'scale_plot', 'window_title'

**`Value`** (input_control)  string(-array) `→`  (string / real / integer)

Value to be set.

Default:
'false'

List of values:
'best', 'black', 'blue', 'false', 'good', 'green', 'low', 'medium', 'orthogonal', 'red', 'true', 'unlimited', 'white'

## Possible Predecessors

`open_window`

## Possible Successors

`disp_image`

## See also

`get_window_param`,
`set_window_attr`,
`set_part_style`

## Module

Foundation
