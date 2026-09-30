# set_comprise (Operator)

## Name

`set_comprise` — Define the image matrix output clipping.

## Warning

**`set_comprise` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def set_comprise(window_handle: HHandle, mode: str) -> None`

## Description

`set_comprise` defines the image matrix output
clipping. If *`mode`* is set to 'object', only gray values
belonging to the output object are displayed. If set to 'image', the
whole image matrix is displayed. Default is 'object'.

## Attention

If *`mode`* was set to 'image', undefined gray values may be
displayed. Depending on the context they are black or can have
random content. See the examples.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`mode`** (input_control)  string `→` str

Clipping mode for gray value output.

Default:
"object"

List of values:
"image", "object"

## Example (HDevelop)

```
read_image(Image,'fabrik')
gen_circle (Circle, 200, 200, 100.5)
reduce_domain (Image, Circle, ImageReduced)
set_system('init_new_image','false')
sobel_amp(ImageReduced,SobelReduced,'sum_abs',3)
dev_display (SobelReduced)
get_comprise(WindowHandle,Mode)
set_comprise(WindowHandle,'image')
stop ()
dev_display (SobelReduced)
```

## Result

`set_comprise` returns 2 (
H_MSG_TRUE)
if *`mode`*
is correct and the window is valid. Otherwise an exception is
raised.

## Possible Predecessors

`get_comprise`

## Possible Successors

`disp_image`

## See also

`get_comprise`,
`disp_image`,
`disp_color`

## Module

Foundation
