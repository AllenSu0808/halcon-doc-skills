# QueryColor (Operator)

## Name

`QueryColor` — Query all color names displayable in the window.

## Signature

`static void HOperatorSet.QueryColor(HTuple windowHandle, out HTuple colors)`

`HTuple HWindow.QueryColor()`

## Description

`QueryColor` returns the names of all colors that are
usable for region output ([`DispRegion`](disp_region.md),
[`DispPolygon`](disp_polygon.md), [`DispCircle`](disp_circle.md), etc.). On a b/w
screen `QueryColor` returns *"black"* and *"white"*.
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
`QueryColor`. The list of available colors (to HALCON )
must not be confused with the list of displayable colors. For
screens with true-color output the available colors are only a small
subset of the displayable colors. Colors that are not directly
available to HALCON can be chosen manually with [`SetRgb`](set_rgb.md)
or [`SetHsi`](set_hsi.md). If colors are chosen that are known to
HALCON but cannot be displayed, HALCON can choose a similar
color. To use this feature, `set_check(::'~color':)`
must be set.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`colors`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Color names.

## Example (HDevelop)

```
open_window(0,0,-1,-1,'root','invisible','',WindowHandle)
query_color(WindowHandle,Colors)
close_window(WindowHandle)
fwrite_string (FileHandle, ['Displayable colors: ',Colors])
```

## Result

`QueryColor` returns 2 (
H_MSG_TRUE)
, if the window is
valid. Otherwise an exception is raised.

## Possible Successors

`SetColor`,
`DispRegion`

## See also

`QueryAllColors`,
`SetColor`,
`DispRegion`,
`OpenWindow`

## Module

Foundation
