# get_memory_block_ptr (Operator)

## Name

`get_memory_block_ptr` — Return the data pointer and size of a memory block.

## Warning

**It is not recommended to use the operator `get_memory_block_ptr` in
HDevelop.**

## Signature

`def get_memory_block_ptr(memory_block_handle: HHandle) -> Tuple[int, int]`

## Description

`get_memory_block_ptr` returns the data pointer to the beginning of a
memory block in *`pointer`* and its size in bytes in *`size`*.
*`memory_block_handle`* is the handle of the memory block.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`memory_block_handle`** (input_control)  memory_block `→` HHandle

Handle of the memory block.

**`pointer`** (output_control)  pointer `→` int

Data pointer to the beginning of the memory block.

**`size`** (output_control)  integer `→` int

Size of the memory block.

## Result

If the parameters are valid, the operator `get_memory_block_ptr` returns
the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_memory_block_extern`,
`create_memory_block_extern_copy`,
`image_to_memory_block`,
`read_memory_block`

## Module

Foundation
