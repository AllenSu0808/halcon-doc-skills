# write_lut (Operator)

## Name

`write_lut` — Write look-up-table (lut) as file.

## Warning

**`write_lut` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`write_lut( : : WindowHandle, FileName : )`

## Description

`write_lut` saves the look-up-table (resp. the part of it that
is relevant for displaying image gray values) of the valid output
window into a file named '*`FileName`*.lut'. It can be read again
later with [`set_lut`](set_lut.md).

## Attention

`write_lut` is only suitable for systems using 256 colors.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`FileName`** (input_control)  filename.write `→`  (string)

File name (of file containing the look-up-table).

Default:
'/tmp/lut'

File extension:
.`lut`

## Result

`write_lut` returns 2 (
H_MSG_TRUE)
if the window with the required
properties (256 colors) is valid and the parameter (file name) is
correct. Otherwise an exception is raised.

## Possible Predecessors

`set_lut`

## See also

`set_lut`,
`set_pixel`,
`get_pixel`

## Module

Foundation
