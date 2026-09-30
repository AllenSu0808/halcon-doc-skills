# GetChapterInfo (Operator)

## Name

`GetChapterInfo` — Get information concerning the chapters on operators.

## Signature

`static void HOperatorSet.GetChapterInfo(HTuple chapter, out HTuple info)`

`static HTuple HInfo.GetChapterInfo(HTuple chapter)`

`static HTuple HInfo.GetChapterInfo(string chapter)`

## Description

The operator `GetChapterInfo` gives information concerning the chapters
on operators. If instead of *`chapter`* the empty string is transmitted, the
routine will provide in *`info`* the names of all chapters.
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
directory or the directory 'help_dir' (see also [`GetSystem`](get_system.md) and
[`SetSystem`](set_system.md)).

## Attention

The encoding of the result is UTF-8.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`chapter`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Operator class or subclass of interest.

Default:
""

**`info`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Operator classes (*`chapter`* = ”) or
operator subclasses respectively operators.

## Result

If the parameter values are correct and the helpfile
is available, the operator `GetChapterInfo` returns the
value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`GetSystem`,
`SetSystem`

## See also

`GetOperatorInfo`,
`GetSystem`,
`SetSystem`

## Module

Foundation
