# CreateMemoryBlockExtern (Operator)

## Name

`CreateMemoryBlockExtern` — Create a memory block from an external pointer.

## Warning

**It is not recommended to use the operator `CreateMemoryBlockExtern`
in HDevelop.**

## Signature

`static void HOperatorSet.CreateMemoryBlockExtern(HTuple pointer, HTuple size, HTuple freeFunction, out HTuple memoryBlockHandle)`

`public HMemoryBlock(IntPtr pointer, int size, IntPtr freeFunction)`

`void HMemoryBlock.CreateMemoryBlockExtern(IntPtr pointer, int size, IntPtr freeFunction)`

## Description

`CreateMemoryBlockExtern` creates a memory block and returns its
handle *`memoryBlockHandle`*. *`pointer`* is a data pointer to the
beginning of the memory block. *`size`* controls the size in bytes of the
memory block. *`freeFunction`* is an optional callback function that
frees the memory pointed to by *`pointer`*. This function must have the
following signature

```
    void FreeFunction(void* ptr);
```

and will be called using `__cdecl` calling convention when deleting
*`memoryBlockHandle`*. Hence, HALCON gains ownership over the memory in
this case and releases the memory via the callback function. If the memory
shall not be released when deleting *`memoryBlockHandle`*, i.e., HALCON
shall not own the memory, the NULL-Pointer can be passed.

## Attention

This operator does not copy any data. If a copy is required
[`CreateMemoryBlockExternCopy`](create_memory_block_extern_copy.md) can be used.

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

**`freeFunction`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Function to free the memory block.

Default:
0

**`memoryBlockHandle`** (output_control)  memory_block `→` [HMemoryBlock](HMemoryBlock.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the memory block.

## Result

If the parameters are valid, the operator `CreateMemoryBlockExtern`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`GetMemoryBlockPtr`,
`CompareMemoryBlock`,
`MemoryBlockToImage`,
`WriteMemoryBlock`

## Alternatives

`CreateMemoryBlockExternCopy`

## Module

Foundation
