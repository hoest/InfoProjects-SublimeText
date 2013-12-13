import os, sublime, sublime_plugin

class BuildProjectCommand(sublime_plugin.WindowCommand):
  def run(self, deploy=False):
    self.deploy = deploy

    if self.deploy:
      self.on_done()
    else:
      sublime.status_message("Commands like: 'less', 'csslint' or 'less,coffee'")
      self.window.show_input_panel("Build command", "", self.on_done, None, None)

  def on_done(self, buildcmd="all"):
    sublime.status_message("")
    working_dir = os.path.dirname(os.path.abspath("."))
    psscript = "Invoke-Build%s.ps1" % "Develop" if self.deploy else ""

    if "\\src\\" in working_dir:
      cmd = {
        "cmd": ["powershell", "-NoLogo", psscript, "-p", buildcmd],
        "working_dir": working_dir
      }

      self.window.run_command("exec", cmd)
    else:
      sublime.status_message("You need to edit an InfoProjects-project")
