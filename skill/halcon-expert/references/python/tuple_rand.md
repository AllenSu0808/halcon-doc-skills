# tuple_rand (Operator)

## Name

`tuple_rand` — Return a tuple of random numbers between 0 and 1.

## Signature

`def tuple_rand(length: int) -> Sequence[float]`

`def tuple_rand_s(length: int) -> float`

## Description

`tuple_rand` returns a tuple of random numbers distributed
uniformly in the interval [0,1). The parameter *`length`*
specifies the length of the output tuple, i.e., how many random
numbers are generated.

The random numbers are generated using the C function “drand48()”.
See the parameter *"seed_rand"* of [`set_system`](set_system.md) for
information on the used random seed.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_rand`,
which can be used in an expression in the following syntax:

[`Rand := rand(Length)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_misc_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`length`** (input_control)  number `→` int

Length of tuple to generate.

**`rand`** (output_control)  number(-array) `→` Sequence[float]

Tuple of random numbers.

## See also

`tuple_gen_const`

## Module

Foundation
