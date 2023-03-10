<!--
.. title: Automator Quick Action for KDiff3 in Finder
.. slug: custom-action-mac-finder
.. date: 2023-03-10 08:24:11 UTC+05:30
.. tags: macbook, automation
.. category: 
.. link: 
.. description: 
.. type: text
-->

### The need for quick action

kdiff3[^kdiff3] is a diff & merge tool that compares multiple files/directories and shows the difference line by line and character by character as shown below.

<img src="/images/mac-finder-kdiff3.png" alt="mac-finder-kdiff3" />

In Windows, when we select multiple files/directories and right click on them, it will show the option to compare selected items with kdiff3.

<img src="/images/mac-finder-kdiff3-windows.png" alt="mac-finder-kdiff3-windows" />

However, in Macbook, it doesn't show this option. In this tutorial, let us see how we can create the same quick action in the right-click menu when we right-click on the files/directories.


### Creating Quick Action

Let us open Automator[^automator], create new file and select Quick Action.

<img src="/images/mac-finder-quick-action.png" alt="mac-finder-automator" />


On the left side select `Utilities` and then select `Run Shell Script`. 

For Workflow receives current, select `files or folders` and then select `in Finder`. 

<img src="/images/mac-finder-quick-action2.png" alt="mac-finder-quick-action" />


Then select pass input `as agruments` and in the script section let us add the following command.

```bash
/path/to/kdiff3 $1 $2
```

After adding the command, save this Quick Action. 

Now if we relaunch Finder app and then select multiple directories, and right click we can see `Compare with KDiff3` in quick actions.

<img src="/images/mac-finder-kdiff3-quick-action.png" alt="mac-finder-kdiff3" />


### Conclusion

Even though we can use the command line to compare the files/directories, it is always good to have a quick action in the right-click menu. 

[^kdiff3]: [https://kdiff3.sourceforge.io](https://kdiff3.sourceforge.io)

[^automator]: [https://en.wikipedia.org/wiki/Automator_(macOS)](https://en.wikipedia.org/wiki/Automator_(macOS))
