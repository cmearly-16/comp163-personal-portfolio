# comp163-personal-portfolio
A personal portfolio repository for course work.

## Troubleshooting: "git" not recognized on Windows

If you see "git: The term 'git' is not recognized..." in PowerShell, Git is likely installed but not on your PATH for the current session or system-wide. Quick fixes:

- Temporary (current PowerShell session):

	Use the PowerShell call operator to run Git directly and add Git to the session PATH:

	& "C:\Program Files\Git\cmd\git.exe" --version
	$env:Path += ";C:\Program Files\Git\cmd"

- Permanent (recommended):

	1. Open Start → Settings → System → About → Advanced system settings → Environment Variables.
	2. Under "System variables", edit `Path` and add `C:\Program Files\Git\cmd` (or your Git install path).
	3. Restart PowerShell / terminals.

If Git is not installed, download and install Git for Windows from https://git-scm.com/download/win and follow the installer prompts (choose to add Git to PATH during install).

After this, `git --version`, `git init`, and other git commands should work from PowerShell.

