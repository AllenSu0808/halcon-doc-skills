# tuple_environment (Operator)

## Name

`tuple_environment` — Read one or more environment variables.

## Signature

`tuple_environment( : : Names : Values)`

## Description

`tuple_environment` reads the content of all environment variables
that are referenced by their names in the input tuple *`Names`* and
returns the content with the output tuple *`Values`*. The input
tuple may only contain strings.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

### Exception: Empty input tuples

If the input tuple is empty, the operator returns an empty tuple.
Additionally, an empty string is returned for every
name within *`Names`* that does not denote a valid environment
variable.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_environment`,
which can be used in an expression in the following syntax:

[`Values := environment(Names)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_misc_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Names`** (input_control)  string(-array) `→`  (string)

Tuple containing name(s) of the environment
variable(s).

**`Values`** (output_control)  string(-array) `→`  (string)

Content of the environment variable(s).

## Alternatives

`tuple_strstr`,
`tuple_strrstr`,
`tuple_strchr`,
`tuple_strrchr`,
`tuple_strlen`,
`tuple_str_first_n`,
`tuple_str_last_n`,
`tuple_split`,
`tuple_substr`

## Module

Foundation
