# read_string (Operator)

## Name

`read_string` — Read a string in a text window.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`def read_string(window_handle: HHandle, in_string: str, length: int) -> str`

## Description

`read_string` reads a string with a predetermined maximum length
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
is set to *"locale"* with [`set_system`](set_system.md), the length is stated in
number of bytes.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`in_string`** (input_control)  string `→` str

Default string (visible before input).

Default:
""

**`length`** (input_control)  integer `→` int

Maximum number of characters.

Default:
32

Restriction:
`Length > 0 && Length <= 1024`

**`out_string`** (output_control)  string `→` str

Read string.

## Result

`read_string` returns 2 (
H_MSG_TRUE)
if the text window is valid and a
string of maximal length fits within the right window boundary.
Otherwise an exception is raised.

## Possible Predecessors

`open_window`,
`set_font`

## Alternatives

`read_char`,
`fread_string`,
`fread_char`

## See also

`set_tposition`,
`new_line`,
`open_window`,
`set_font`,
`set_color`

## Module

Foundation
