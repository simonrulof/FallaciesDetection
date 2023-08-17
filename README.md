TAKE NOTE THAT IT IS ONLY A DEMO, CODE IS FASTLY COMMENTED.


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

## Running

To run the application, you need to first write your ACE sentences in the input file, you can modify this file's name in the config file. By default, this file's name is ACE_SENTENCES.
Each sentence must be on its own line, the last line is considered as the "conclusion" of your argument.

Then you just have to run FallaciesDetection.py and see the result.
