# close_framegrabber (Operator)

## Name

`close_framegrabber` — Close specified image acquisition device.

## Signature

`close_framegrabber( : : AcqHandle : )`

## Description

The operator `close_framegrabber` closes the image acquisition device
specified by *`AcqHandle`*. In particular, allocated memory for data
buffers is released and the image acquisition device is made available for
other processes.

## Attention

For a multithreaded application,
[`info_framegrabber`](info_framegrabber.md), [`open_framegrabber`](open_framegrabber.md), and
`close_framegrabber` are executed exclusively. Thus,
they block the concurrent execution of each other, but run in
parallel with all non-exclusive operators outside of this group.

Make sure that `close_framegrabber` is not called for a framegrabber
handle that is being used by another thread concurrently.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- AcqHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`AcqHandle`** (input_control, state is modified)  framegrabber `→`  (handle)

Handle of the image acquisition device to be closed.

## Result

If the specified image acquisition device could be closed,
`close_framegrabber` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`grab_image`,
`grab_image_async`

## See also

`open_framegrabber`

## Module

Foundation
