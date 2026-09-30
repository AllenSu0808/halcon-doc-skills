# get_window_type (Operator)

## Name

`get_window_type` — Get the window type.

## Signature

`def get_window_type(window_handle: HHandle) -> str`

## Description

`get_window_type` determines the type or the graphical software,
respectively, of the output device for the window.
You may query the available types of output devices with the operator
[`query_window_type`](query_window_type.md).
A reasonable use for `get_window_type` might be in the field of the
development of machine independent software.
Possible values are:

- ***"X-Window"*** —

  X-Window Version 11.
- ***"WIN32-Window"*** —

  Microsoft Windows.
- ***"pixmap"*** —

  Windows are not shown, but managed in memory. By this means
  HALCON programs can be ported on computers without a graphical display.
  Note that windows of this type support only HALCON objects (images,
  regions and XLDs). Fonts, for example, are not available.
- ***"PostScript"*** —

  Objects are output to a PostScript File.
- ***"default"*** —

  Current window type.
- ***"system_default"*** —

  Default window type for current platform.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

Suggested values:
"default", "system_default"

**`window_type`** (output_control)  string `→` str

Window type

## Result

If the window is valid `get_window_type`
returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`

## See also

`query_window_type`,
`set_window_type`,
`get_window_pointer3`,
`open_window`

## Module

Foundation
