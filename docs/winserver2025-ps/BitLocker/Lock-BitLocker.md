---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BitLocker-help.xml
Module Name: BitLocker
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitlocker/lock-bitlocker?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Lock-BitLocker
---

# Lock-BitLocker

## 摘要
防止访问使用 BitLocker 加密的保护卷中的加密数据。

## 语法

```
Lock-BitLocker [-MountPoint] <String[]> [-ForceDismount] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Lock-Bitlocker` cmdlet 可以阻止对使用 BitLocker 驱动器加密技术的卷上的所有加密数据的访问。你可以使用 `Unlock-BitLocker` cmdlet 来恢复对这些数据的访问权限。

您可以通过驱动器字母来指定要锁定的卷，或者可以直接指定一个 BitLocker 卷对象。此 cmdlet 无法锁定包含操作系统的卷；如果您尝试锁定已经处于锁定状态的卷，该 cmdlet 将不会执行任何操作。

有关 BitLocker 的概述，请参阅 TechNet 上的 [BitLocker 磁盘加密概述](https://technet.microsoft.com/en-us/library/cc732774.aspx)。

## 示例

#### 示例 1：锁定一个卷
```
PS C:\> Lock-BitLocker -MountPoint "E:" -ForceDismount
```

此命令用于锁定通过 *MountPoint* 参数指定的 BitLocker 卷。该命令使用了 *ForceDismount* 参数，因此即使卷正在使用中，cmdlet 也会尝试锁定它。

## 参数

### -Confirm
在运行 cmdlet 之前，会提示您进行确认。

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

### -ForceDismount
表示即使驱动器正在使用中，该cmdlet也会尝试锁定它。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: fd

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MountPoint
用于指定一组驱动器字母或 BitLocker 卷对象。该 cmdlet 会尝试锁定所指定的卷。若要获取 BitLocker 卷对象，请使用 **Get-BitLockerVolume** cmdlet。

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
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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

[禁用BitLocker](./Disable-BitLocker.md)

[Enable-BitLocker](./Enable-BitLocker.md)

[Get-BitLockerVolume](./Get-BitLockerVolume.md)

[简历 - BitLocker](./Resume-BitLocker.md)

[暂停 BitLocker 功能](./Suspend-BitLocker.md)

[解锁 BitLocker](./Unlock-BitLocker.md)

