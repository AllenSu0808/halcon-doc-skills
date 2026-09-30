# ReadString (Operator)

## Name

`ReadString` — Read a string in a text window.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`static void HOperatorSet.ReadString(HTuple windowHandle, HTuple inString, HTuple length, out HTuple outString)`

`string HWindow.ReadString(string inString, int length)`

## Description

`ReadString` reads a string with a predetermined maximum length
(*`length`*) from the keyboard in the input window (= output
window). The string is read from the current position of the text cursor
using the current font. The maximum length has to be small enough to keep the
string within the right window boundary. A default string which can be
edited or simply accepted by the user may be provided. After text input
the text cursor is positioned at the end of the edited string.
Commands for editing:

- **RETURN** —

  finish input
- **BACKSPACE** —

  delete the character on the left side of the cursor and
  move the cursor to this position.

The length is stated as number of characters. If *"filename_encoding"*
is set to *"locale"* with [`SetSystem`](set_system.md), the length is stated in
number of bytes.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`inString`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Default string (visible before input).

Default:
""

**`length`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum number of characters.

Default:
32

Restriction:
`Length > 0 && Length <= 1024`

**`outString`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Read string.

## Result

`ReadString` returns 2 (
H_MSG_TRUE)
if the text window is valid and a
string of maximal length fits within the right window boundary.
Otherwise an exception is raised.

## Possible Predecessors

`OpenWindow`,
`SetFont`

## Alternatives

`ReadChar`,
`FreadString`,
`FreadChar`

## See also

`SetTposition`,
`NewLine`,
`OpenWindow`,
`SetFont`,
`SetColor`

## Module

Foundation
