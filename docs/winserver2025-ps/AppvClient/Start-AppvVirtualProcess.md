---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: AppVClientCmdlets-help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/start-appvvirtualprocess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-AppvVirtualProcess
---

# 启动 AppVVirtualProcess 进程

## 摘要
启动一个虚拟进程。

## 语法

### 默认值（Default）
```
Start-AppvVirtualProcess [-FilePath] <String> [[-ArgumentList] <String[]>] [-Credential <PSCredential>]
 [-WorkingDirectory <String>] [-LoadUserProfile] [-NoNewWindow] [-PassThru] [-RedirectStandardError <String>]
 [-RedirectStandardInput <String>] [-RedirectStandardOutput <String>] [-Wait] [-UseNewEnvironment]
 -AppvClientObject <Object> [<CommonParameters>]
```

### 使用 ShellExecute
```
Start-AppvVirtualProcess [-FilePath] <String> [[-ArgumentList] <String[]>] [-WorkingDirectory <String>]
 [-PassThru] [-Verb <String>] [-Wait] [-WindowStyle <ProcessWindowStyle>] -AppvClientObject <Object>
 [<CommonParameters>]
```

## 描述
`Start-AppvVirtualProcess` cmdlet 用于启动一个新的虚拟进程。

## 示例

#### 示例 1：在某个软件包的虚拟环境中启动一个虚拟进程
```
PS C:\> $AppVObj = Get-AppvClientPackage -Name "MyPackage"
PS C:\> Start-AppvVirtualProcess -FilePath "C:\Calc.exe" -AppvClientObject $AppVObj
```

第一个命令使用 **Get-AppvClientPackage** cmdlet 获取名为 “MyPackage” 的客户端包，并将结果存储在 `$AppVObj` 变量中。

第二个命令会在 `$AppVObj` 的虚拟环境中为 `Calc.exe` 启动一个新的虚拟进程。

### 示例 2：在连接组的虚拟环境中启动一个虚拟进程
```
PS C:\> $AppVObj = Get-AppvClientConnectionGroup -Name MyConnectionGroup
PS C:\> Start-AppvVirtualProcess -FilePath "C:\Calc.exe" -AppvClientObject $AppVObj
```

第一个命令使用 **Get-AppvClientConnectionGroup** cmdlet 获取名为 “MyPackage” 的客户端软件包，并将结果存储在 $AppVObj 变量中。

第二个命令会在 `$AppVObj` 的虚拟环境中为 `Calc.exe` 启动一个新的虚拟进程。

## 参数

### -AppvClientObject
指定一个 **AppvClientPackage** 或 **AppvClientConnectionGroup** 对象。

```yaml
Type: Object
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ArgumentList
指定要传递给虚拟进程的参数。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: Args

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定用于启动此过程的凭据。

```yaml
Type: PSCredential
Parameter Sets: Default
Aliases: RunAs

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FilePath
指定一个文件路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases: PSPath

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LoadUserProfile
表示该cmdlet加载了一个用户配置文件，以便在过程中使用。

```yaml
Type: SwitchParameter
Parameter Sets: Default
Aliases: Lup

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoNewWindow
表示该cmdlet会尝试将进程保持在同一个窗口中，而不是打开一个新的窗口。

```yaml
Type: SwitchParameter
Parameter Sets: Default
Aliases: nnw

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RedirectStandardError
将标准错误（stderr）重定向到指定的文件中。

```yaml
Type: String
Parameter Sets: Default
Aliases: RSE

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RedirectStandardInput
从指定的文件中读取标准输入（stdinput）。

```yaml
Type: String
Parameter Sets: Default
Aliases: RSI

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RedirectStandardOutput
将标准输出（stdout）重定向到指定的文件中。

```yaml
Type: String
Parameter Sets: Default
Aliases: RSO

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseNewEnvironment
表示此cmdlet在运行过程中使用了新的环境设置。

```yaml
Type: SwitchParameter
Parameter Sets: Default
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Verb
为该过程指定一个动词（即执行操作的命令或动作）。

```yaml
Type: String
Parameter Sets: UseShellExecute
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Wait
这表示该cmdlet使用虚拟进程的同步操作方式。在执行完命令后，该cmdlet会一直等待直到虚拟进程完全终止才会结束自身的执行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WindowStyle
指定在没有“进程窗口样式”（Process Window Style）的情况下应执行的操作。该参数的可接受值为：

- Normal.
Display the normal window.
- Hidden.
Launch a hidden window.
- Minimized.
Launch a minimized window.
- Maximized.
Launch a maximized window.

默认值是“Normal”。

```yaml
Type: ProcessWindowStyle
Parameter Sets: UseShellExecute
Aliases:
Accepted values: Normal, Hidden, Minimized, Maximized

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WorkingDirectory
指定进程的工作目录。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-AppvClientConnectionGroup](./Get-AppvClientConnectionGroup.md)

[Get-AppvClientPackage](./Get-AppvClientPackage.md)

[Get-AppvVirtualProcess](./Get-AppvVirtualProcess.md)

