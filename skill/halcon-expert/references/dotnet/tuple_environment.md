# TupleEnvironment (Operator)

## Name

`TupleEnvironment` — Read one or more environment variables.

## Signature

`static void HOperatorSet.TupleEnvironment(HTuple names, out HTuple values)`

`HTuple HTuple.TupleEnvironment()`

## Description

`TupleEnvironment` reads the content of all environment variables
that are referenced by their names in the input tuple *`names`* and
returns the content with the output tuple *`values`*. The input
tuple may only contain strings.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

### Exception: Empty input tuples

If the input tuple is empty, the operator returns an empty tuple.
Additionally, an empty string is returned for every
name within *`names`* that does not denote a valid environment
variable.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleEnvironment`,
which can be used in an expression in the following syntax:

[`Values := environment(Names)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_misc_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`names`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Tuple containing name(s) of the environment
variable(s).

**`values`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Content of the environment variable(s).

## Alternatives

`TupleStrstr`,
`TupleStrrstr`,
`TupleStrchr`,
`TupleStrrchr`,
`TupleStrlen`,
`TupleStrFirstN`,
`TupleStrLastN`,
`TupleSplit`,
`TupleSubstr`

## Module

Foundation
