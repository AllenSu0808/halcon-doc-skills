# read_char (Operator)

## Name

`read_char` — Read a character from a window.

## Signature

`read_char( : : WindowHandle : Char, Code)`

## Description

`read_char` reads a character from the keyboard in the
input window (= output window). If the character is printable it is returned
in *`Char`*. If a control key has been pressed, this will be indicated
by the value of *`Code`*. Some important keys are recognizable by
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

  `read_char` has been canceled (not always possible,
  e.g., in native X11 windows)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Char`** (output_control)  string `→`  (string)

Input character (if it is not a control character).

**`Code`** (output_control)  string `→`  (string)

Code for input character.

## Result

`read_char` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Predecessors

`open_window`,
`set_font`

## Alternatives

`read_string`,
`fread_char`,
`fread_string`

## See also

`write_string`,
`set_font`

## Module

Foundation
