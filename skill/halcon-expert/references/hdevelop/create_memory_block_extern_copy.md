# create_memory_block_extern_copy (Operator)

## Name

`create_memory_block_extern_copy` — Create a memory block from an external pointer by copying.

## Signature

`create_memory_block_extern_copy( : : Pointer, Size : MemoryBlockHandle)`

## Description

`create_memory_block_extern_copy` creates a memory block by copying
bytes and returns its handle *`MemoryBlockHandle`*. *`Pointer`* is a
data pointer to the beginning of the memory to be copied. *`Size`*
determines the number of bytes to be copied and with that the size of the
memory block in bytes.
Note that the memory copied by this operator is released when deleting
*`MemoryBlockHandle`*, whereas the original memory in *`Pointer`*
that is copied from is not released.

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

**`MemoryBlockHandle`** (output_control)  memory_block `→`  (handle)

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
