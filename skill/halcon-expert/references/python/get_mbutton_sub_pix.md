# get_mbutton_sub_pix (Operator)

## Name

`get_mbutton_sub_pix` — Wait until a mouse button is pressed and get the subpixel mouse position.

## Signature

`def get_mbutton_sub_pix(window_handle: HHandle) -> Tuple[float, float, int]`

## Description

`get_mbutton_sub_pix` returns the subpixel accurate image coordinates
of the mouse pointer in the output window and the mouse button pressed.
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
pressed mouse button is returned in *`button`*.

The operator waits until a button is pressed in the output
window. For graphics windows the coordinates *`row`* and
*`column`* are expressed with consideration of the current image part
(see [`set_part`](set_part.md)).

If only pixel accurate image coordinates are required, you can use the
operator [`get_mbutton`](get_mbutton.md).

## Attention

`get_mbutton_sub_pix` only returns if a mouse button is pressed in
the window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`row`** (output_control)  point.y `→` float

Row coordinate of the mouse cursor in the image coordinate
system.

**`column`** (output_control)  point.x `→` float

Column coordinate of the mouse cursor in the image coordinate
system.

**`button`** (output_control)  integer `→` int

Mouse button(s) pressed.

## Result

`get_mbutton_sub_pix` returns the value 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`open_window`

## Alternatives

`get_mbutton`,
`get_mposition`,
`get_mposition_sub_pix`

## See also

`open_window`

## Module

Foundation
