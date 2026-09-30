# GetWindowParam (Operator)

## Name

`GetWindowParam` — Get window parameters.

## Signature

`static void HOperatorSet.GetWindowParam(HTuple windowHandle, HTuple param, out HTuple value)`

`HTuple HWindow.GetWindowParam(string param)`

## Description

The operator `GetWindowParam` allows querying different parameters
of an open window. For detailed descriptions of the individual parameters
see [`SetWindowParam`](set_window_param.md).

General window parameters:

- ***"flush"*** —

  *"true"* if automatic flushing is enabled, *"false"*
  otherwise.
- ***"region_quality"*** —

  Quality of the rendering of regions.
- ***"background_color"*** —

  The background color of the window *`windowHandle`*.
- ***"window_title"*** —

  The text in the title bar of the window *`windowHandle`*.
- ***"anti_aliasing"*** —

  *"true"* if anti aliasing is enabled, *"false"*
  otherwise.
- ***"graphics_stack"*** —

  *"true"* if the graphics stack is enabled, *"false"*
  otherwise.
- ***"graphics_stack_max_element_num"*** —

  Maximum number of elements in the graphics stack.
- ***"graphics_stack_max_memory_size"*** —

  Maximum memory consumption of the graphics stack.
- ***"pixel_grid_enable"*** —

  *"true"* if the pixel grid is enabled for the window
  *`windowHandle`*.
- ***"pixel_grid_min_resolution"*** —

  Minimal required resolution of one pixel in the window
  *`windowHandle`* such that the pixel grid becomes visible.
- ***"pixel_grid_color"*** —

  Color of the pixel grid lines.
- ***"pixel_grid_line_width"*** —

  Line width of the pixel grid lines.

Parameters concerning the *"3d_plot"*:

- ***"angle_of_view"*** —

  The angle of view of the virtual camera used to display the 3D plot.
- ***"axis_captions"*** —

  The captions for row, column, and height axis.
- ***"plot_quality"*** —

  The quality of the 3D plot.
- ***"scale_plot"*** —

  *"true"* if the height values of an image are transformed into
  the interval [0,255] before display, *"false"* otherwise.
- ***"display_grid"*** —

  *"true"* if the grid is displayed.
- ***"display_axes"*** —

  *"true"* if the coordinate axes are displayed.

## Attention

The parameters *"anti_aliasing"*, *"flush"*,
*"graphics_stack"*, *"graphics_stack_max_element_num"*,
*"graphics_stack_max_memory_size"*, and *"region_quality"*
depend on the library libcanvas, which might not be available on embedded
systems.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`param`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the parameter.

Default:
"flush"

List of values:
"angle_of_view", "axis_captions", "background_color", "display_axes", "display_grid", "flush", "graphics_stack", "graphics_stack_max_element_num", "graphics_stack_max_memory_size", "pixel_grid_color", "pixel_grid_enable", "pixel_grid_line_width", "pixel_grid_min_resolution", "plot_quality", "region_quality", "scale_plot", "window_title"

**`value`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long)

Value of the parameter.

## Possible Predecessors

`OpenWindow`

## Possible Successors

`SetWindowParam`

## See also

`GetWindowAttr`,
`GetPartStyle`

## Module

Foundation
