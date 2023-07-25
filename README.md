TAKE NOTE THAT IT IS ONLY A DEMO, CODE IS FASTLY COMMENTED.
IT WILL BE UPDATED TO FIX BUGS DURING THIS WEEK


# Fallacies Detection

Fallacies Detection is a small project to detect possible fallacies in an [Attempto Controlled English (APE)](http://attempto.ifi.uzh.ch/site/) argument.

## Introduction

Note that all the tests so far has been made from a fresh re-installed Ubuntu 22.04, it should work on MacOS but no tests has been done.
Fallacies Detection uses [ACE parser (APE)](https://github.com/Attempto/APE) in order to use ACE. To avoid confusion, the installation process of APE and its needs will be shown below.

## Installation

To run APE (which is needed for FallaciesDetection) you need a recent version of SWI-Prolog.
SWI-Prolog is free software and can be downloaded from <http://www.swi-prolog.org>. Note that you
minimally need to install the following SWI Prolog packages: `clib`, `sgml`, and `http`. To view
the documentation embedded in the source files you also need `pldoc`.

Note that the lexicon used for APE is not the basic one you get on the APE's github. it is instead a [Large lexicon for APE](https://github.com/Attempto/Clex).

Then you have to compile the APE. Go in the APE folder and run the command `make install`. 
The APE installation process is finished if you don't see any compilation error and if a new file `ape.exe` appeared in the APE folder.
