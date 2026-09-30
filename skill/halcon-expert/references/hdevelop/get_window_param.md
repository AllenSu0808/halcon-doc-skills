# get_window_param (Operator)

## Name

`get_window_param` — Get window parameters.

## Signature

`get_window_param( : : WindowHandle, Param : Value)`

## Description

The operator `get_window_param` allows querying different parameters
of an open window. For detailed descriptions of the individual parameters
see [`set_window_param`](set_window_param.md).

General window parameters:

- ***'flush'*** —

  *'true'* if automatic flushing is enabled, *'false'*
  otherwise.
- ***'region_quality'*** —

  Quality of the rendering of regions.
- ***'background_color'*** —

  The background color of the window *`WindowHandle`*.
- ***'window_title'*** —

  The text in the title bar of the window *`WindowHandle`*.
- ***'anti_aliasing'*** —

  *'true'* if anti aliasing is enabled, *'false'*
  otherwise.
- ***'graphics_stack'*** —

  *'true'* if the graphics stack is enabled, *'false'*
  otherwise.
- ***'graphics_stack_max_element_num'*** —

  Maximum number of elements in the graphics stack.
- ***'graphics_stack_max_memory_size'*** —

  Maximum memory consumption of the graphics stack.
- ***'pixel_grid_enable'*** —

  *'true'* if the pixel grid is enabled for the window
  *`WindowHandle`*.
- ***'pixel_grid_min_resolution'*** —

  Minimal required resolution of one pixel in the window
  *`WindowHandle`* such that the pixel grid becomes visible.
- ***'pixel_grid_color'*** —

  Color of the pixel grid lines.
- ***'pixel_grid_line_width'*** —

  Line width of the pixel grid lines.

Parameters concerning the *'3d_plot'*:

- ***'angle_of_view'*** —

  The angle of view of the virtual camera used to display the 3D plot.
- ***'axis_captions'*** —

  The captions for row, column, and height axis.
- ***'plot_quality'*** —

  The quality of the 3D plot.
- ***'scale_plot'*** —

  *'true'* if the height values of an image are transformed into
  the interval [0,255] before display, *'false'* otherwise.
- ***'display_grid'*** —

  *'true'* if the grid is displayed.
- ***'display_axes'*** —

  *'true'* if the coordinate axes are displayed.

## Attention

The parameters *'anti_aliasing'*, *'flush'*,
*'graphics_stack'*, *'graphics_stack_max_element_num'*,
*'graphics_stack_max_memory_size'*, and *'region_quality'*
depend on the library libcanvas, which might not be available on embedded
systems.

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
'angle_of_view', 'axis_captions', 'background_color', 'display_axes', 'display_grid', 'flush', 'graphics_stack', 'graphics_stack_max_element_num', 'graphics_stack_max_memory_size', 'pixel_grid_color', 'pixel_grid_enable', 'pixel_grid_line_width', 'pixel_grid_min_resolution', 'plot_quality', 'region_quality', 'scale_plot', 'window_title'

**`Value`** (output_control)  string(-array) `→`  (string / real / integer)

Value of the parameter.

## Possible Predecessors

`open_window`

## Possible Successors

`set_window_param`

## See also

`get_window_attr`,
`get_part_style`

## Module

Foundation
