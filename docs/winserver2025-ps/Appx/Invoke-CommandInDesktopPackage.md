---
description: 这是一个调试工具，它会在已打包的应用程序的上下文中创建一个新的进程。
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-Help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/invoke-commandindesktoppackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Invoke-CommandInDesktopPackage
---

# 在桌面应用程序包中调用命令

## 摘要
这是一个调试工具，它会在已打包的应用程序的上下文中创建一个新的进程。

## 语法

```
Invoke-CommandInDesktopPackage [-PackageFamilyName] <String> [-AppId] <String>
 [-Command] <String> [[-Args] <String>] [-PreventBreakaway] [<CommonParameters>]
```

## 描述

`Invoke-CommandInDesktopPackage` 会在提供的 **PackageFamilyName** 和 **AppId** 的上下文中创建一个新的进程。

创建的进程将拥有所提供的 **AppId** 的身份，并能够访问其虚拟化的文件系统和注册表（如果有的话）。新进程将获得一个令牌，该令牌与真实的 **AppId** 进程相似，但不完全相同。

这个命令的主要用途是在已打包的应用程序的上下文中调用调试或故障排除工具，以访问其虚拟化资源。例如，你可以运行注册表编辑器来查看虚拟化的注册表键，或者使用记事本来读取虚拟化的文件。请注意：某些工具（如注册表编辑器）需要管理员权限才能正常使用。

对于所创建进程的行为，我们不提供任何保证（除了该进程具有相应的包标识以及对该包的虚拟化资源的访问权限）。特别需要注意的是：即使通常情况下带有 **AppId** 的进程会被创建在 AppContainer 中，新进程也不会被创建在 AppContainer 内。诸如隐私控制或其他应用设置等功能可能适用于新进程，也可能不适用。你不应该依赖于使用此命令所产生的一些特定副作用，因为这些副作用是未定义的，并且可能会发生变化。

## 示例

### 示例 1：调用记事本来读取虚拟化文件

以下命令会在 `Contoso.MyApp` 包中的 `ContosoApp` 应用程序的上下文中调用记事本（Notepad）。这使您能够访问存储在应用程序虚拟文件系统中的资源，例如日志文件或配置文件。

```powershell
$params = @{
    AppId             = 'ContosoApp'
    PackageFamilyName = 'Contoso.MyApp_abcdefgh23456'
    Command           = 'notepad.exe'
}
Invoke-CommandInDesktopPackage @params
```

## 参数

### -AppId

**AppId** 是目标包清单（manifest）中的应用程序ID。

例如，在这个清单片段中，`MyAppName` 就是应用程序的标识符（Application ID）。

`<Application Id="MyAppName" ... />`

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Args

可以传递给新进程的可选参数。例如：`/foo /bar`。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Command

一个可执行的程序，类似于 `regedit.exe`。

请注意，如果可执行文件需要提升权限（例如 `regedit`），则必须从已经具有提升权限的上下文中调用 `Invoke-CommandInDesktopPackage`。如果从没有提升权限的上下文中调用 `Invoke-CommandInDesktopPackage`，则无法按预期正常工作。新的进程将在没有相应的包上下文的情况下创建，从而导致 PowerShell 命令执行失败。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -PackageFamilyName

目标软件包所属的软件包系列名称。您可以通过调用 [Get-AppxPackage](./Get-AppxPackage.md) 命令来获取该信息。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -PreventBreakaway

该选项会确保被调用进程的所有子进程也在 **AppId** 的上下文中创建。默认情况下，子进程是在没有任何上下文的情况下创建的。这个开关对于运行 `cmd.exe` 非常有用，因为它允许你在包的上下文中启动其他多个工具。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 5
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Get-AppxPackage](./Get-AppxPackage.md)
