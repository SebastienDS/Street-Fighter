from cx_Freeze import setup, Executable

buildOptions = dict(include_files = ['image/', 'hit_box/', 'son/', 'replay/', 'record.txt']) 


setup(
	name = "Street Fighter",
	version = "0.1",
	description = "",
	options = dict(build_exe = buildOptions),
	executables = [Executable("game.py", base = "Win32GUI")]
)
