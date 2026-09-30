# get_mposition_sub_pix (Operator)

## Name

`get_mposition_sub_pix` — Query the subpixel mouse position.

## Signature

`def get_mposition_sub_pix(window_handle: HHandle) -> Tuple[float, float, int]`

## Description

`get_mposition_sub_pix` returns the subpixel accurate image
coordinates of the mouse pointer in the output window and the mouse button
pressed.
These values are returned regardless of the state of the mouse
buttons (pressed or not pressed). If at least one mouse button is pressed,
the state of the modifier keys is returned as well. If no mouse button is
pressed, [`get_mposition`](get_mposition.md) returns 0 in *`button`*, even if
a modifier key is pressed.
The following values are assigned to the individual buttons and keys:

- **0:** —

  No button,
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

The sum of the values for all pressed buttons/keys is returned in
*`button`*.

For graphics windows the coordinates *`row`* and *`column`*
are expressed with consideration of the current image part
(see [`set_part`](set_part.md)).

If only pixel accurate image coordinates are required, you can use the
operator [`get_mposition`](get_mposition.md).

## Attention

`get_mposition_sub_pix` fails (returns 5 (
H_MSG_FAIL)
) if the mouse pointer
is not located within the window. In this case, no values
are returned.

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

Mouse button(s) pressed or 0.

## Result

If the mouse pointer is not located within the
window, 5 (
H_MSG_FAIL)
is returned.

## Possible Predecessors

`open_window`

## Alternatives

`get_mbutton`,
`get_mposition`,
`get_mbutton_sub_pix`

## See also

`open_window`

## Module

Foundation
