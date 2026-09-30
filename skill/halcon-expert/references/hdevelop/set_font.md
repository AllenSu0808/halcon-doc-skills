# set_font (Operator)

## Name

`set_font` — Set the font used for text output.

## Signature

`set_font( : : WindowHandle, Font : )`

## Description

`set_font` sets the font *`Font`* for the output window
*`WindowHandle`*. All subsequent text outputs (e.g., with
the operators [`disp_text`](disp_text.md), [`write_string`](write_string.md) or [`read_string`](read_string.md))
will now use the new font instead of the default font (see
`set_system('default_font',Font)`).
All available fonts can be queried with [`query_font`](query_font.md).

The syntax for the specification of *`Font`* is the following:

```
     FONTNAME[-STYLE]-FONT_SIZE.
```

The optional STYLE may be one of the following (other values are possible as
well):

- Normal,
- Bold,
- BoldItalic, or
- Italic.

The FONT_SIZE is measured in pixels.

An example of a valid string for *`Font`* would be

'Courier-Bold-14'.

## Attention

For different machines the available fonts may differ a lot. Therefore it
is suggested to use the operator [`query_font`](query_font.md) or the procedure
set_display_font.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Font`** (input_control)  string `→`  (string)

Name of new font.

## Example (HDevelop)

```
dev_get_window (WindowHandle)
query_font (WindowHandle, Font)
* Specify font name and size
FontWithSize := Font[0]+'-20'
set_font (WindowHandle, FontWithSize)
dev_disp_text ('Font set to: '+FontWithSize, 'window', 20, 12, 'black', \
               [], [])
* Specify font name, style, and size
FontWithStyleAndSize := Font[0]+'-Bold-20'
set_font (WindowHandle, FontWithStyleAndSize)
dev_disp_text ('Font set to: '+FontWithStyleAndSize, 'window', 50, 12, \
               'black', [], [])
```

## Result

`set_font` returns 2 (
H_MSG_TRUE)
if the font name can be resolved.
Otherwise an exception is raised.

## Possible Predecessors

`open_window`

## Possible Successors

`query_font`

## See also

`get_font`,
`query_font`,
`open_window`

## Module

Foundation
