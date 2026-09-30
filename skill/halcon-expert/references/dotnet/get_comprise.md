# GetComprise (Operator)

## Name

`GetComprise` — Get the output treatment of an image matrix.

## Warning

**`GetComprise` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.GetComprise(HTuple windowHandle, out HTuple mode)`

`static string HInfo.GetComprise(HWindow windowHandle)`

## Description

`GetComprise` returns the output mode of gray values in the
window *`windowHandle`* that is used by [`DispImage`](disp_image.md) and
[`DispColor`](disp_color.md). The output mode defines whether only the
gray values of objects are displayed or the whole image is displayed.
The query is used for temporary mode settings, i.e., the current
mode is queried, then overwritten with ([`SetComprise`](set_comprise.md)) and
finally reset.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`mode`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Display mode for images.

## Result

`GetComprise` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`SetComprise`,
`DispImage`,
`DispImage`

## See also

`SetComprise`,
`DispImage`,
`DispColor`

## Module

Foundation
