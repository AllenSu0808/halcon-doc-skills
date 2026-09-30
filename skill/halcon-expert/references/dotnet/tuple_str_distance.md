# TupleStrDistance (Operator)

## Name

`TupleStrDistance` — Calculate the distance between strings.

## Signature

`static void HOperatorSet.TupleStrDistance(HTuple string1, HTuple string2, HTuple mode, out HTuple distance)`

`HTuple HTuple.TupleStrDistance(HTuple string2, HTuple mode)`

## Description

`TupleStrDistance` computes the edit distance between *`string1`*
and *`string2`* and returns the result in *`distance`*.
The distance measure used is specified in *`mode`*.
Both input tuples may only consist of strings. Otherwise, `TupleStrDistance`
returns an error.
As an exception, an empty tuple in *`string1`* or *`string2`* cause
*`distance`* to also be empty.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each of the input tuples *`string1`* and *`string2`*
can be given as a tuple of length *1* or *"N"*.
Parameters with tuple length *1* will be repeated internally
such that the number of computed distances is always *"N"*.

### Supported distance measures

- *"levenshtein"*:
  Uses the Levenshtein distance to quantify string distances. The
  Levenshtein distance is the minimum number of edit operations
  required to transform *`string1`* into *`string2`*.
  Valid edit operations are insertion, deletion and replacement of
  characters.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleStrDistance`,
which can be used in an expression in the following syntax:

[`Result := str_distance(String1, String2, Mode)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`string1`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Input tuple.

Default:
"String1"

**`string2`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Input tuple.

Default:
"String2"

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Distance measure.

Default:
"levenshtein"

List of values:
"levenshtein"

**`distance`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Element-wise string distance.

## Possible Predecessors

`GetTextResult`,
`FindText`,
`DoOcrWordMlp`

## Alternatives

`SuggestLexicon`

## References

Vladimir I. Levenshtein, Binary codes capable of correcting deletions, insertions,
and reversals, Doklady Akademii Nauk SSSR, 163(4):845-848, 1965 (Russian).
English translation in Soviet Physics Doklady, 10(8):707-710, 1966.

## Module

Foundation
