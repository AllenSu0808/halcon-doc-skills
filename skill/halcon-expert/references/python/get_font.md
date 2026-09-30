# get_font (Operator)

## Name

`get_font` — Get the current font.

## Signature

`def get_font(window_handle: HHandle) -> str`

## Description

`get_font` queries the name of the font used in the
output window *`window_handle`*. The font is used by the operators
[`write_string`](write_string.md), [`read_string`](read_string.md) etc. The font is
set by the operator [`set_font`](set_font.md). Text windows as well as
windows for image display use fonts. Both types of windows have a
default font that can be modified with
`set_system('default_font',Font)` prior to opening
the window. A list of all available fonts can be obtained using
[`query_font`](query_font.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`font`** (output_control)  string `→` str

Name of the current font.

## Result

`get_font` returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`open_window`,
`query_font`

## Possible Successors

`set_font`

## See also

`set_font`,
`query_font`,
`open_window`,
`set_system`

## Module

Foundation
