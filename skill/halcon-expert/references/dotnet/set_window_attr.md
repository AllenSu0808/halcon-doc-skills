# SetWindowAttr (Operator)

## Name

`SetWindowAttr` — Set window characteristics.

## Signature

`static void HOperatorSet.SetWindowAttr(HTuple attributeName, HTuple attributeValue)`

`static void HSystem.SetWindowAttr(string attributeName, HTuple attributeValue)`

`static void HSystem.SetWindowAttr(string attributeName, string attributeValue)`

## Description

You may use `SetWindowAttr` to set specific characteristics
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

You have to call `SetWindowAttr` *before*
calling [`OpenWindow`](open_window.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`attributeName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the attribute that should be modified.

List of values:
"background_color", "border_color", "border_width", "window_title"

**`attributeValue`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Value of the attribute that should be set.

List of values:
0, 1, 2, "MyName", "black", "default", "white"

## Result

If the parameters are correct `SetWindowAttr` returns 2 (
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
`GetWindowAttr`,
`SetWindowParam`

## Module

Foundation
