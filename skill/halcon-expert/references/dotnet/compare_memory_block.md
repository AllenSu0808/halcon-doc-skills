# CompareMemoryBlock (Operator)

## Name

`CompareMemoryBlock` — Compare contents of memory blocks regarding equality.

## Signature

`static void HOperatorSet.CompareMemoryBlock(HTuple memoryBlocks1, HTuple memoryBlocks2, out HTuple isEqual)`

## Description

The operator `CompareMemoryBlock` compares the contents of two memory
block tuples and returns the comparison result in *`isEqual`*. Therefore,
each memory block in the tuple *`memoryBlocks1`* is compared to the
respective block in the tuple *`memoryBlocks2`* with the same index.
*`isEqual`* is set to TRUE if the number of elements of the two tuples
matches and if the length and byte content of each pair of memory blocks
coincides, otherwise to FALSE.

## Attention

Note that `CompareMemoryBlock` compares the memory blocks regarding
their actual byte content, not their location in memory.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`memoryBlocks1`** (input_control)  memory_block(-array) `→` [HMemoryBlock](HMemoryBlock.md), [HTuple](HTuple.md) (*IntPtr*)

Tuple of reference memory blocks.

**`memoryBlocks2`** (input_control)  memory_block(-array) `→` [HMemoryBlock](HMemoryBlock.md), [HTuple](HTuple.md) (*IntPtr*)

Tuple of test memory blocks.

**`isEqual`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Boolean result value.

## Result

The operator `CompareMemoryBlock` returns the value 2 (
H_MSG_TRUE)
if the
passed handles are valid. Otherwise, an exception is raised.

## Possible Predecessors

`CreateMemoryBlockExtern`,
`CreateMemoryBlockExternCopy`,
`ImageToMemoryBlock`,
`ReadMemoryBlock`

## Module

Foundation
