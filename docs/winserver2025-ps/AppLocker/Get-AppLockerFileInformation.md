---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Security.ApplicationId.PolicyManagement.Cmdlets.dll-Help.xml
Module Name: AppLocker
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/applocker/get-applockerfileinformation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppLockerFileInformation
---

# 获取 AppLocker 文件信息

## 摘要
从文件列表或事件日志中获取创建 AppLocker 规则所需的文件信息。

## 语法

### ByFilePath（默认值）
```
Get-AppLockerFileInformation [[-Path] <System.Collections.Generic.List`1[System.String]>] [<CommonParameters>]
```

### 作者：ByAppx
```
Get-AppLockerFileInformation
 [[-Packages] <System.Collections.Generic.List`1[Microsoft.Windows.Appx.PackageManager.Commands.AppxPackage]>]
 [<CommonParameters>]
```

### 按目录（ByDirectory）
```
Get-AppLockerFileInformation -Directory <String>
 [-FileType <System.Collections.Generic.List`1[Microsoft.Security.ApplicationId.PolicyManagement.PolicyModel.AppLockerFileType]>]
 [-Recurse] [<CommonParameters>]
```

### ByEventLog
```
Get-AppLockerFileInformation [-EventLog] [-LogPath <String>]
 [-EventType <System.Collections.Generic.List`1[Microsoft.Security.ApplicationId.PolicyManagement.Cmdlets.AppLockerEventType]>]
 [-Statistics] [<CommonParameters>]
```

## 描述
`Get-AppLockerFileInformation` cmdlet 可以从文件列表或事件日志中获取 AppLocker 文件的相关信息。这些信息包括文件的发布者信息、文件哈希值以及文件路径。

事件日志中的文件信息可能不包含所有的发布者信息、文件哈希值以及文件路径字段。未经过签名的文件将没有任何发布者相关信息。

## 示例

### 示例 1：获取.exe 文件和脚本的文件信息
```
PS C:\> Get-AppLockerFileInformation -Directory C:\Windows\system32\ -Recurse -FileType exe, script
```

这个示例会获取 `%windir%\system32` 目录下所有 `.exe` 文件和脚本的文件信息。

### 示例 2：获取文件的文件信息
```
PS C:\> Get-AppLockerFileInformation -Path "C:\Program Files (x86)\Internet Explorer\iexplore.exe" | Format-List
Path      : %PROGRAMFILES%\INTERNET EXPLORER\IEXPLORE.EXE
Publisher : CN=WINDOWS MAIN BUILD LAB ACCOUNT\WINDOWS® INTERNET EXPLORER\IEXPLORE.EXE,10.0.8421.0
Hash      : SHA256 0x5F374C2DD91A6F9E9E96F149EE221EC0454649F50E1AF6D3DAEFB849FB7C551C
AppX      : False


PS C:\> Get-AppLockerFileInformation -Path "C:\Program Files\Internet Explorer\iexplore.exe" | Format-List
Path      : %PROGRAMFILES%\INTERNET EXPLORER\IEXPLORE.EXE
Publisher : CN=WINDOWS MAIN BUILD LAB ACCOUNT\WINDOWS® INTERNET EXPLORER\IEXPLORE.EXE,10.0.8421.0
Hash      : SHA256 0x5F374C2DD91A6F9E9E96F149EE221EC0454649F50E1AF6D3DAEFB849FB7C551C
AppX      : False
```

这个示例会获取由路径指定的文件的文件信息。

### 示例 3：获取所有用户安装的所有应用程序的文件信息
```
PS C:\> Get-AppXPackage -AllUsers | Get-AppLockerFileInformation
Path      : windows.immersivecontrolpanel_6.2.0.0_neutral_neutral_cw5n1h2txyewy.appx
Publisher : CN=Microsoft Windows, O=Microsoft Corporation, L=Redmond, S=Washington,
            C=US\windows.immersivecontrolpanel\APPX,6.2.0.0
Hash      :
AppX      : True

Path      : windows.RemoteDesktop_1.0.0.0_neutral_neutral_cw5n1h2txyewy.appx
Publisher : CN=Microsoft Windows, O=Microsoft Corporation, L=Redmond, S=Washington,
            C=US\windows.RemoteDesktop\APPX,1.0.0.0
Hash      :
AppX      : True

Path      : WinStore_1.0.0.0_neutral_neutral_cw5n1h2txyewy.appx
Publisher : CN=Microsoft Windows, O=Microsoft Corporation, L=Redmond, S=Washington, C=US\WinStore\APPX,1.0.0.0
Hash      :
AppX      : True
```

这个示例会输出该计算机上为所有用户安装的所有打包应用程序的文件信息。

### 示例 4：获取已审核事件的文件信息
```
PS C:\> Get-AppLockerFileInformation -EventLog -EventType Audited
```

这个示例会输出本地事件日志中所有经过审核的事件的文件信息。这些被审核的事件对应于 AppLocker 审计日志中的“警告”级别事件。

### 示例 5：获取允许事件的统计数据
```
PS C:\> Get-AppLockerFileInformation -EventLog -EventType Allow -Statistics
```

这个示例显示了本地事件日志中所有允许发生的事件的统计信息。对于事件日志中的每个文件，该 cmdlet 会统计该事件类型出现的次数总和。

### 示例 6：创建一个 AppLocker 策略
```
PS C:\> Get-AppLockerFileInformation -EventLog -EventType Audited | New-AppLockerPolicy -RuleType Publisher, Hash, Path -User Everyone -Optimize | Set-AppLockerPolicy -LDAP LDAP://TestGPO
```

这个示例根据本地事件日志中的警告事件创建一个新的AppLocker策略，并将该策略应用到一个测试组策略对象（Group Policy Object，简称GPO）上。

## 参数

### -Directory
指定包含需要获取文件信息的文件的目录。如果需要搜索指定目录中的所有子文件夹和文件，请添加 *Recurse* 参数。

```yaml
Type: String
Parameter Sets: ByDirectory
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EventLog
指定文件信息是从事件日志中获取的。

```yaml
Type: SwitchParameter
Parameter Sets: ByEventLog
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EventType
指定用于过滤事件的事件类型。该参数的允许值包括：Allowed（允许）、Denied（拒绝）或Audited（审计）。这些事件类型对应于AppLocker事件日志中的信息性（Informational）、错误性（Error）和警告性（Warning）级别的事件。

```yaml
Type: System.Collections.Generic.List`1[Microsoft.Security.ApplicationId.PolicyManagement.Cmdlets.AppLockerEventType]
Parameter Sets: ByEventLog
Aliases:
Accepted values: Allowed, Denied, Audited

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FileType
指定要搜索的通用文件类型。所有具有相应文件扩展名的文件都将被包括在内。此参数的可接受值为：

- Exe
- Dll
- WindowsInstaller
- Script
- Appx.

```yaml
Type: System.Collections.Generic.List`1[Microsoft.Security.ApplicationId.PolicyManagement.PolicyModel.AppLockerFileType]
Parameter Sets: ByDirectory
Aliases:
Accepted values: Exe, Dll, WindowsInstaller, Script, Appx

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LogPath
Specifies the log name or file path of the event log where the AppLocker events are located.
By default, if this parameter is not specified, the local Microsoft-Windows-AppLocker/EXE and DLL channel is used.

```yaml
Type: String
Parameter Sets: ByEventLog
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Packages
Specifies a list of installed packaged applications, from which the file information is retrieved.

```yaml
Type: System.Collections.Generic.List`1[Microsoft.Windows.Appx.PackageManager.Commands.AppxPackage]
Parameter Sets: ByAppx
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Path
指定用于获取文件信息的文件路径列表。支持正则表达式。

```yaml
Type: System.Collections.Generic.List`1[System.String]
Parameter Sets: ByFilePath
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Recurse
指定将对指定目录中的所有文件和文件夹进行搜索。

```yaml
Type: SwitchParameter
Parameter Sets: ByDirectory
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Statistics
指定要从事件日志中包含的文件中检索哪些统计信息。根据指定的参数，计算文件在事件日志中出现的次数总和（即简单的计数结果）。

```yaml
Type: SwitchParameter
Parameter Sets: ByEventLog
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.security.ApplicationId.PolicyManagement.PolicyModel.FileInformation

### System.String

## 备注

## 相关链接

[Get-AppLockerPolicy](./Get-AppLockerPolicy.md)

[新应用锁策略](./New-AppLockerPolicy.md)

[Set-AppLockerPolicy](./Set-AppLockerPolicy.md)

[Test-AppLockerPolicy](./Test-AppLockerPolicy.md)

