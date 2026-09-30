# get_tposition (Operator)

## Name

`get_tposition` — Get cursor position.

## Signature

`def get_tposition(window_handle: HHandle) -> Tuple[int, int]`

## Description

`get_tposition` queries the current position of the text
cursor in the output window. The position is measured in the image
coordinate system. The next output of text in this window starts at
the cursor position. The left end of the baseline for writing the
next string (not considering descenders) is placed on this
position. The position is changed by the output or input of text
([`write_string`](write_string.md), [`read_string`](read_string.md)) or by an explicit change
of position by ([`set_tposition`](set_tposition.md), [`new_line`](new_line.md)).

## Attention

If the output text does not fit completely into the window, an exception is
raised. This can be avoided by
`set_check('~text')`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`row`** (output_control)  point.y `→` int

Row index of text cursor position.

**`column`** (output_control)  point.x `→` int

Column index of text cursor position.

## Result

`get_tposition` returns 2 (
H_MSG_TRUE)
if the window is valid. Otherwise
an exception is raised.

## Possible Predecessors

`open_window`,
`set_font`

## Possible Successors

`set_tposition`,
`write_string`,
`read_string`,
`read_char`

## See also

`new_line`,
`read_string`,
`set_tposition`,
`write_string`,
`set_check`

## Module

Foundation
