# CloseFramegrabber (Operator)

## Name

`CloseFramegrabber` — Close specified image acquisition device.

## Signature

`static void HOperatorSet.CloseFramegrabber(HTuple acqHandle)`

`void HFramegrabber.CloseFramegrabber()`

## Description

The operator `CloseFramegrabber` closes the image acquisition device
specified by *`acqHandle`*. In particular, allocated memory for data
buffers is released and the image acquisition device is made available for
other processes.

## Attention

For a multithreaded application,
[`InfoFramegrabber`](info_framegrabber.md), [`OpenFramegrabber`](open_framegrabber.md), and
`CloseFramegrabber` are executed exclusively. Thus,
they block the concurrent execution of each other, but run in
parallel with all non-exclusive operators outside of this group.

Make sure that `CloseFramegrabber` is not called for a framegrabber
handle that is being used by another thread concurrently.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- acqHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`acqHandle`** (input_control, state is modified)  framegrabber `→` [HFramegrabber](HFramegrabber.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the image acquisition device to be closed.

## Result

If the specified image acquisition device could be closed,
`CloseFramegrabber` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`GrabImage`,
`GrabImageAsync`

## See also

`OpenFramegrabber`

## Module

Foundation
