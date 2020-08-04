# CCC Practice

This repository contains all of my **CCC practice**, completed in Python (so far, only the junior section). It is divided into years, then problems, and also contains the input and its corresponding output file.

## Checker

It also contains a helpful checker.py script that can be used to check the CCC problems. Here is how to set up and use the checker.py script.

**1. Clone the repository**

<code>$ git clone https://github.com/vishnupsatish/CCC-practice/</code>

**2. Run the checker.py script**

<code>$ python path/to/script/checker.py</code>

The next part is optional, only if you want to create a shortcut to the script.

**3. Open bash profile and add source to bashrc**

<code>open ~/.bash_profile</code>

Add the following to the end of the bash profile file.

<code>source ~/.bashrc</code>

**4. Open bashrc**

<code>open ~/.bashrc</code>

**5. Add alias for checker script**

Add the following to the end of the bashrc file.

<code>alias check_ccc='cd /path/to/CCC-practice && python checker.py'</code>

**6. Run**

Now, you have finished creating the alias. Restart the Terminal, and type

<code>check_ccc</code>

You will be prompted on the years and problems you want to check, and the checker.txt file will be updated accordingly.

## Contribute

Please help add any CCC problems you have done.