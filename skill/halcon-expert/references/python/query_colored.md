# query_colored (Operator)

## Name

`query_colored` — Query the number of colors for color output.

## Signature

`def query_colored() -> Sequence[int]`

## Description

`query_colored` returns all possible parameter values for
[`set_colored`](set_colored.md). [`set_colored`](set_colored.md) defines how many
colors are used for region or graphics output.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`possible_number_of_colors`** (output_control)  integer-array `→` Sequence[int]

Tuple of the possible numbers of colors.

## Result

`query_colored` always returns 2 (
H_MSG_TRUE)
.

## Possible Successors

`set_colored`,
`set_color`,
`disp_region`

## Alternatives

`query_color`

## See also

`set_colored`,
`set_color`

## Module

Foundation
