# get_comprise (Operator)

## Name

`get_comprise` — Get the output treatment of an image matrix.

## Warning

**`get_comprise` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def get_comprise(window_handle: HHandle) -> str`

## Description

`get_comprise` returns the output mode of gray values in the
window *`window_handle`* that is used by [`disp_image`](disp_image.md) and
[`disp_color`](disp_color.md). The output mode defines whether only the
gray values of objects are displayed or the whole image is displayed.
The query is used for temporary mode settings, i.e., the current
mode is queried, then overwritten with ([`set_comprise`](set_comprise.md)) and
finally reset.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`mode`** (output_control)  string `→` str

Display mode for images.

## Result

`get_comprise` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`set_comprise`,
`disp_image`,
`disp_image`

## See also

`set_comprise`,
`disp_image`,
`disp_color`

## Module

Foundation
