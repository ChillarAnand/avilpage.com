<--
.. title: Split/Merge PDF Files From Command Line
.. slug: split-merge-stitch-pdf-file-ubuntu
.. date: 2014-05-07 13:44:00
.. category: programming, linux
.. tags: command-line
.. description: A simple way to split & merge multiple pdf files with pdf tool kit in linux terminal.
-->

### Introduction

Sometimes we come across a situation where we need to split or stitch the pdf document. The simplest and easiest way is to use PDF Toolkit on the command line.

Let's first install it using the following command:

```shell
$ sudo apt-get install pdftk
```

Now that pdftk is installed, lets take a smaple pdf file and split it into parts.

### Splitting PDF

We can split the entire pdf into single pages using the following command:

```shell
$ pdftk myFile.pdf burst
```

We can also split only specific page by specifying the page number:

```shell
$ pdftk myFile.pdf cat 21 output page_21.pdf
```

You can also split specific set of pages by using the following command:

```shell
$ pdftk myFile.pdf cat  21-end output 21_to_last.pdf
```

### Merging PDF

Now that we have scissored a lot of pages. Let's go ahead and stitch a few of them.

We can merge specific pages by using the following command:

```shell
$ pdftk page_21.pdf 21_to_end.pdf cat output stitched.pdf
```

This will stitch the two pdf's we created above.

If we have a huge list of single age pdf's in a folder and if we want to stitch them together, we can run the following command.

```shell
$ pdftk *.pdf cat output newFile.pdf
```

This will stitch all the pdf in the current directory to a single pdf.

### Conclusion

That's it. We have successfully split and merged pdf files using pdftk. Hope you find this useful.
