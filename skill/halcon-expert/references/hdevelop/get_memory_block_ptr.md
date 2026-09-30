# get_memory_block_ptr (Operator)

## Name

`get_memory_block_ptr` — Return the data pointer and size of a memory block.

## Warning

**It is not recommended to use the operator `get_memory_block_ptr` in
HDevelop.**

## Signature

`get_memory_block_ptr( : : MemoryBlockHandle : Pointer, Size)`

## Description

`get_memory_block_ptr` returns the data pointer to the beginning of a
memory block in *`Pointer`* and its size in bytes in *`Size`*.
*`MemoryBlockHandle`* is the handle of the memory block.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MemoryBlockHandle`** (input_control)  memory_block `→`  (handle)

Handle of the memory block.

**`Pointer`** (output_control)  pointer `→`  (integer)

Data pointer to the beginning of the memory block.

**`Size`** (output_control)  integer `→`  (integer)

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
