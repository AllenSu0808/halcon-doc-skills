# read_memory_block (Operator)

## Name

`read_memory_block` — Read a memory block from a file.

## Signature

`def read_memory_block(file_name: str) -> HHandle`

## Description

The operator `read_memory_block` reads the file *`file_name`* and
creates a new memory block in *`memory_block_handle`* that is an identical
copy of the bytes in the file.

The default HALCON file extension for memory block files is '.bin'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

Name of the file.

Default:
"memory_block.bin"

File extension:
.`bin`

**`memory_block_handle`** (output_control)  memory_block `→` HHandle

Memory block handle.

## Result

The operator `read_memory_block` returns the value 2 (
H_MSG_TRUE)
if the named
file was found and correctly read. Otherwise, an exception is raised.

## Possible Successors

`get_memory_block_ptr`,
`compare_memory_block`,
`memory_block_to_image`

## See also

`write_memory_block`

## Module

Foundation
