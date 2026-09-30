# new_line (Operator)

## Name

`new_line` — Set the position of the text cursor to the beginning of the next line.

## Signature

`new_line( : : WindowHandle : )`

## Description

`new_line` sets the position of the text cursor to the beginning
of the next line. The new position depends on the current font. The left end
of the baseline for writing the following text string (not considering
descenders) is placed on this position.

If the next line does not fit into the window the content of the window is
scrolled by the height of one line in the upper direction. In order to
reach the correct new cursor position the font used in the next line must
be set before `new_line` is called. The position is changed by the output or input of text
([`write_string`](write_string.md), [`read_string`](read_string.md))
or by an explicit change of position by ([`set_tposition`](set_tposition.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

## Result

`new_line` returns 2 (
H_MSG_TRUE)
if the window is valid. Otherwise
an exception is raised.

## Possible Predecessors

`open_window`,
`set_font`,
`write_string`

## Alternatives

`get_tposition`,
`get_string_extents`,
`set_tposition`

## See also

`write_string`,
`set_font`

## Module

Foundation
