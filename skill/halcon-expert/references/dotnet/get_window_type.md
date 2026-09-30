# GetWindowType (Operator)

## Name

`GetWindowType` — Get the window type.

## Signature

`static void HOperatorSet.GetWindowType(HTuple windowHandle, out HTuple windowType)`

`string HWindow.GetWindowType()`

## Description

`GetWindowType` determines the type or the graphical software,
respectively, of the output device for the window.
You may query the available types of output devices with the operator
[`QueryWindowType`](query_window_type.md).
A reasonable use for `GetWindowType` might be in the field of the
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

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr* / IntPtr)

Window handle.

Suggested values:
"default", "system_default"

**`windowType`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Window type

## Example (HDevelop)

```
open_window(100,100,200,200,'root','visible','',WindowHandle)
get_window_type(WindowHandle,WindowType)
fwrite_string(FileHandle, ['Window type: ',WindowType])
fnew_line(FileHandle)
```

## Result

If the window is valid `GetWindowType`
returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`OpenWindow`

## See also

`QueryWindowType`,
`SetWindowType`,
`GetWindowPointer3`,
`OpenWindow`

## Module

Foundation
