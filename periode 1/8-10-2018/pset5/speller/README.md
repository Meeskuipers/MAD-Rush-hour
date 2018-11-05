# Questions

## What is pneumonoultramicroscopicsilicovolcanoconiosis?

It is the longest word in the english dictionary

## According to its man page, what does `getrusage` do?

TODO

## Per that same man page, how many members are in a variable of type `struct rusage`?

16

## Why do you think we pass `before` and `after` by reference (instead of by value) to `calculate`, even though we're not changing their contents?

You get a lot of copies and that costs a lot of memory

## Explain as precisely as possible, in a paragraph or more, how `main` goes about reading words from a file. In other words, convince us that you indeed understand how that function's `for` loop works.

A for loop is used to read one character at the time until the end of the file. Then it was checked if is was a alpabetical or '. It gives zero if any of the values is a number or misspelled word.

## Why do you think we used `fgetc` to read each word's characters one at a time rather than use `fscanf` with a format string like `"%s"` to read whole words at a time? Put another way, what problems might arise by relying on `fscanf` alone?

strings with number would be fine following fscanf

## Why do you think we declared the parameters for `check` and `load` as `const` (which means "constant")?

the thing the pointer points to can not be changed.
