# compare_memory_block (Operator)

## Name

`compare_memory_block` — Compare contents of memory blocks regarding equality.

## Signature

`compare_memory_block( : : MemoryBlocks1, MemoryBlocks2 : IsEqual)`

## Description

The operator `compare_memory_block` compares the contents of two memory
block tuples and returns the comparison result in *`IsEqual`*. Therefore,
each memory block in the tuple *`MemoryBlocks1`* is compared to the
respective block in the tuple *`MemoryBlocks2`* with the same index.
*`IsEqual`* is set to TRUE if the number of elements of the two tuples
matches and if the length and byte content of each pair of memory blocks
coincides, otherwise to FALSE.

## Attention

Note that `compare_memory_block` compares the memory blocks regarding
their actual byte content, not their location in memory.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MemoryBlocks1`** (input_control)  memory_block(-array) `→`  (handle)

Tuple of reference memory blocks.

**`MemoryBlocks2`** (input_control)  memory_block(-array) `→`  (handle)

Tuple of test memory blocks.

**`IsEqual`** (output_control)  integer `→`  (integer)

Boolean result value.

## Result

The operator `compare_memory_block` returns the value 2 (
H_MSG_TRUE)
if the
passed handles are valid. Otherwise, an exception is raised.

## Possible Predecessors

`create_memory_block_extern`,
`create_memory_block_extern_copy`,
`image_to_memory_block`,
`read_memory_block`

## Module

Foundation
