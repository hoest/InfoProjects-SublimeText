import os
import sublime
import sublime_plugin

class BuildProjectCommand(sublime_plugin.WindowCommand):
  def run(self, deploy=False, cleanup=False):
    self.cleanup = cleanup
    self.deploy = deploy
    self.view = self.window.active_view()

    if self.deploy:
      self.on_done()
    else:
      sublime.status_message("Commands like: 'less', 'csslint' or 'less,coffee'")
      self.window.show_input_panel("Build command", "", self.on_done, None, None)

  def on_done(self, buildcmd="all"):
    sublime.status_message("")
    working_dir = os.path.dirname(self.view.file_name())

    psscript = "Invoke-Build.ps1"
    if self.deploy:
      psscript = "Invoke-BuildDevelop.ps1"

    psargs = "-p"
    if self.deploy and not self.cleanup:
      psargs += " -k"

    if "\\src\\" in working_dir:
      cmd = {
        "cmd": ["powershell", "-NoLogo", psscript, psargs, buildcmd],
        "working_dir": working_dir
      }

      self.window.run_command("exec", cmd)
    else:
      sublime.status_message("You need to edit an InfoProjects-project")
