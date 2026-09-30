# MakeDir (Operator)

## Name

`MakeDir` — Make a directory.

## Signature

`static void HOperatorSet.MakeDir(HTuple dirName)`

`static void HMisc.MakeDir(string dirName)`

## Description

`MakeDir` creates the directory given by *`dirName`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dirName`** (input_control)  filename.dir `→` [HTuple](HTuple.md) (*string*)

Name of directory to be created.

## Result

`MakeDir` returns the value 2 (
H_MSG_TRUE)
if the directory
could be created. Otherwise, an exception is raised.

## Module

Foundation
