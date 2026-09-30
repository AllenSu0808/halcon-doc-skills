# dump_window (Operator)

## Name

`dump_window` — Write the window content to a file.

## Signature

`dump_window( : : WindowHandle, Device, FileName : )`

## Description

`dump_window` writes the content of the window to a
file. You may continue to process this file by convenient printers or
other programs.
The content of a display is prepared for each special device
(*`Device`*), i.e., it is formatted in a manner, that you may
print this file directly or it can be processed furthermore by
a graphical program.

To transform gray values the current color table of the window is
used.

Possible values for *`Device`*

- **'postscript':** —

  PostScript - file.
  File extension: '.ps'
- **'postscript',Width,Height:** —

  PostScript - file with specification of the output size.
  Width and Height refer to the size.
  In this case a tuple with three values as *`Device`*
  is passed.

  File extension: '.ps'
- **'tiff':** —

  TIFF format; Compression is possible with Adobe deflate
  compression (*'deflate [num]'*, lossless), JPEG
  (*'jpeg [num]'*, lossy), LZW (*'lzw'*, lossless),
  and PackBits (*'packbits'*, lossless). Here,
  *'[num]'* denotes an optional specification of a
  compression parameter. For *'deflate'*, a number between
  *0* (no compression) and *9* (maximum compression)
  can be specified. For *'jpeg'*, a number between
  *0* and *100* can be specified. The semantics are
  identical to the semantics of 'jpeg' described below. The
  different options can be accumulated by appending them separated
  by a space character.
  Examples:
  *'tiff deflate 9'*: Maximum Adobe deflate compression;
  *'tiff jpeg 90'*: JPEG compression with high quality;
  *'tiff lzw'*: LZW compression;
  *'tiff'* or *'tiff none'*: no compression.

  File extension: '.tif'
- **'bmp':** —

  Windows-BMP format, RGB image, 3 bytes per pixel.
  The color resolution depends on the VGA card.

  File extension: '.bmp'
- **'jpeg':** —

  JPEG format, with lost of information; together with the format
  string the quality value determining the compression rate can be
  provided: e.g., 'jpeg 30'.

  File extension: '.jpg'
- **'jpegxr':** —

  JPEG-XR format (lossless and lossy compression); together with the format
  string the quality value determining the compression rate can be
  provided: e.g., 'jpegxr 30'.

  File extension: '.jxr'
- **'jp2':** —

  JPEG2000 format (lossless and lossy compression); together with
  the format string the quality value determining the compression rate
  can be provided (e.g., 'jp2 40'). This value corresponds to the
  ratio of the size of the compressed image and the size of the
  uncompressed image (in percent). As lossless JPEG2000 compression
  reduces the file size significantly already, only smaller values
  (typically smaller than 50) influence the file size. Is no value
  provided (and only then), the image is compressed without loss.

  File extension: '.jp2'
- **'png':** —

  PNG format (lossless compression); together with the format string,
  a compression level between 0 and 9 can be specified, where 0
  corresponds to no compression and 9 to the best possible
  compression. Alternatively, the compression can be selected with
  the following strings: 'best', 'fastest', and 'none'. Hence,
  examples for correct parameters are 'png', 'png 7', and 'png none'.

  File extension: '.png'

## Attention

Under Unix-like systems, the graphics window must be completely visible on the
root window, because otherwise the contents of the window cannot be
read due to limitations in X Windows. If larger graphical displays
are to be written to a file, the window type *'pixmap'* can
be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Device`** (input_control)  string(-array) `→`  (string / integer)

Name of the target device or of the graphic format.

Default:
'postscript'

Suggested values:
'postscript', 'tiff', 'tiff deflate 9', 'tiff jpeg 90', 'tiff lzw', 'tiff packbits', 'bmp', 'jpeg', 'jpeg 100', 'jpeg 80', 'jpeg 60', 'jpeg 40', 'jpeg 20', 'jpegxr', 'jpegxr 50', 'jpegxr 40', 'jpegxr 30', 'jpegxr 20', 'jp2', 'jp2 50', 'jp2 40', 'jp2 30', 'jp2 20', 'png', 'png best', 'png fastest', 'png none'

**`FileName`** (input_control)  filename.write `→`  (string)

File name (without extension).

Default:
'halcon_dump'

## Example (HDevelop)

```
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
read_image (Image, 'fabrik')
gen_circle (Circle, 200, 200, 100.5)
dev_display (Image)
dev_display (Circle)
dump_window(WindowHandle,'postscript','halcon_dump')
```

## Result

If the appropriate window is valid and the specified parameters are
correct `dump_window` returns 2 (
H_MSG_TRUE)
. If necessary an exception
is raised.

## Possible Predecessors

`open_window`,
`set_draw`,
`set_color`,
`set_colored`,
`set_line_width`,
`disp_region`

## Possible Successors

`system_call`

## See also

`open_window`,
`set_system`,
`dump_window_image`

## Module

Foundation
