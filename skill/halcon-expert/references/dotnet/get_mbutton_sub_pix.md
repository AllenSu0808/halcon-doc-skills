# GetMbuttonSubPix (Operator)

## Name

`GetMbuttonSubPix` — Wait until a mouse button is pressed and get the subpixel mouse position.

## Signature

`static void HOperatorSet.GetMbuttonSubPix(HTuple windowHandle, out HTuple row, out HTuple column, out HTuple button)`

`void HWindow.GetMbuttonSubPix(out double row, out double column, out int button)`

## Description

`GetMbuttonSubPix` returns the subpixel accurate image coordinates
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
(see [`SetPart`](set_part.md)).

If only pixel accurate image coordinates are required, you can use the
operator [`GetMbutton`](get_mbutton.md).

## Attention

`GetMbuttonSubPix` only returns if a mouse button is pressed in
the window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row`** (output_control)  point.y `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the mouse cursor in the image coordinate
system.

**`column`** (output_control)  point.x `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the mouse cursor in the image coordinate
system.

**`button`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Mouse button(s) pressed.

## Result

`GetMbuttonSubPix` returns the value 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`OpenWindow`

## Alternatives

`GetMbutton`,
`GetMposition`,
`GetMpositionSubPix`

## See also

`OpenWindow`

## Module

Foundation
