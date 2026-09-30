# create_memory_block_extern (Operator)

## Name

`create_memory_block_extern` — Create a memory block from an external pointer.

## Warning

**It is not recommended to use the operator `create_memory_block_extern`
in HDevelop.**

## Signature

`def create_memory_block_extern(pointer: int, size: int, free_function: int) -> HHandle`

## Description

`create_memory_block_extern` creates a memory block and returns its
handle *`memory_block_handle`*. *`pointer`* is a data pointer to the
beginning of the memory block. *`size`* controls the size in bytes of the
memory block. *`free_function`* is an optional callback function that
frees the memory pointed to by *`pointer`*. This function must have the
following signature

```
    void FreeFunction(void* ptr);
```

and will be called using `__cdecl` calling convention when deleting
*`memory_block_handle`*. Hence, HALCON gains ownership over the memory in
this case and releases the memory via the callback function. If the memory
shall not be released when deleting *`memory_block_handle`*, i.e., HALCON
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

**`pointer`** (input_control)  pointer `→` int

Data pointer of the memory block.

**`size`** (input_control)  integer `→` int

Size of the memory block.

**`free_function`** (input_control)  pointer `→` int

Function to free the memory block.

Default:
0

**`memory_block_handle`** (output_control)  memory_block `→` HHandle

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
