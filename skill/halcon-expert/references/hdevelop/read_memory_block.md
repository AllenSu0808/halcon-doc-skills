# read_memory_block (Operator)

## Name

`read_memory_block` — Read a memory block from a file.

## Signature

`read_memory_block( : : FileName : MemoryBlockHandle)`

## Description

The operator `read_memory_block` reads the file *`FileName`* and
creates a new memory block in *`MemoryBlockHandle`* that is an identical
copy of the bytes in the file.

The default HALCON file extension for memory block files is '.bin'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

Name of the file.

Default:
'memory_block.bin'

File extension:
.`bin`

**`MemoryBlockHandle`** (output_control)  memory_block `→`  (handle)

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
