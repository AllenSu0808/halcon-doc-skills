# set_window_type (Operator)

## Name

`set_window_type` — Specify a window type.

## Signature

`def set_window_type(window_type: str) -> None`

## Description

`set_window_type` determines on which type of output device the
output is going to be displayed.
This specification is going to be used by the operator [`open_window`](open_window.md)
while opening the windows. You may open different windows on different types
of output devices. Therefore you have to specify the wanted type before
opening. You may request the available types of output devices by calling
the operator [`query_window_type`](query_window_type.md).
Possible values are:

- ***"X-Window"*** —

  X-Window Version 11.
- ***"WIN32-Window"*** —

  Microsoft Windows.
- ***"pixmap"*** —

  Windows are not displayed, but managed in memory only.
  In this manner you may port HALCON programs to computers without
  graphical display.
- ***"PostScript"*** —

  Objects are output to a PostScript File.
- ***"system_default"*** —

  Default for current platform.

A useful usage of `set_window_type` could be the development of
machine independent programs.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_type`** (input_control)  string `→` str

Name of the window type which has to be set.

Default:
"X-Window"

List of values:
"PostScript", "WIN32-Window", "X-Window", "pixmap", "system_default"

## Result

If the type of the output device is available, then
`set_window_type` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`

## See also

`open_window`,
`query_window_type`,
`get_window_type`

## Module

Foundation
