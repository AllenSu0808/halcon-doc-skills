# query_color (Operator)

## Name

`query_color` — Query all color names displayable in the window.

## Signature

`def query_color(window_handle: HHandle) -> Sequence[str]`

## Description

`query_color` returns the names of all colors that are
usable for region output ([`disp_region`](disp_region.md),
[`disp_polygon`](disp_polygon.md), [`disp_circle`](disp_circle.md), etc.). On a b/w
screen `query_color` returns *"black"* and *"white"*.
These two “colors” are displayable on any screen.
In addition to *"black"* and *"white"* several gray values
(e.g., *"dim gray"*) are returned on
screens capable of gray values. A list of all displayable colors is
returned for screens with color lookup table. The returned tuple of
colors begins with b/w, followed by the three primaries
(*"red"*,*"green"*,*"blue"*) and several gray values.
`query_all_colors(::WindowHandle:Colors )` returns a list of all
available colors.
For screens with true-color output the same list is returned by
`query_color`. The list of available colors (to HALCON )
must not be confused with the list of displayable colors. For
screens with true-color output the available colors are only a small
subset of the displayable colors. Colors that are not directly
available to HALCON can be chosen manually with [`set_rgb`](set_rgb.md)
or [`set_hsi`](set_hsi.md). If colors are chosen that are known to
HALCON but cannot be displayed, HALCON can choose a similar
color. To use this feature, `set_check(::'~color':)`
must be set.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`colors`** (output_control)  string-array `→` Sequence[str]

Color names.

## Example (HDevelop)

```
open_window(0,0,-1,-1,'root','invisible','',WindowHandle)
query_color(WindowHandle,Colors)
close_window(WindowHandle)
fwrite_string (FileHandle, ['Displayable colors: ',Colors])
```

## Result

`query_color` returns 2 (
H_MSG_TRUE)
, if the window is
valid. Otherwise an exception is raised.

## Possible Successors

`set_color`,
`disp_region`

## See also

`query_all_colors`,
`set_color`,
`disp_region`,
`open_window`

## Module

Foundation
