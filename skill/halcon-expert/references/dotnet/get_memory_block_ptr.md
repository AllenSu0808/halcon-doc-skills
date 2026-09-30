# GetMemoryBlockPtr (Operator)

## Name

`GetMemoryBlockPtr` — Return the data pointer and size of a memory block.

## Warning

**It is not recommended to use the operator `GetMemoryBlockPtr` in
HDevelop.**

## Signature

`static void HOperatorSet.GetMemoryBlockPtr(HTuple memoryBlockHandle, out HTuple pointer, out HTuple size)`

`IntPtr HMemoryBlock.GetMemoryBlockPtr(out int size)`

## Description

`GetMemoryBlockPtr` returns the data pointer to the beginning of a
memory block in *`pointer`* and its size in bytes in *`size`*.
*`memoryBlockHandle`* is the handle of the memory block.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`memoryBlockHandle`** (input_control)  memory_block `→` [HMemoryBlock](HMemoryBlock.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the memory block.

**`pointer`** (output_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Data pointer to the beginning of the memory block.

**`size`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Size of the memory block.

## Result

If the parameters are valid, the operator `GetMemoryBlockPtr` returns
the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMemoryBlockExtern`,
`CreateMemoryBlockExternCopy`,
`ImageToMemoryBlock`,
`ReadMemoryBlock`

## Module

Foundation
