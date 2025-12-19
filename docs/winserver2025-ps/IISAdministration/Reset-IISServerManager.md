---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/reset-iisservermanager?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Reset-IISServerManager
---

# 重置 IISServerManager

## 摘要
重置 IIS ServerManager 中的 IISAdministration 视图。

## 语法

```
Reset-IISServerManager [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Reset-IISServerManager` cmdlet 会将 IIS ServerManager 对象的 IISAdministration 视图以及 `.config` 文件（特别是 `applicationHost.config` 部分）的显示内容重置为 `.config` 文件当前的实际内容。

## 示例

### 示例 1：重置 IISServerManager 视图中的配置信息
```
PS C:\> $Sites = (Get-IISServerManager).Sites
PS C:\> $Sites["default web site"].Attributes["serverAutoStart"]


IsInheritedFromDefaultValue : True
IsProtected                 : False
Name                        : serverAutoStart
Schema                      : Microsoft.Web.Administration.ConfigurationAttributeSchema
Value                       : True


PS C:\> $Sites["default web site"].Attributes["serverAutoStart"].value = $false
PS C:\> $Sites["default web site"].Attributes["serverAutoStart"]


IsInheritedFromDefaultValue : False
IsProtected                 : False
Name                        : serverAutoStart
Schema                      : Microsoft.Web.Administration.ConfigurationAttributeSchema
Value                       : False


PS C:\> Reset-IISServerManager

Confirm
Are you sure you want to perform this action?
Performing the operation "Reset-IISServerManager" on target "ServerManager".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): y
PS C:\> $Sites = (Get-IISServerManager).Sites
PS C:\> $Sites["default web site"].Attributes["serverAutoStart"]


IsInheritedFromDefaultValue : True
IsProtected                 : False
Name                        : serverAutoStart
Schema                      : Microsoft.Web.Administration.ConfigurationAttributeSchema
Value                       : True
```

此命令在修改配置文件（.config）后，会重置 IISServerManager 对该文件的显示设置，并随后验证修改后的值是否已被正确恢复。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您确认是否要继续执行操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。不过实际上这个cmdlet并没有被执行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Get-IISServerManager](./Get-IISServerManager.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

