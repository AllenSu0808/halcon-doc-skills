# ReadChar (Operator)

## Name

`ReadChar` — Read a character from a window.

## Signature

`static void HOperatorSet.ReadChar(HTuple windowHandle, out HTuple charVal, out HTuple code)`

`string HWindow.ReadChar(out string code)`

## Description

`ReadChar` reads a character from the keyboard in the
input window (= output window). If the character is printable it is returned
in *`charVal`*. If a control key has been pressed, this will be indicated
by the value of *`code`*. Some important keys are recognizable by
this value. Possible values are:

- **'character':** —

  printable character
- **'left':** —

  cursor left
- **'right':** —

  cursor right
- **'up':** —

  cursor up
- **'down':** —

  cursor down
- **'insert':** —

  insert
- **'none':** —

  none of these keys
- **'canceled':** —

  `ReadChar` has been canceled (not always possible,
  e.g., in native X11 windows)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`charVal`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Input character (if it is not a control character).

**`code`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Code for input character.

## Result

`ReadChar` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Predecessors

`OpenWindow`,
`SetFont`

## Alternatives

`ReadString`,
`FreadChar`,
`FreadString`

## See also

`WriteString`,
`SetFont`

## Module

Foundation
