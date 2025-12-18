---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BitLocker-help.xml
Module Name: BitLocker
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitlocker/backup-bitlockerkeyprotector?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Backup-BitLockerKeyProtector
---

# 备份 BitLocker 密钥保护器

## 摘要
在 Active Directory Domain Services (AD DS) 中为 BitLocker 卷保存一个密钥保护器。

## 语法

```
Backup-BitLockerKeyProtector [-MountPoint] <String[]> [-KeyProtectorId] <String> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Backup-BitLockerKeyProtector` cmdlet 用于将受 BitLocker 驱动器加密保护的卷的恢复密码密钥保护器保存到 Active Directory 域服务（AD DS）中。请通过 ID 指定要保存的密钥。

有关 BitLocker 的概述，请参阅 TechNet 上的 [BitLocker 驱动器加密概述](https://technet.microsoft.com/en-us/library/cc732774.aspx)。

## 示例

### 示例 1：为某个卷保存一个密钥保护器
```
PS C:\> $BLV = Get-BitLockerVolume -MountPoint "C:"
PS C:\> Backup-BitLockerKeyProtector -MountPoint "C:" -KeyProtectorId $BLV.KeyProtector[1].KeyProtectorId
```

这个示例为指定的 BitLocker 卷保存了一个密钥保护器。

第一个命令使用 **Get-BitLockerVolume** 来获取一个 BitLocker 卷，并将其存储在变量 $BLV 中。

第二个命令用于备份由 *MountPoint* 参数指定的 BitLocker 卷的密钥保护器。该命令通过使用存储在 $BLV 中的 BitLocker 对象中的密钥保护器的 ID 来指定该密钥保护器。**KeyProtector** 属性包含与该卷关联的所有密钥保护器。此命令使用标准的数组语法来索引 **KeyProtector** 对象。可以通过查看 **KeyProtector** 对象中的 **KeyProtectorType** 属性来确定与恢复密码相关的密钥保护器。

### 示例 2：使用 ID 保存密钥保护器
```
PS C:\> Backup-BitLockerKeyProtector -MountPoint "C:" -KeyProtectorId "{E2611001E-6AD0-4A08-BAAA-C9c031DB2AA6}"
```

此命令将指定的 BitLocker 卷对应的密钥保护器保存到 Active Directory Domain Services (AD DS) 中。该命令通过使用密钥保护器的 ID 来指定它。

## 参数

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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

### -KeyProtectorId
用于指定密钥保护器（Key Protector）对象的ID。BitLocker卷对象中包含一个KeyProtector对象。您可以指定该KeyProtector对象本身，也可以仅指定其ID。具体用法请参见“示例”部分。要获取BitLocker卷对象，请使用Get-BitLockerVolume cmdlet命令。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -MountPoint
指定一个包含驱动器字母或 BitLocker 卷对象的数组。该cmdlet会为所指定的卷保存密钥保护器（key protector）。要获取 BitLocker 卷对象，请使用 **Get-BitLockerVolume** cmdlet。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### BitLockerVolume

### 字符串

## 输出

### BitLockerVolume

## 备注

## 相关链接

[Add-BitLockerKeyProtector](./Add-BitLockerKeyProtector.md)

[Get-BitLockerVolume](./Get-BitLockerVolume.md)

[Remove-BitLockerKeyProtector](./Remove-BitLockerKeyProtector.md)

