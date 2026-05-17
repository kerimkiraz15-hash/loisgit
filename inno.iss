[Setup]
AppName=Loisgit
AppVersion=1.1
DefaultDirName={localappdata}\Loisgit
DefaultGroupName=Loisgit

ChangesEnvironment=yes
PrivilegesRequired=lowest


[Tasks]
Name: "desktopicon"; Description: "Desktop Shortcut erstellen"; GroupDescription: "Extras:"

[Files]
Source: "dist\loisgit.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autodesktop}\Loisgit"; Filename: "{app}\loisgit.exe"; Tasks: desktopicon

[Code]
procedure CurStepChanged(CurStep: TSetupStep);
var
  OldPath: String;
begin
  if CurStep = ssPostInstall then
  begin
    RegQueryStringValue(HKEY_CURRENT_USER, 'Environment', 'Path', OldPath);
    RegWriteStringValue(HKEY_CURRENT_USER, 'Environment', 'Path', OldPath + ';' + ExpandConstant('{app}'));
  end;
end;