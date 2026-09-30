# QueryFont (Operator)

## Name

`QueryFont` — Query the available fonts.

## Signature

`static void HOperatorSet.QueryFont(HTuple windowHandle, out HTuple font)`

`HTuple HWindow.QueryFont()`

## Description

`QueryFont` queries the fonts available for text output in the
output window. They can be set with the operator [`SetFont`](set_font.md) using the
appropriate syntax. Fonts are used by the operators [`WriteString`](write_string.md),
[`ReadChar`](read_char.md), [`ReadString`](read_string.md) and [`NewLine`](new_line.md).

## Attention

For different machines the available fonts may differ a lot. Therefore
`QueryFont` will return different fonts on different machines.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`font`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Tuple with available font names.

## Example (HDevelop)

```
open_window(0,0,-1,-1,'root','visible','',WindowHandle)
set_check('~text')
query_font(WindowHandle,Fontlist)
set_color(WindowHandle,'white')
for i:=0 to |Fontlist|-1 by 1
  set_display_font (WindowHandle,16,Fontlist[i],'true','false')
  write_string(WindowHandle,Fontlist[i])
  new_line(WindowHandle)
endfor
```

## Result

`QueryFont` returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`OpenWindow`

## Possible Successors

`SetFont`,
`WriteString`,
`ReadString`,
`ReadChar`

## See also

`SetFont`,
`WriteString`,
`ReadString`,
`ReadChar`,
`NewLine`

## Module

Foundation
