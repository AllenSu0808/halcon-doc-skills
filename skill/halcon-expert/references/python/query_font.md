# query_font (Operator)

## Name

`query_font` — Query the available fonts.

## Signature

`def query_font(window_handle: HHandle) -> Sequence[str]`

## Description

`query_font` queries the fonts available for text output in the
output window. They can be set with the operator [`set_font`](set_font.md) using the
appropriate syntax. Fonts are used by the operators [`write_string`](write_string.md),
[`read_char`](read_char.md), [`read_string`](read_string.md) and [`new_line`](new_line.md).

## Attention

For different machines the available fonts may differ a lot. Therefore
`query_font` will return different fonts on different machines.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`font`** (output_control)  string-array `→` Sequence[str]

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

`query_font` returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`open_window`

## Possible Successors

`set_font`,
`write_string`,
`read_string`,
`read_char`

## See also

`set_font`,
`write_string`,
`read_string`,
`read_char`,
`new_line`

## Module

Foundation
