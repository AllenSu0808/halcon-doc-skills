# get_chapter_info (Operator)

## Name

`get_chapter_info` — Get information concerning the chapters on operators.

## Signature

`get_chapter_info( : : Chapter : Info)`

## Description

The operator `get_chapter_info` gives information concerning the chapters
on operators. If instead of *`Chapter`* the empty string is transmitted, the
routine will provide in *`Info`* the names of all chapters.
If on the other hand a certain chapter or a chapter and its subchapter(s) are indicated
(by a tuple of names), the corresponding subchapters or - in case there are no
further subchapters - the names of the corresponding operators will be given.
The organization of the chapters on operators is the same as the organization of chapters
and subchapters in the HALCON-manual.
Please note: The chapters on operators respectively the subchapters concerning an
individual operator can be called by using the operator
`get_operator_info(::<Name>,'chapter',Info:)`.
The Online-texts will be taken from the files `operators_[LANG].ref`,
`operators_[LANG].sta`, `operators_[LANG].key`,
`operators_[LANG].num` and `operators_[LANG].idx`
, which will be searched by HALCON in the currently used
directory or the directory 'help_dir' (see also [`get_system`](get_system.md) and
[`set_system`](set_system.md)).

## Attention

The encoding of the result is UTF-8.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Chapter`** (input_control)  string(-array) `→`  (string)

Operator class or subclass of interest.

Default:
''

**`Info`** (output_control)  string-array `→`  (string)

Operator classes (*`Chapter`* = ”) or
operator subclasses respectively operators.

## Result

If the parameter values are correct and the helpfile
is available, the operator `get_chapter_info` returns the
value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`get_system`,
`set_system`

## See also

`get_operator_info`,
`get_system`,
`set_system`

## Module

Foundation
