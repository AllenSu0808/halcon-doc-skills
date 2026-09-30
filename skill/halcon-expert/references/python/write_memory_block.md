# write_memory_block (Operator)

## Name

`write_memory_block` — Write a memory block to a file.

## Signature

`def write_memory_block(memory_block_handle: HHandle, file_name: str) -> None`

## Description

The operator `write_memory_block` writes the byte content of the memory
block *`memory_block_handle`* to the file *`file_name`*. The memory
block can be read again with [`read_memory_block`](read_memory_block.md).

The default HALCON file extension for memory block files is '.bin', but any
file extension can be chosen, including none.

## Attention

Choosing a file extension that does not fit the byte content of the memory
block *`memory_block_handle`* only changes the name of the file, not the
bytes written to disk.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`memory_block_handle`** (input_control)  memory_block `→` HHandle

Memory block handle.

**`file_name`** (input_control)  filename.write `→` str

Name of the file.

Default:
"memory_block.bin"

File extension:
.`bin`

## Result

The operator `write_memory_block` returns the value 2 (
H_MSG_TRUE)
if the
passed handle is valid and if the memory block was successfully written into
the named file. Otherwise, an exception is raised.

## Possible Predecessors

`create_memory_block_extern`,
`create_memory_block_extern_copy`,
`image_to_memory_block`

## See also

`read_memory_block`

## Module

Foundation
