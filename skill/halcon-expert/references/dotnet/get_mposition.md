# GetMposition (Operator)

## Name

`GetMposition` — Query the mouse position.

## Signature

`static void HOperatorSet.GetMposition(HTuple windowHandle, out HTuple row, out HTuple column, out HTuple button)`

`void HWindow.GetMposition(out int row, out int column, out int button)`

## Description

`GetMposition` returns the pixel accurate image coordinates of the
mouse pointer in the output window and the mouse button pressed.
These values are returned regardless of the state of the mouse
buttons (pressed or not pressed). If at least one mouse button is pressed,
the state of the modifier keys is returned as well. If no mouse button is
pressed, `GetMposition` returns 0 in *`button`*, even if
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

The origin of the coordinate system is located in the left upper
corner of the window. For graphics windows the coordinates *`row`*
and *`column`* are expressed with consideration of the current
image part (see [`SetPart`](set_part.md)).

If subpixel accurate image coordinates are required, you can use the
operator [`GetMpositionSubPix`](get_mposition_sub_pix.md).

## Attention

`GetMposition` fails (returns 5 (
H_MSG_FAIL)
) if the mouse pointer
is not located within the window. In this case, no values
are returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row`** (output_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Row coordinate of the mouse cursor in the image coordinate
system.

**`column`** (output_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

Column coordinate of the mouse cursor in the image coordinate
system.

**`button`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Mouse button(s) pressed or 0.

## Result

`GetMposition` returns the value 2 (
H_MSG_TRUE)
.
If the mouse pointer is not located within the
window, 5 (
H_MSG_FAIL)
is returned.

## Possible Predecessors

`OpenWindow`

## Alternatives

`GetMbutton`,
`GetMpositionSubPix`,
`GetMbuttonSubPix`

## See also

`OpenWindow`

## Module

Foundation
