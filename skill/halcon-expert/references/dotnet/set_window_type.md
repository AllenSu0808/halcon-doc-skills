# SetWindowType (Operator)

## Name

`SetWindowType` — Specify a window type.

## Signature

`static void HOperatorSet.SetWindowType(HTuple windowType)`

`static void HSystem.SetWindowType(string windowType)`

## Description

`SetWindowType` determines on which type of output device the
output is going to be displayed.
This specification is going to be used by the operator [`OpenWindow`](open_window.md)
while opening the windows. You may open different windows on different types
of output devices. Therefore you have to specify the wanted type before
opening. You may request the available types of output devices by calling
the operator [`QueryWindowType`](query_window_type.md).
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

A useful usage of `SetWindowType` could be the development of
machine independent programs.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the window type which has to be set.

Default:
"X-Window"

List of values:
"PostScript", "WIN32-Window", "X-Window", "pixmap", "system_default"

## Result

If the type of the output device is available, then
`SetWindowType` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`OpenWindow`

## See also

`OpenWindow`,
`QueryWindowType`,
`GetWindowType`

## Module

Foundation
