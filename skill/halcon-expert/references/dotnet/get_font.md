# GetFont (Operator)

## Name

`GetFont` — Get the current font.

## Signature

`static void HOperatorSet.GetFont(HTuple windowHandle, out HTuple font)`

`string HWindow.GetFont()`

## Description

`GetFont` queries the name of the font used in the
output window *`windowHandle`*. The font is used by the operators
[`WriteString`](write_string.md), [`ReadString`](read_string.md) etc. The font is
set by the operator [`SetFont`](set_font.md). Text windows as well as
windows for image display use fonts. Both types of windows have a
default font that can be modified with
`set_system('default_font',Font)` prior to opening
the window. A list of all available fonts can be obtained using
[`QueryFont`](query_font.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`font`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the current font.

## Example (HDevelop)

```
get_font(WindowHandle,CurrentFont)
set_font(WindowHandle,MyFont)
write_string(WindowHandle,['The name of my Font is:',Myfont])
new_line(WindowHandle)
set_font(WindowHandle,CurrentFont)
```

## Result

`GetFont` returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`OpenWindow`,
`QueryFont`

## Possible Successors

`SetFont`

## See also

`SetFont`,
`QueryFont`,
`OpenWindow`,
`SetSystem`

## Module

Foundation
