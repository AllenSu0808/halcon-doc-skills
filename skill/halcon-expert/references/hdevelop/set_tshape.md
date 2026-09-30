# set_tshape (Operator)

## Name

`set_tshape` — Set the shape of the text cursor.

## Warning

**`set_tshape` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`set_tshape( : : WindowHandle, TextCursor : )`

## Description

`set_tshape` sets the shape and the display mode of the text
cursor of the output window.

A text cursor marks the current position for text output. It is different
from the mouse cursor (although both will be called 'cursor', if the context
makes misconceptions impossible). The available shapes for the text cursor
can be queried with [`query_tshape`](query_tshape.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`TextCursor`** (input_control)  string `→`  (string)

Name of cursor shape.

Default:
'invisible'

## Result

`set_tshape` returns 2 (
H_MSG_TRUE)
if the window is valid and the
given cursor shape is defined for this window. Otherwise an
exception is raised.

## Possible Predecessors

`open_window`,
`query_tshape`,
`get_tshape`

## Possible Successors

`write_string`,
`read_string`

## See also

`get_tshape`,
`query_tshape`,
`write_string`,
`read_string`

## Module

Foundation
