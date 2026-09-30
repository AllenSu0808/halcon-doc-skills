# create_memory_block_extern_copy (Operator)

## Name

`create_memory_block_extern_copy` — Create a memory block from an external pointer by copying.

## Signature

`def create_memory_block_extern_copy(pointer: int, size: int) -> HHandle`

## Description

`create_memory_block_extern_copy` creates a memory block by copying
bytes and returns its handle *`memory_block_handle`*. *`pointer`* is a
data pointer to the beginning of the memory to be copied. *`size`*
determines the number of bytes to be copied and with that the size of the
memory block in bytes.
Note that the memory copied by this operator is released when deleting
*`memory_block_handle`*, whereas the original memory in *`pointer`*
that is copied from is not released.

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

**`memory_block_handle`** (output_control)  memory_block `→` HHandle

Handle of the memory block.

## Result

If the parameters are valid, the operator
`create_memory_block_extern_copy` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`get_memory_block_ptr`,
`compare_memory_block`,
`memory_block_to_image`,
`write_memory_block`

## Alternatives

`create_memory_block_extern`

## Module

Foundation
