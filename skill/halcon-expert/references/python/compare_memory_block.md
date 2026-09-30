# compare_memory_block (Operator)

## Name

`compare_memory_block` — Compare contents of memory blocks regarding equality.

## Signature

`def compare_memory_block(memory_blocks_1: MaybeSequence[HHandle], memory_blocks_2: MaybeSequence[HHandle]) -> int`

## Description

The operator `compare_memory_block` compares the contents of two memory
block tuples and returns the comparison result in *`is_equal`*. Therefore,
each memory block in the tuple *`memory_blocks_1`* is compared to the
respective block in the tuple *`memory_blocks_2`* with the same index.
*`is_equal`* is set to TRUE if the number of elements of the two tuples
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

**`memory_blocks_1`** (input_control)  memory_block(-array) `→` MaybeSequence[HHandle]

Tuple of reference memory blocks.

**`memory_blocks_2`** (input_control)  memory_block(-array) `→` MaybeSequence[HHandle]

Tuple of test memory blocks.

**`is_equal`** (output_control)  integer `→` int

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
