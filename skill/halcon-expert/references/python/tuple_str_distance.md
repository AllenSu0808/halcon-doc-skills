# tuple_str_distance (Operator)

## Name

`tuple_str_distance` — Calculate the distance between strings.

## Signature

`def tuple_str_distance(string_1: MaybeSequence[str], string_2: MaybeSequence[str], mode: str) -> Sequence[int]`

`def tuple_str_distance_s(string_1: MaybeSequence[str], string_2: MaybeSequence[str], mode: str) -> int`

## Description

`tuple_str_distance` computes the edit distance between *`string_1`*
and *`string_2`* and returns the result in *`distance`*.
The distance measure used is specified in *`mode`*.
Both input tuples may only consist of strings. Otherwise, `tuple_str_distance`
returns an error.
As an exception, an empty tuple in *`string_1`* or *`string_2`* cause
*`distance`* to also be empty.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each of the input tuples *`string_1`* and *`string_2`*
can be given as a tuple of length *1* or *"N"*.
Parameters with tuple length *1* will be repeated internally
such that the number of computed distances is always *"N"*.

### Supported distance measures

- *"levenshtein"*:
  Uses the Levenshtein distance to quantify string distances. The
  Levenshtein distance is the minimum number of edit operations
  required to transform *`string_1`* into *`string_2`*.
  Valid edit operations are insertion, deletion and replacement of
  characters.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_str_distance`,
which can be used in an expression in the following syntax:

[`Result := str_distance(String1, String2, Mode)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`string_1`** (input_control)  string(-array) `→` MaybeSequence[str]

Input tuple.

Default:
"String1"

**`string_2`** (input_control)  string(-array) `→` MaybeSequence[str]

Input tuple.

Default:
"String2"

**`mode`** (input_control)  string `→` str

Distance measure.

Default:
"levenshtein"

List of values:
"levenshtein"

**`distance`** (output_control)  integer(-array) `→` Sequence[int]

Element-wise string distance.

## Possible Predecessors

`get_text_result`,
`find_text`,
`do_ocr_word_mlp`

## Alternatives

`suggest_lexicon`

## References

Vladimir I. Levenshtein, Binary codes capable of correcting deletions, insertions,
and reversals, Doklady Akademii Nauk SSSR, 163(4):845-848, 1965 (Russian).
English translation in Soviet Physics Doklady, 10(8):707-710, 1966.

## Module

Foundation
