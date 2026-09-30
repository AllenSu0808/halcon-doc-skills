# create_memory_block_extern (Operator)

## Name

`create_memory_block_extern` — Create a memory block from an external pointer.

## Warning

**It is not recommended to use the operator `create_memory_block_extern`
in HDevelop.**

## Signature

`create_memory_block_extern( : : Pointer, Size, FreeFunction : MemoryBlockHandle)`

## Description

`create_memory_block_extern` creates a memory block and returns its
handle *`MemoryBlockHandle`*. *`Pointer`* is a data pointer to the
beginning of the memory block. *`Size`* controls the size in bytes of the
memory block. *`FreeFunction`* is an optional callback function that
frees the memory pointed to by *`Pointer`*. This function must have the
following signature

```
    void FreeFunction(void* ptr);
```

and will be called using `__cdecl` calling convention when deleting
*`MemoryBlockHandle`*. Hence, HALCON gains ownership over the memory in
this case and releases the memory via the callback function. If the memory
shall not be released when deleting *`MemoryBlockHandle`*, i.e., HALCON
shall not own the memory, the NULL-Pointer can be passed.

## Attention

This operator does not copy any data. If a copy is required
[`create_memory_block_extern_copy`](create_memory_block_extern_copy.md) can be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Pointer`** (input_control)  pointer `→`  (integer)

Data pointer of the memory block.

**`Size`** (input_control)  integer `→`  (integer)

Size of the memory block.

**`FreeFunction`** (input_control)  pointer `→`  (integer)

Function to free the memory block.

Default:
0

**`MemoryBlockHandle`** (output_control)  memory_block `→`  (handle)

Handle of the memory block.

## Result

If the parameters are valid, the operator `create_memory_block_extern`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`get_memory_block_ptr`,
`compare_memory_block`,
`memory_block_to_image`,
`write_memory_block`

## Alternatives

`create_memory_block_extern_copy`

## Module

Foundation
