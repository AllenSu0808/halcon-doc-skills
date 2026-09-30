# dev_set_colored (Operator)

## Name

`dev_set_colored` — Set multiple output colors.

## Signature

`dev_set_colored( : : NumColors : )`

## Description

`dev_set_colored` allows to display tuples of regions, XLDs, and other
geometrical objects in the graphics windows in different colors using a set
of *`NumColors`* predefined colors.
Valid values for *`NumColors`* can be queried with the operator
[`query_colored`](query_colored.md).

For more information see the description of the operator [`set_colored`](set_colored.md).
However, in contrast to that operator the color setting is also used for
all new graphics windows that are opened afterwards.

These color settings remain valid until [`dev_set_color`](dev_set_color.md) or
`dev_set_colored` is called or until the color setting are modified
interactively.

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

**`NumColors`** (input_control)  integer `→`  (integer)

Number of output colors.

Default:
6

List of values:
3, 6, 12

## Example (HDevelop)

```
read_image(Image,'monkey')
threshold(Image,Region,128,255)
dev_set_colored(6)
connection(Region,Regions)
```

## Result

If the values of the specified parameters are correct,
`dev_set_colored` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Predecessors

`dev_open_window`

## Possible Successors

`dev_display`

## Alternatives

`dev_set_color`

## See also

`dev_set_draw`,
`dev_set_line_width`,
`set_colored`

## Module

Foundation
