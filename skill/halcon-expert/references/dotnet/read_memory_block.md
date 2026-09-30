# ReadMemoryBlock (Operator)

## Name

`ReadMemoryBlock` — Read a memory block from a file.

## Signature

`static void HOperatorSet.ReadMemoryBlock(HTuple fileName, out HTuple memoryBlockHandle)`

`public HMemoryBlock(string fileName)`

`void HMemoryBlock.ReadMemoryBlock(string fileName)`

## Description

The operator `ReadMemoryBlock` reads the file *`fileName`* and
creates a new memory block in *`memoryBlockHandle`* that is an identical
copy of the bytes in the file.

The default HALCON file extension for memory block files is '.bin'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Name of the file.

Default:
"memory_block.bin"

File extension:
.`bin`

**`memoryBlockHandle`** (output_control)  memory_block `→` [HMemoryBlock](HMemoryBlock.md), [HTuple](HTuple.md) (*IntPtr*)

Memory block handle.

## Result

The operator `ReadMemoryBlock` returns the value 2 (
H_MSG_TRUE)
if the named
file was found and correctly read. Otherwise, an exception is raised.

## Possible Successors

`GetMemoryBlockPtr`,
`CompareMemoryBlock`,
`MemoryBlockToImage`

## See also

`WriteMemoryBlock`

## Module

Foundation
