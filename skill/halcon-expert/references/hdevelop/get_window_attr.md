# get_window_attr (Operator)

## Name

`get_window_attr` — Get window characteristics.

## Signature

`get_window_attr( : : AttributeName : AttributeValue)`

## Description

The operator `get_window_attr` can be used to read
characteristics of graphics windows that were set using
[`set_window_attr`](set_window_attr.md). The following parameters of a window may
be queried:

- **'border_width'** —

  Width of the window border in pixels.
- **'border_color'** —

  Color of the window border.
- **'background_color'** —

  Background color of the window.
- **'window_title'** —

  Name of the window in the title bar.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`AttributeName`** (input_control)  string `→`  (string)

Name of the attribute that should be returned.

List of values:
'background_color', 'border_color', 'border_width', 'window_title'

**`AttributeValue`** (output_control)  string `→`  (string / integer)

Attribute value.

## Result

If the parameters are correct `get_window_attr` returns 2 (
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
`set_window_attr`

## Module

Foundation
