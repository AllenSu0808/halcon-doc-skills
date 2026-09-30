# exit (Operator)

## Name

`exit` — Terminate HDevelop.

## Signature

`exit( : : : )`

## Description

`exit` terminates HDevelop.
The operator is equivalent to the menu entry
`File` -> `Quit`.
Internally and for exported C++ code the C-function call
`exit(0)` is used.

## Example (HDevelop)

```
read_image (Image, 'fabrik')
intensity (Image, Image, Mean, Deviation)
open_file ('intensity.txt', 'output', FileHandle)
fwrite_string (FileHandle, Mean + ' ' + Deviation)
close_file (FileHandle)
exit ()
```

## Result

`exit` returns 0 (o.k.) to the calling environment of
HDevelop = operating system.

## See also

`stop`

## Module

Foundation
