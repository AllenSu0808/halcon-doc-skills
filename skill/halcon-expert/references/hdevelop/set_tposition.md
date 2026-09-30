# set_tposition (Operator)

## Name

`set_tposition` — Set the position of the text cursor.

## Signature

`set_tposition( : : WindowHandle, Row, Column : )`

## Description

`set_tposition` sets the position of the text cursor in the
output window. The reference position is the upper left corner of an
upper case character.

The position is measured in the image coordinate system. The
position of the text cursor can be marked, e.g., by an underscore.
The next text output in this window starts at the cursor position.
The left end of the baseline for writing the following text string
(not considering descenders) is placed on this position.

The position is changed by the output or input of text
([`write_string`](write_string.md), [`read_string`](read_string.md)) or by an explicit change
of position by (`set_tposition`, [`new_line`](new_line.md)). In order
to stop the display of the cursor, the operator [`set_tshape`](set_tshape.md)
with the parameter ”invisible” can be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row`** (input_control)  point.y `→`  (integer)

Row index of text cursor position.

Default:
24

**`Column`** (input_control)  point.x `→`  (integer)

Column index of text cursor position.

Default:
12

## Result

`set_tposition` returns 2 (
H_MSG_TRUE)
if the window is valid. Otherwise
an exception is raised.

## Possible Predecessors

`open_window`

## Possible Successors

`write_string`,
`read_string`

## Alternatives

`new_line`

## See also

`read_string`,
`write_string`

## Module

Foundation
