# Sublime Terminal Notifier

Let Sublime Text post notifications to the Notification Center on [OS X](http://www.apple.com/osx/).

## Description

This plugin is a utility plugin for other plugins that wants to post notifications to the user.

## Features

The plugin provides you with one command: `terminal_notifier`, which you call in your plugin code like this:

```python
import sublime
sublime.active_window().run_command("terminal_notifier", {
    "title": "Something happened",
    "subtitle": "Over there",
    "message": "This is a nice notification."
})
```

## Install

You first need to install the terminal-notifier gem:

    gem install terminal-notifier

Then you install this plugin either by cloning this project directly, or by installing it via the excellent [Package Control](https://sublime.wbond.net) plugin.

## License

&copy; 2013 David Olrik <david@olrik.dk>.

This is free software. It is licensed under the [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/). Feel free to use this package in your own work. However, if you modify and/or redistribute it, please attribute me in some way, and distribute your work under this or a similar license.
