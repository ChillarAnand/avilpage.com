<!--
.. title: Mastering HammerSpoon - Excel Automation
.. slug: excel-automation-with-hammerspoon-on-mac
.. date: 2023-05-21 18:14:00 UTC+05:30
.. tags: hammerspoon, automation, mac
.. category: 
.. link:
.. description: How to automate Excel and other apps with Hammerspoon on Mac
.. type: text
-->

### Introduction

Recently, I have been using Excel a lot. When opening a new Excel file, I have to do the following:

1. Maximize the window
2. Select all columns and fit them to its width
3. Apply filters to all columns
4. Freeze the first row

When opening and closing multiple Excel files, this becomes a tedious task. So, I decided to automate this and came across Hammerspoon.


### HammerSpoon

Hammerspoon[^hammerspoon] is a powerful automation tool for macOS. It allows you to write Lua scripts to automate various tasks and make our keybindings.

First, let's install Hammerspoon using Homebrew.

```bash
$ brew install hammerspoon
```

We can write our automation script in `~/.hammerspoon/init.lua` file. Let us see how we can automate the above tasks.

### Automating Excel

```lua
-- excel
function excel(appObject)
   local win = hs.window.focusedWindow()
   if (not win) then
      return
   end
    win:maximize()
    
    appObject:selectMenuItem({"Edit", "Select all"})
    appObject:selectMenuItem({"Format", "Column", "Autofit Selection"})
    appObject:selectMenuItem({"Data", "Auto-filter"})

end)


function applicationWatcher(appName, eventType, appObject)
   local w = hs.application.watcher
   if (eventType == w.activated or eventType == w.launched) then
      if (appName == "Microsoft Excel") then
         excel(appObject)
      end
   end
end
```

This script will watch for application events and when Excel is launched or activated, it will call the `excel` function. 

The `excel` function will maximize the window, select all columns and fit them to it's width, apply filters to all columns.

`Free top row` option is not available in the standard menu. So, I have added it to the quick access toolbar and click it via mouse event.


### Conclusion

Hammerspoon is a powerful tool for various automation tasks. In addition to that it can replace a lot of utility apps like CheatSheet, BlueSnooze[^bluesnooze], Rectangle, ShiftIT[^shiftit], HotKey etc. I have replaced most of the utility apps with Hammerspoon, and it is working great. I will be writing about it in detail in the upcoming posts.


[^hammerspoon]: [https://github.com/Hammerspoon/hammerspoon](https://github.com/Hammerspoon/hammerspoon)

[^bluesnooze]: [https://github.com/odlp/bluesnooze](https://github.com/odlp/bluesnooze)

[^shiftit]: [https://github.com/fikovnik/ShiftIt](https://github.com/fikovnik/ShiftIt)
