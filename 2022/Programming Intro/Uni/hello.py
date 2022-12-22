#
# hello.py
# Charlie Morrison
# 4 DEC 22
#
# This is a university project for 'Introduction to Porgramming'
#

import sys

message ="Hello\n"
message+="world!"

message+="\n"

message += '''                 '
            *          .
                   *       '
              *                *'''

message += "\n\nHello, my name is Charlie.\nI have chosen the dataset title 'Power consumption of Tetouan city Data Set,' since I find that electricity is something we utilise every single day no matter who we are, and eventually leading into a system which will hopefully analyse this data will certainly have some interesting results."
message += "\nI have programmed previously in my life, I haven't for quite some time but it is good to see that the base rules still haven't changed."
message += "\nThe ASCII art surrounding this wall of text is space themed. I find the vastness of space pure and fascinating. \n\n"

message += '''   *   '*
           *
                *
                       *
               *
                     *

         .                      .
         .                      ;
         :                  - --+- -
         !           .          !
         |        .             .
        _|_         +
      ,' | `.
--- --+-<#>-+- ---  --  -
      `._|_,'
         T
         |
         !
         :         . : 
         .       *'''

sys.stdout.write(message)