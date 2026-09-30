# get_mbutton (Operator)

## Name

`get_mbutton` — Wait until a mouse button is pressed.

## Signature

`get_mbutton( : : WindowHandle : Row, Column, Button)`

## Description

`get_mbutton` returns the pixel accurate image coordinates of the
mouse pointer in the output window and the mouse button pressed.
In addition the state of the modifier keys is returned. The following
values are assigned to the individual buttons and keys:

- **1:** —

  Left button,
- **2:** —

  Middle button,
- **4:** —

  Right button,
- **8:** —

  Shift key,
- **16:** —

  Ctrl key,
- **32:** —

  Alt key.

The sum of the values for all pressed keys added to the value of the
pressed mouse button is returned in *`Button`*.

The operator waits until a mouse button is pressed in the output
window. For graphics windows the coordinates *`Row`* and
*`Column`* are expressed with consideration of the current
image part (see [`set_part`](set_part.md)).

If subpixel accurate image coordinates are required, you can use the
operator [`get_mbutton_sub_pix`](get_mbutton_sub_pix.md).

## Attention

`get_mbutton` only returns if a mouse button is pressed in
the window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row`** (output_control)  point.y `→`  (integer)

Row coordinate of the mouse cursor in the image coordinate
system.

**`Column`** (output_control)  point.x `→`  (integer)

Column coordinate of the mouse cursor in the image coordinate
system.

**`Button`** (output_control)  integer `→`  (integer)

Mouse button(s) pressed.

## Result

`get_mbutton` returns the value 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`open_window`

## Alternatives

`get_mposition`,
`get_mbutton_sub_pix`,
`get_mposition_sub_pix`

## See also

`open_window`

## Module

Foundation
