# dev_set_lut (Operator)

## Name

`dev_set_lut` — Set “look-up-table” (lut).

## Signature

`dev_set_lut( : : LutName : )`

## Description

`dev_set_lut` sets the look-up-table of the active graphics window.
A look-up-table defines the transformation of a “gray value” from an
one-channel-image into a gray value or color on the screen.
[`query_lut`](query_lut.md) lists the names of all look-up-tables.

For more information see the description of the operator
[`set_lut`](set_lut.md).
However, in contrast to that operator the new look-up-table is also used for
all new graphics windows that are opened afterwards.

## Attention

Using the code export feature of HDevelop, the code that is generated
for this operator may have a different behavior than the related
HALCON operator.
For a detailed description of the code export of HDevelop graphics
operators into the different programming languages see in the
`“HDevelop User's Guide”` the chapter `Code Export`
-> `General Aspects of Code Generation`
-> `Graphics Windows`.

## Parameters

**`LutName`** (input_control)  filename.read(-array) `→`  (string / real / integer)

Name of look-up-table, values of look-up-table (RGB)
or file name.

Default:
'default'

Suggested values:
'default', 'linear', 'inverse', 'sqr', 'inv_sqr', 'cube', 'inv_cube', 'sqrt', 'inv_sqrt', 'cubic_root', 'inv_cubic_root', 'color1', 'color2', 'color3', 'color4', 'three', 'six', 'twelve', 'twenty_four', 'rainbow', 'temperature', 'cyclic_gray', 'cyclic_temperature', 'hsi', 'change1', 'change2', 'change3', 'jet', 'inverse_jet', 'batlow', 'inverse_batlow'

File extension:
.`lut`

## Example (HDevelop)

```
read_image(Image,'mreut')
dev_set_lut('inverse')
* For true color only:
dev_display(Image)
```

## Result

If the values of the specified parameters are correct,
`dev_set_lut` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Successors

`dev_display`

## See also

`set_lut`

## Module

Foundation
