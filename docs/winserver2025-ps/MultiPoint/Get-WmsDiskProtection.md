---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/get-wmsdiskprotection?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WmsDiskProtection
---

# Get-WmsDiskProtection

## 摘要
获取磁盘保护功能的当前状态和配置信息。

## 语法

```
Get-WmsDiskProtection [-Server <String>] [<CommonParameters>]
```

## 描述
`Get-WmsDiskProtection` cmdlet 可以获取磁盘保护功能的当前配置状态。该配置状态可以是 “Not Installed”（未安装）、”Discard”（已丢弃）或 “Passive”（被动模式）。

## 示例

### 示例 1：获取本地计算机的磁盘保护配置
```
PS C:\> Get-WmsDiskProtection
Discard
```

该命令会返回本地计算机上磁盘保护功能的当前状态。

### 示例 2：获取指定计算机的磁盘保护配置信息
```
PS C:\> Get-WmsDiskProtection -Server "Sample.microsoft.com"
Passive
```

该命令返回指定计算机上磁盘保护功能的当前状态。

## 参数

### -Server
指定该命令的目标——即多点服务器（MultiPoint Server）的完全限定主机名。默认值为“localhost”。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ComputerName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### Microsoft.WindowsServerSolutions.MultipointServer POWERShellcommands.Library.DiskProtectionMode

**DiskProtectionMode** 对象是一个枚举类型，包含三个值之一，这些值反映了磁盘保护功能的当前模式。可能的值有：NotInstalled（未安装）、Discard（丢弃）和 Passive（被动模式）。

## 备注

## 相关链接

[ Disable-WmsDiskProtection](./Disable-WmsDiskProtection.md)

[Enable-WmsDiskProtection](./Enable-WmsDiskProtection.md)

[ Resume-WmsDiskProtection](./Resume-WmsDiskProtection.md)

[暂停 WMS 磁盘保护功能](./Suspend-WmsDiskProtection.md)

