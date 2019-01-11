c = get_config()
c.InlineBackend.rc = {}
c.InteractiveShellApp.extensions = [
    'autoreload',
    'line_profiler',
    'memory_profiler']
c.InteractiveShellApp.exec_lines.append('%autoreload 2')
c.InteractiveShellApp.exec_lines.append('%matplotlib qt')
