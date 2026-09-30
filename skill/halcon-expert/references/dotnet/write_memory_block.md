# WriteMemoryBlock (Operator)

## Name

`WriteMemoryBlock` — Write a memory block to a file.

## Signature

`static void HOperatorSet.WriteMemoryBlock(HTuple memoryBlockHandle, HTuple fileName)`

## Description

The operator `WriteMemoryBlock` writes the byte content of the memory
block *`memoryBlockHandle`* to the file *`fileName`*. The memory
block can be read again with [`ReadMemoryBlock`](read_memory_block.md).

The default HALCON file extension for memory block files is '.bin', but any
file extension can be chosen, including none.

## Attention

Choosing a file extension that does not fit the byte content of the memory
block *`memoryBlockHandle`* only changes the name of the file, not the
bytes written to disk.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`memoryBlockHandle`** (input_control)  memory_block `→` [HMemoryBlock](HMemoryBlock.md), [HTuple](HTuple.md) (*IntPtr*)

Memory block handle.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the file.

Default:
"memory_block.bin"

File extension:
.`bin`

## Result

The operator `WriteMemoryBlock` returns the value 2 (
H_MSG_TRUE)
if the
passed handle is valid and if the memory block was successfully written into
the named file. Otherwise, an exception is raised.

## Possible Predecessors

`CreateMemoryBlockExtern`,
`CreateMemoryBlockExternCopy`,
`ImageToMemoryBlock`

## See also

`ReadMemoryBlock`

## Module

Foundation
