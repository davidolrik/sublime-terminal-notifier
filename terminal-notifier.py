import sublime, sublime_plugin
import subprocess, threading, os, glob

class TerminalNotifierCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        thread = Notify(args)
        thread.start()

class Notify(threading.Thread):
    def __init__(self, args):
        self.args = args
        threading.Thread.__init__(self)

    def run(self):
        # Places to look for terminal-notifier
        paths =[
            os.environ['HOME']+"/bin",
            os.environ['HOME']+"/.rbenv/shims",
            "/usr/local/bin",
            "/opt/local/bin"
        ]
        paths.extend(glob.glob(os.environ['HOME']+"/.rvm/gems/*/bin/terminal-notifier"))
        paths.extend(glob.glob("/usr/local/Cellar/gems/*/bin"))
        paths.extend(os.environ['PATH'].split(":"))

        binary = None
        for path in paths:
            if os.path.isfile(path+"/terminal-notifier") and os.access(path+"/terminal-notifier", os.X_OK):
                binary = path+"/terminal-notifier"
                break

        if binary == None:
            print("terminal-notifier command not found.")
            return

        # Build notify command
        notify_command = [
            binary,
            "-sender",   "com.sublimetext.3",
            "-group",    "sublime_rsync_ssh_" + self.args.get("group", "default"),
            "-title",    self.args.get("title", "Sublime Text"),
            "-message",  self.args.get("message", "This is a notification"),
            "-activate", "com.sublimetext.3"
        ]
        if self.args.get("subtitle"):
            notify_command.extend(["-subtitle", self.args.get("subtitle")])

        # Execute notify command
        try:
            output = subprocess.check_output(notify_command, universal_newlines=True, timeout=10, stderr=subprocess.STDOUT)
        except subprocess.TimeoutExpired as e:
            print("Unable to send notification: "+ e.output)
            print(e.output)
        except subprocess.CalledProcessError as e:
            print(e.output)

        return
