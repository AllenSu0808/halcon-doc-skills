# query_tshape (Operator)

## Name

`query_tshape` — Query all shapes available for text cursors.

## Warning

**`query_tshape` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def query_tshape(window_handle: HHandle) -> Sequence[str]`

## Description

`query_tshape` queries the available shapes of text
cursors for the output window. The retrieved shapes can be
used by the operator [`set_tshape`](set_tshape.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`text_cursor`** (output_control)  string-array `→` Sequence[str]

Names of the available text cursors.

## Result

`query_tshape` returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`open_window`

## Possible Successors

`set_tshape`,
`write_string`,
`read_string`

## See also

`set_tshape`,
`get_shape`,
`set_tposition`,
`write_string`,
`read_string`

## Module

Foundation
