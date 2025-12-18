---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BitLocker-help.xml
Module Name: BitLocker
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitlocker/disable-bitlocker?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-BitLocker
---

# 禁用BitLocker

## 摘要
禁用某个卷的 BitLocker 驱动器加密功能。

## 语法

```
Disable-BitLocker [-MountPoint] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Disable-BitLocker` cmdlet 用于禁用 BitLocker 对卷的加密功能。运行此 cmdlet 时，它会删除所有密钥保护机制，并开始解密该卷中的数据。

如果包含操作系统的卷中存在任何自动解锁密钥，该cmdlet将不会继续执行。你可以使用**Clear-BitLockerAutoUnlock** cmdlet来删除所有自动解锁密钥，之后就可以禁用该卷上的BitLocker功能了。

有关 BitLocker 的概述，请参阅 TechNet 上的 [BitLocker 驱动器加密概述](https://technet.microsoft.com/en-us/library/cc732774.aspx)。

## 示例

#### 示例 1：禁用某个卷的 BitLocker 功能
```
PS C:\> Disable-BitLocker -MountPoint "C:"
```

此命令将禁用指定BitLocker卷的BitLocker功能。BitLocker会立即开始解密C:盘上的数据。

### 示例 2：禁用所有卷的 BitLocker 功能
```
PS C:\>$BLV = Get-BitLockerVolume
PS C:\>Disable-BitLocker -MountPoint $BLV
```

这个示例会禁用所有卷的 BitLocker 加密功能。

第一个命令使用 **Get-BitLockerVolume** 来获取当前计算机上的所有 BitLocker 加密卷，并将它们存储在 `$BLV` 变量中。

第二个命令会禁用存储在 `$BLV` 变量中的所有 BitLocker 卷的 BitLocker 加密功能。随后，BitLocker 会开始解密这些卷上的数据。

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
指定一个包含驱动器字母或 BitLocker 卷对象的数组。该 cmdlet 会禁用所指定卷的保护功能。若要获取 BitLocker 卷对象，请使用 **Get-BitLockerVolume** cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### BitLockerVolume[], String[]

## 输出

### BitLockerVolume[]

## 备注

## 相关链接

[Enable-BitLocker](./Enable-BitLocker.md)

[Get-BitLockerVolume](./Get-BitlockerVolume.md)

[Lock-BitLocker](./Lock-BitLocker.md)

[Resume-BitLocker](./Resume-BitLocker.md)

[暂停 BitLocker 功能](./Suspend-BitLocker.md)

[解锁 BitLocker](./Unlock-BitLocker.md)

