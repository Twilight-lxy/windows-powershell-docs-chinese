---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BitLocker-help.xml
Module Name: BitLocker
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitlocker/enable-bitlockerautounlock?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-BitLockerAutoUnlock
---

# 启用 BitLocker 的自动解锁功能

## 摘要
启用BitLocker卷的自动解锁功能。

## 语法

```
Enable-BitLockerAutoUnlock [-MountPoint] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Enable-BitLockerAutoUnlock` cmdlet 可以为受 BitLocker 磁盘加密保护的卷启用自动解锁功能。

你可以配置 BitLocker，使其自动解锁那些不包含操作系统的卷。当用户解锁了操作系统所在的卷后，BitLocker 会使用存储在注册表和卷元数据中的加密信息来解锁所有启用自动解锁功能的数据卷。

有关 BitLocker 的概述，请参阅 TechNet 上的 [BitLocker 驱动器加密概述](https://technet.microsoft.com/en-us/library/cc732774.aspx)。

## 示例

### 示例 1：启用自动解锁功能
```
PS C:\>Enable-BitLockerAutoUnlock -MountPoint "E:"
```

此命令可启用对指定BitLocker卷的自动解锁功能。

## 参数

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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
指定一个驱动器字母数组或 BitLocker 卷对象。该 cmdlet 可以实现对所指定卷的自动解锁功能。若要获取 BitLocker 卷对象，请使用 **Get-BitLockerVolume** cmdlet。

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### BitLockerVolume[], String[]

## 输出

### BitLockerVolume[]

## 备注

## 相关链接

[Clear-BitLockerAutoUnlock](./Clear-BitLockerAutoUnlock.md)

[Disable-BitLockerAutoUnlock](./Disable-BitLockerAutoUnlock.md)

[Get-BitLockerVolume](./Get-BitLockerVolume.md)

