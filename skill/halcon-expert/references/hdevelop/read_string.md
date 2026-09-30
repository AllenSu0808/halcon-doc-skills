# read_string (Operator)

## Name

`read_string` — Read a string in a text window.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`read_string( : : WindowHandle, InString, Length : OutString)`

## Description

`read_string` reads a string with a predetermined maximum length
(*`Length`*) from the keyboard in the input window (= output
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

The length is stated as number of characters. If *'filename_encoding'*
is set to *'locale'* with [`set_system`](set_system.md), the length is stated in
number of bytes.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`InString`** (input_control)  string `→`  (string)

Default string (visible before input).

Default:
''

**`Length`** (input_control)  integer `→`  (integer)

Maximum number of characters.

Default:
32

Restriction:
`Length > 0 && Length <= 1024`

**`OutString`** (output_control)  string `→`  (string)

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
