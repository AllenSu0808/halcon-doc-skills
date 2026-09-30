# CreateMemoryBlockExternCopy (Operator)

## Name

`CreateMemoryBlockExternCopy` — Create a memory block from an external pointer by copying.

## Signature

`static void HOperatorSet.CreateMemoryBlockExternCopy(HTuple pointer, HTuple size, out HTuple memoryBlockHandle)`

`public HMemoryBlock(IntPtr pointer, int size)`

`void HMemoryBlock.CreateMemoryBlockExternCopy(IntPtr pointer, int size)`

## Description

`CreateMemoryBlockExternCopy` creates a memory block by copying
bytes and returns its handle *`memoryBlockHandle`*. *`pointer`* is a
data pointer to the beginning of the memory to be copied. *`size`*
determines the number of bytes to be copied and with that the size of the
memory block in bytes.
Note that the memory copied by this operator is released when deleting
*`memoryBlockHandle`*, whereas the original memory in *`pointer`*
that is copied from is not released.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`pointer`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Data pointer of the memory block.

**`size`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Size of the memory block.

**`memoryBlockHandle`** (output_control)  memory_block `→` [HMemoryBlock](HMemoryBlock.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the memory block.

## Result

If the parameters are valid, the operator
`CreateMemoryBlockExternCopy` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`GetMemoryBlockPtr`,
`CompareMemoryBlock`,
`MemoryBlockToImage`,
`WriteMemoryBlock`

## Alternatives

`CreateMemoryBlockExtern`

## Module

Foundation
