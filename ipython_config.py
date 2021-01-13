c = get_config()
# c.InlineBackend.rc = {}
c.InteractiveShellApp.extensions = ["autoreload"]
c.InteractiveShellApp.exec_lines.append("%autoreload 2")
c.IPCompleter.use_jedi = False
c.InlineBackend.figure_format = "retina"
