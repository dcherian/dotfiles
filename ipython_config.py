c = get_config()
c.InlineBackend.rc = {}
c.InteractiveShellApp.extensions = ['autoreload']
c.InteractiveShellApp.exec_lines = []
c.InteractiveShellApp.exec_lines.append('%load_ext autoreload')
c.InteractiveShellApp.exec_lines.append('%autoreload 2')
