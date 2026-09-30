# GetWindowAttr (Operator)

## Name

`GetWindowAttr` — Get window characteristics.

## Signature

`static void HOperatorSet.GetWindowAttr(HTuple attributeName, out HTuple attributeValue)`

`static HTuple HSystem.GetWindowAttr(string attributeName)`

## Description

The operator `GetWindowAttr` can be used to read
characteristics of graphics windows that were set using
[`SetWindowAttr`](set_window_attr.md). The following parameters of a window may
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

**`attributeName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the attribute that should be returned.

List of values:
"background_color", "border_color", "border_width", "window_title"

**`attributeValue`** (output_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Attribute value.

## Result

If the parameters are correct `GetWindowAttr` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`OpenWindow`,
`SetDraw`,
`SetColor`,
`SetColored`,
`SetLineWidth`

## See also

`OpenWindow`,
`SetWindowAttr`

## Module

Foundation
