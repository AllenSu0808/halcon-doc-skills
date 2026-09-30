# set_window_attr (Operator)

## Name

`set_window_attr` — Set window characteristics.

## Signature

`set_window_attr( : : AttributeName, AttributeValue : )`

## Description

You may use `set_window_attr` to set specific characteristics
of graphics windows. With it you may modify the following default
parameters of a window:

- **'border_width'** —

  Width of the window border in pixels.
  Is not implemented under Windows.
- **'border_color'** —

  Color of the window border.
  Is not implemented under Windows.
- **'background_color'** —

  Background color of the window.
- **'window_title'** —

  Name of the window in the title bar.

## Attention

You have to call `set_window_attr` *before*
calling [`open_window`](open_window.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`AttributeName`** (input_control)  string `→`  (string)

Name of the attribute that should be modified.

List of values:
'background_color', 'border_color', 'border_width', 'window_title'

**`AttributeValue`** (input_control)  string `→`  (string / integer)

Value of the attribute that should be set.

List of values:
0, 1, 2, 'MyName', 'black', 'default', 'white'

## Result

If the parameters are correct `set_window_attr` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`,
`set_draw`,
`set_color`,
`set_colored`,
`set_line_width`

## See also

`open_window`,
`get_window_attr`,
`set_window_param`

## Module

Foundation
