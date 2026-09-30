# get_tshape (Operator)

## Name

`get_tshape` — Get the shape of the text cursor.

## Warning

**`get_tshape` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`get_tshape( : : WindowHandle : TextCursor)`

## Description

`get_tshape` queries the shape of the text cursor for the
output window. A new cursor shape is set by the operator
[`set_tshape`](set_tshape.md).

A text cursor marks the current position for text output (which can also
be invisible). It is different from the mouse cursor (although both will
be called ”cursor” if the context makes misconceptions impossible).
The available shapes for the text cursor can be queried with
[`query_tshape`](query_tshape.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`TextCursor`** (output_control)  string `→`  (string)

Name of the current text cursor.

## Result

`get_tshape` returns 2 (
H_MSG_TRUE)
if the window is valid. Otherwise an
exception is raised.

## Possible Predecessors

`open_window`,
`set_font`

## Possible Successors

`set_tshape`,
`set_tposition`,
`write_string`,
`read_string`,
`read_char`

## See also

`set_tshape`,
`query_tshape`,
`write_string`,
`read_string`

## Module

Foundation
