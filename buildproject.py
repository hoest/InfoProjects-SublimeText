import os, sublime, sublime_plugin

class BuildProjectCommand(sublime_plugin.WindowCommand):
  def run(self, deploy=False, cleanup=False):
    self.cleanup = cleanup
    self.deploy = deploy

    if self.deploy:
      self.on_done()
    else:
      sublime.status_message("Commands like: 'less', 'csslint' or 'less,coffee'")
      self.window.show_input_panel("Build command", "", self.on_done, None, None)

  def on_done(self, buildcmd="all"):
    sublime.status_message("")
    working_dir = os.path.dirname(self.view.file_name())
    psscript = "Invoke-Build%s.ps1" % "Develop" if self.deploy else ""
    psargs = "-p%s" % " -k" if not self.cleanup else ""

    if "\\src\\" in working_dir:
      cmd = {
        "cmd": ["powershell", "-NoLogo", psscript, psargs, buildcmd],
        "working_dir": working_dir
      }

      self.window.run_command("exec", cmd)
    else:
      sublime.status_message("You need to edit an InfoProjects-project")
