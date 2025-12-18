---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BitLocker-help.xml
Module Name: BitLocker
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitlocker/disable-bitlockerautounlock?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-BitLockerAutoUnlock
---

# 禁用BitLocker自动解锁功能

## 摘要
禁用BitLocker卷的自动解锁功能。

## 语法

```
Disable-BitLockerAutoUnlock [-MountPoint] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Disable-BitLockerAutoUnlock` 这个 cmdlet 用于禁用由 BitLocker 磁盘加密保护的卷的自动解锁功能。该 cmdlet 会删除存储在运行操作系统的卷上的、用于指定卷的自动解锁密钥。

您可以配置 BitLocker，使其自动解锁那些未安装操作系统的卷。当用户解锁了操作系统所在的卷之后，BitLocker 会利用存储在注册表和卷元数据中的加密信息来访问那些支持自动解锁功能的 数据卷。

您可以通过驱动器字母来指定某个卷，或者直接指定一个 BitLocker 卷对象。在使用 **Disable-BitLocker** cmdlet 禁用 BitLocker 之前，必须先删除自动解锁密钥。您还可以使用 **Clear-BitLockerAutoUnlock** cmdlet 来删除所有配置为使用自动解锁功能的卷的密钥，而不仅仅是指定的某个卷。

有关 BitLocker 的概述，请参阅 TechNet 上的 [BitLocker 驱动器加密概述](https://technet.microsoft.com/en-us/library/cc732774.aspx)。

## 示例

### 示例 1：禁用某个卷的自动解锁功能
```
PS C:\> Disable-BitLockerAutoUnlock -MountPoint "E:"
```

此命令将禁用指定 BitLocker 卷的自动解锁功能。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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

### -MountPoint
用于指定一组驱动器字母或 BitLocker 卷对象。该cmdlet会禁用所指定卷的自动解锁功能。若要获取 BitLocker 卷对象，请使用 **Get-BitLockerVolume** cmdlet。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。不过实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### BitLockerVolume[], String[]

## 输出

### BitLockerVolume[]

## 备注

## 相关链接

[Clear-BitLockerAutoUnlock](./Clear-BitLockerAuto Unlock.md)

[Enable-BitlockerAutoUnlock](./Enable-BitLockerAutoUnlock.md)

[Get-BitLockerVolume](./Get-BitLockerVolume.md)

